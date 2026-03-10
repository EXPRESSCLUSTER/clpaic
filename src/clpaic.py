import httpx
import json
import os
import subprocess
import shlex

from openai import OpenAI

import config
from tool_definitions import TOOLS_DEFINITIONS, TOOLS


def generate_command(tool_name, arguments):
    cmd = TOOLS_DEFINITIONS[tool_name]["command"](arguments)
    if hostname := arguments.get("hostname"):
        cmd += f" -h {hostname}"
    return cmd


def execute_command(cmd):
    if not config.DRYRUN:
        print(f"Running {cmd} ...")
        try:
            cmd_list = shlex.split(cmd)
            result = subprocess.run(
                cmd_list,
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(result.stderr)
        except FileNotFoundError as e:
            print(f"[ERROR] Command not found: {e}")
        except subprocess.TimeoutExpired as e:
            print(f"[ERROR] Command timed out: {e}")
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")
    else:
        print(cmd)

def get_action_description(tool_name, arguments):
    description = TOOLS_DEFINITIONS[tool_name]["description"](arguments)
    if description is None:
        description = "Unknown operation"
    return description

def suggest_command(user_input, messages):
    messages.append({
        "role": "user",
        "content": user_input
    })

    http_client = httpx.Client(verify=config.SSL_VERIFY)

    client = OpenAI(
        api_key = config.OPENAI_API_KEY,
        http_client=http_client
    )
    client.base_url = config.OPENAI_BASE_URL
    response = client.chat.completions.create(
        model=config.OPENAI_MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )

    rsp_msg = response.choices[0].message
    messages.append({
        "role": "assistant",
        "content": rsp_msg.content,
        "tool_calls": rsp_msg.tool_calls
    })

    if rsp_msg.tool_calls:
        suggested_commands = []

        for tool_call in rsp_msg.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            # Generate command line
            command = generate_command(function_name, function_args)
            action = get_action_description(function_name, function_args)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": command
            })

            suggested_commands.append({
                "action": action, 
                "command": command,
                "tool_name": function_name,
                "arguments": function_args
            })
        return suggested_commands
    else:
        # No tool call was made
        return rsp_msg.content


def main():
    print("=== Command Line Suggestion System ===")
    print("Enter cluster operations in natural language (type 'exit' to quit)\n")

    messages = [
        {
            "role": "system",
            "content": "You are an assistant for system administrators. Suggest appropriate commands based on the user's request."
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
            result = suggest_command(user_input, messages)

            if isinstance(result, list):
                print("\n[Suggested Commands]")
                for i, suggestion in enumerate(result, 1):
                    print(f"{i}. {suggestion['action']}")
                    print(f"   Command: {suggestion['command']}")
                print()
                execute_command(result[0]["command"])
            elif result:
                print(f"\n{result}\n")
            else:
                print("\n[WARNING] No response was received from the LLM. Please try again.\n")

        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


if __name__ == "__main__":
    main()
