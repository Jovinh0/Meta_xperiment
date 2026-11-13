import base64
import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Cargar las llaves del archivo .env
load_dotenv(override=True)
meta_key = os.getenv("MODEL_API_KEY").strip()

print("Conectando con la API oficial de Meta...")

# 2. Configurar el cliente con la URL correcta que indica la documentación
client = OpenAI(
    base_url="https://api.meta.ai/v1",
    api_key=meta_key,
)

# 3. Solicitar la generación de la imagen usando el modelo muse-image-1.0
prompt = "A futuristic cyberpunk red panda in a neon city, highly detailed, 4k"

try:
    response = client.responses.create(
        model="muse-image-1.0",
        input=prompt
    )

    print("¡Respuesta recibida! Buscando y guardando la imagen...")

    # 4. Extraer la imagen usando la función de análisis de resultados de Meta
    b64_data = next(
        item.result
        for item in response.output
        if item.type == "image_generation_call"
    )

    image_data = base64.b64decode(b64_data)

    # Guardar como archivo PNG
    with open("mi_primera_imagen.png", "wb") as f:
        f.write(image_data)

    print("¡Listo! Tu imagen se guardó con éxito como 'mi_primera_imagen.png'.")

except Exception as e:
    print("Ocurrió un error al procesar la respuesta:")
    print(e)