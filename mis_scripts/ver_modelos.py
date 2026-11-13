import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client = OpenAI(
    base_url="https://api.meta.ai/v1",
    api_key=os.getenv("MODEL_API_KEY").strip(),
)

print("📋 Modelos disponibles para tu llave de Meta:\n")
modelos = client.models.list()
for m in modelos.data:
    print(" -", m.id)