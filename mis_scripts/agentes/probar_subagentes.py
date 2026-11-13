import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
client = OpenAI(
    base_url="https://api.meta.ai/v1",
    api_key=os.getenv("MODEL_API_KEY").strip(),
)

# El "Padre" coordina subtareas independientes (simulando el patrón de distribución)
subtareas = [
    "Subagente 1: Diseña la estructura de carpetas para un backend en Python.",
    "Subagente 2: Redacta 3 pruebas unitarias básicas para validar una API.",
]

print("🤖 Iniciando distribución de tareas entre subagentes...\n")

for tarea in subtareas:
    print(f"📌 Enviando a subagente: {tarea}")

    respuesta = client.chat.completions.create(
        model="muse-spark-1.3",
        messages=[{"role": "user", "content": tarea}]
    )

    resultado_texto = respuesta.choices[0].message.content
    print(f"✅ Resultado del subagente:\n{resultado_texto}\n" + "-"*40)