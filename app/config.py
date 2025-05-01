import os
from dotenv import load_dotenv

# Carga las variables desde .env al entorno
load_dotenv()

# Variables necesarias en todo el sistema
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Validaciones mínimas
if not OPENAI_API_KEY:
    raise ValueError("❌ Falta la variable OPENAI_API_KEY en el archivo .env")
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("❌ Falta la variable TELEGRAM_BOT_TOKEN en el archivo .env")
