import json
import requests
from openai import OpenAI

from pprint import pprint
from dotenv import load_dotenv
_ = load_dotenv()

# --- Função que retorna o clima ---
def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']


# --- Etapa 1: chamar o modelo com a ferramenta get_weather definida ---
# Modelo de chamada com funções definidas – junto com seu sistema e mensagens do usuário.


client = OpenAI()

tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for provided coordinates in celsius.",
    "parameters": {
        "type": "object",
        "properties": {
            "latitude": {"type": "number"},
            "longitude": {"type": "number"}
        },
        "required": ["latitude", "longitude"],
        "additionalProperties": False
    },
    "strict": True
}]

input_messages = [{"role": "user", "content": "Como está o tempo em São Paulo hoje?"}]

response = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
)

# --- Etapa 2: O modelo decide chamar função(ões) – o modelo retorna o nome e os argumentos de entrada. ---
pprint(response.output[0].model_dump())

# --- Etapa 3: Executar código de função – analisar a resposta do modelo e manipular chamadas de função. ---
tool_call = response.output[0]
args = json.loads(tool_call.arguments)

result = get_weather(args["latitude"], args["longitude"])

# --- Etapa 4: Forneça resultados ao modelo – para que ele possa incorporá-los em sua resposta final. ---
input_messages.append(tool_call)  # append model's function call message
input_messages.append({           # append result message
    "type": "function_call_output",
    "call_id": tool_call.call_id,
    "output": str(result)
})

response_2 = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
)

# --- Etapa 5: O modelo responde – incorporando o resultado em sua saída. ---
print(response_2.output_text)


