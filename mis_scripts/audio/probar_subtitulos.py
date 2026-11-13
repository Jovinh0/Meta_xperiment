import os
import requests
from dotenv import load_dotenv

# 1. Cargar la llave desde la raíz (dos carpetas hacia atrás)
ruta_env = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(ruta_env, override=True)
meta_key = os.getenv("MODEL_API_KEY").strip()

# 2. Rutas de la nueva arquitectura
ruta_audio = os.path.join(os.path.dirname(__file__), "../../assets/audio_prueba.mp3")
ruta_subtitulos = os.path.join(os.path.dirname(__file__), "../../outputs/mis_subtitulos.srt")

print("🎙️ Enviando audio directamente a Meta...")

# 3. Petición manual sin SDK para ver la respuesta real del servidor
url = "https://api.meta.ai/v1/audio/transcriptions"
headers = {
    "Authorization": f"Bearer {meta_key}"
}
archivos = {
    "file": ("audio_prueba.mp3", open(ruta_audio, "rb"), "audio/mpeg")
}
datos = {
    "model": "muse-voice-transcribe-1.0",
    "response_format": "srt"
}

try:
    respuesta = requests.post(url, headers=headers, files=archivos, data=datos)
    
    if respuesta.status_code == 200:
        print("✅ ¡Éxito! Aquí están tus subtítulos:\n")
        print(respuesta.text)
        
        # Guardar en la carpeta outputs
        with open(ruta_subtitulos, "w", encoding="utf-8") as out:
            out.write(respuesta.text)
            
        print(f"\n💾 Subtítulos guardados exitosamente en tu carpeta 'outputs'")
    else:
        print(f"❌ El servidor de Meta respondió con código {respuesta.status_code}:")
        # Aquí veremos exactamente si Meta pide .wav/.mp4 en lugar de .mp3, o si la ruta cambia
        print(respuesta.text)
        
except Exception as e:
    print("Error de conexión local:", e)