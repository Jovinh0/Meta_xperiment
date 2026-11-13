import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

# 1. Cargar tus credenciales de Meta
load_dotenv(override=True)
client = OpenAI(
    base_url="https://api.meta.ai/v1",
    api_key=os.getenv("MODEL_API_KEY").strip(),
)

print("🎨 Enviando tu imagen original a los servidores de Meta para editarla...")

try:
    # 2. Abrimos la imagen del dron que generaste antes
    with open("imagen_generada.webp", "rb") as imagen_original:
        
        # 3. Usamos la función images.edit que encontraste en la documentación
        response = client.images.edit(
            model="muse-image-1.0",
            # Le pedimos que agregue un elemento nuevo sin dañar el resto
            prompt="add a glowing neon billboard floating in the sky, keep the futuristic drone and the sunset over Quito background exactly the same",
            image=imagen_original,
            n=1,
        )

    print("✅ ¡Edición completada! Descargando resultado...")

    # 4. Extraer y guardar la nueva imagen editada
    image_data = base64.b64decode(response.data[0].b64_json)
    
    with open("imagen_editada.png", "wb") as f:
        f.write(image_data)

    print("💾 Tu nueva obra de arte se guardó como 'imagen_editada.png'")

except Exception as e:
    print("❌ Ocurrió un error en la edición:", e)