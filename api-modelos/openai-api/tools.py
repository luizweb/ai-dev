# https://platform.openai.com/docs/guides/tools

from dotenv import load_dotenv
from openai import OpenAI
_ = load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    tools=[{"type": "web_search_preview"}],
    input="Qual a cotação do dolar para hoje?"
)

print(response.output_text)

