from dotenv import load_dotenv
from openai import OpenAI
_ = load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input="Escreva uma frase sobre Inteligência Artificial."
)

print(response.output_text)
