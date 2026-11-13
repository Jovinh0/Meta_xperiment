# 🚀 Meta_xperiment: Integración Multimodal de Meta IA

Este repositorio contiene una arquitectura de software limpia y funcional para la integración de los modelos de inteligencia artificial de Meta, utilizando créditos de desarrollador y la estructura base de `llama-recipes`. 

El proyecto demuestra la implementación práctica de tres capacidades principales (Visión, Agentes y Audio) mediante llamadas directas a la API de Meta.

## 📁 Arquitectura del Proyecto

El entorno está diseñado bajo buenas prácticas de ingeniería de software, separando el código fuente, los recursos multimedia de entrada y los resultados generados:

```text
Meta_xperiment/
├── assets/                 # Archivos de entrada (audio_prueba.mp3, imagen_generada.webp)
├── outputs/                # Resultados generados por la IA (.png, .srt)
├── mis_scripts/            # Scripts de ejecución categorizados
│   ├── agentes/            # Lógica de subagentes y procesamiento en paralelo
│   ├── audio/              # Transcripción de voz a texto
│   ├── vision/             # Generación y edición de imágenes
│   ├── multimodal_meta.py  # Script maestro de validación de conexión
│   └── ver_modelos.py      # Explorador del catálogo de modelos
├── llama-recipes/          # Repositorio original de Meta (core)
├── .env                    # Variables de entorno (Ignorado en Git)
├── .gitignore              # Archivos excluidos del control de versiones
└── README.md               # Documentación del proyecto
