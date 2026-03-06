import httpx
import json
import os
from openai import OpenAI

from tool_definitions import TOOLS_DEFINITIONS, TOOLS
from openai_config import BASE_URL, KEY, MODEL


def execute_tool(tool_name, arguments):
    cmd = TOOLS_DEFINITIONS[tool_name]["command"](arguments)
    if hostname := arguments.get("hostname"):
        cmd += f" -h {hostname}"

    flag = False   # Set to True to actually execute the command
    if flag:
        print(f"Running {cmd} ...")
        os.system(cmd)
    else:
        print(cmd)
    return cmd

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

    http_client = httpx.Client(verify=True)

    client = OpenAI(
        api_key = KEY,
        http_client=http_client
    )
    client.base_url = BASE_URL
    response = client.chat.completions.create(
        model=MODEL,
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
            command = execute_tool(function_name, function_args)
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
        user_input = input("Input: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting.")
            break

        if not user_input.strip():
            continue

        print("\nProcessing...")

        try:
            result = suggest_command(user_input, messages)

            if isinstance(result, list):
                print("\n[Suggested Commands]")
                for i, suggestion in enumerate(result, 1):
                    print(f"{i}. {suggestion['action']}")
                    print(f"   Command: {suggestion['command']}")
                print()
            elif result:
                print(f"\n{result}\n")
            else:
                print("\n[WARNING] No response was received from the LLM. Please try again.\n")

        except Exception as e:
            print(f"\nAn error occurred: {e}\n")


if __name__ == "__main__":
    main()
