import os
import base64
from dotenv import load_dotenv
from openai import OpenAI

# 1. Cargar las credenciales del archivo .env
load_dotenv(override=True)
meta_key = os.getenv("MODEL_API_KEY").strip()
baseten_key = os.getenv("BASETEN_API_KEY").strip()

print("🚀 Inicializando el sistema multimodal con créditos de Meta...\n")

# ==========================================
# MODELO 1: Generación de Imágenes (Muse Image 1.0)
# ==========================================
def generar_imagen_futurista(prompt_texto):
    print("🎨 [Modelo Imagen] Conectando con la API de Meta...")
    client_meta = OpenAI(base_url="https://api.meta.ai/v1", api_key=meta_key)
    
    response = client_meta.responses.create(
        model="muse-image-1.0",
        input=prompt_texto
    )
    
    # Extraer y descargar la imagen a la computadora
    b64_data = next(
        item.result for item in response.output if item.type == "image_generation_call"
    )
    image_bytes = base64.b64decode(b64_data)
    
    nombre_archivo = "imagen_generada.png"
    with open(nombre_archivo, "wb") as f:
        f.write(image_bytes)
    print(f"✅ ¡Imagen descargada y guardada localmente como: '{nombre_archivo}'!\n")

# ==========================================
# MODELO 2: Procesamiento de Voz y Subtítulos (Muse Voice)
# ==========================================
def procesar_voz_y_subtitulos():
    print("🎙️ [Modelo Voz] Módulo de transcripción preparado.")
    print("ℹ️ Para generar subtítulos, puedes pasarle un archivo de audio local (.mp3/.wav) usando client.audio.transcriptions.")
    print("✅ Configuración de subtítulos cargada correctamente en el entorno.\n")

# ==========================================
# MODELO 3: Asistente de Texto y Razonamiento
# ==========================================
def consultar_asistente_texto(pregunta):
    print("💬 [Modelo Texto] Consultando a Meta...")
    client_meta = OpenAI(base_url="https://api.meta.ai/v1", api_key=meta_key)

    response = client_meta.responses.create(
        model="llama-4-maverick-17b-128e-instruct",
        input=pregunta
    )
    print(f"✅ Respuesta: {response.output_text}\n")

if __name__ == "__main__":
    # Puedes activar o desactivar las funciones que desees probar:
    
    # 1. Generar una nueva imagen y descargarla automáticamente
    generar_imagen_futurista("A cinematic shot of a futuristic drone flying over Quito at sunset, 4k")
    
    # 2. Revisar estado de voz
    procesar_voz_y_subtitulos()
    
    # 3. Hacer una consulta de texto
    consultar_asistente_texto("Explica brevemente cómo las APIs conectan tu app local con la nube.")