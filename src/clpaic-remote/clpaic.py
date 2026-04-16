import json
import ssl
import urllib.request
import urllib.error
import base64

from openai import OpenAI

import config
from tool_definitions import TOOLS_DEFINITIONS, TOOLS


def build_api_request(tool_name, arguments):
    defn = TOOLS_DEFINITIONS[tool_name]
    method = defn["method"]
    endpoint = defn["endpoint"](arguments)
    body = defn["body"](arguments)
    url = config.CLP_BASE_URL.rstrip("/") + endpoint
    return method, url, body


def execute_api_request(method, url, body):
    if config.DRYRUN:
        body_str = f" body={json.dumps(body)}" if body else ""
        msg = f"[DRYRUN] {method} {url}{body_str}"
        print(msg)
        return {"result": {"code": 0, "message": "(dry run)"}}

    print(f"Calling {method} {url} ...")

    headers = {"Content-Type": "application/json"}

    if config.CLP_USERNAME:
        credentials = f"{config.CLP_USERNAME}:{config.CLP_PASSWORD}"
        b64 = base64.b64encode(credentials.encode()).decode()
        headers["Authorization"] = f"Basic {b64}"

    data = json.dumps(body).encode() if body else None

    if not config.SSL_VERIFY:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
    else:
        ctx = None

    req = urllib.request.Request(url, data=data, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=300) as resp:
            resp_body = resp.read().decode()
            if resp_body:
                return json.loads(resp_body)
            return {"result": {"code": 0, "message": ""}}
    except urllib.error.HTTPError as e:
        error_body = e.read().decode() if e.fp else ""
        print(f"[ERROR] HTTP {e.code}: {error_body}")
        return {"error": f"HTTP {e.code}", "detail": error_body}
    except urllib.error.URLError as e:
        print(f"[ERROR] URL error: {e.reason}")
        return {"error": str(e.reason)}
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return {"error": str(e)}


def get_action_description(tool_name, arguments):
    description = TOOLS_DEFINITIONS[tool_name]["description"](arguments)
    if description is None:
        description = "Unknown operation"
    return description


def suggest_and_execute(user_input, messages):
    messages.append({
        "role": "user",
        "content": user_input
    })

    client = OpenAI(
        api_key=config.OPENAI_API_KEY,
        base_url=config.OPENAI_BASE_URL
    )

    response = client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    rsp_msg = response.choices[0].message
    messages.append(rsp_msg.model_dump())

    if not rsp_msg.tool_calls:
        return None, rsp_msg.content

    results = []

    for tool_call in rsp_msg.tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        action = get_action_description(function_name, function_args)
        method, url, body = build_api_request(function_name, function_args)

        print(f"\n[Action] {action}")
        print(f"  {method} {url}")
        if body:
            print(f"  Body: {json.dumps(body)}")

        api_result = execute_api_request(method, url, body)

        tool_result_str = json.dumps(api_result, ensure_ascii=False)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": tool_result_str
        })

        results.append({
            "action": action,
            "method": method,
            "url": url,
            "body": body,
            "response": api_result
        })

    followup = client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    followup_msg = followup.choices[0].message
    messages.append(followup_msg.model_dump())

    return results, followup_msg.content


def main():
    print("=== EXPRESSCLUSTER REST API Chat Tool ===")
    print("Enter cluster operations in natural language (type 'exit' to quit)\n")

    messages = [
        {
            "role": "system",
            "content": (
                "You are an assistant for EXPRESSCLUSTER X system administrators. "
                "Use the available tools to interact with the EXPRESSCLUSTER REST API based on the user's request. "
                "For POST (operation) APIs, note that they are asynchronous — the response only indicates "
                "that the request was accepted, not that the operation completed. "
                "Suggest using the corresponding status-check tool to verify completion when appropriate. "
                "Respond in the same language as the user's input."
            )
        }
    ]

    while True:
        try:
            user_input = input(">>> ")
        except EOFError:
            print("\nExiting.")
            break

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting.")
            break

        if not user_input.strip():
            continue

        try:
            results, assistant_reply = suggest_and_execute(user_input, messages)

            if results:
                print("\n[API Call Results]")
                for i, r in enumerate(results, 1):
                    code = r["response"].get("result", {}).get("code")
                    if code is not None:
                        status = "Success" if code == 0 else f"Failed (code={code})"
                    else:
                        status = "Unknown"
                    print(f"\n--- Result {i}: {r['action']} [{status}] ---")
                    print(json.dumps(r["response"], indent=2, ensure_ascii=False))

            if assistant_reply:
                print(f"\n{assistant_reply}\n")
            else:
                print()

        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


if __name__ == "__main__":
    main()
