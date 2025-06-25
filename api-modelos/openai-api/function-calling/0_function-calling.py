# https://platform.openai.com/docs/guides/function-calling

from dotenv import load_dotenv
from openai import OpenAI

from pprint import pprint
_ = load_dotenv()

client = OpenAI()

tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country e.g. Bogotá, Colombia"
            }
        },
        "required": [
            "location"
        ],
        "additionalProperties": False
    }
}]

response = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "What is the weather like in Santos today?"}],
    tools=tools
)

print(response.output)

# json
pprint(response.output[0].model_dump())

