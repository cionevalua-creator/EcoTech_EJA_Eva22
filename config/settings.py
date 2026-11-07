import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

class Settings:
    API_CLIMA_URL: str = os.getenv("API_CLIMA_URL", "")
    API_CLIMA_KEY: str = os.getenv("API_CLIMA_KEY", "")
    API_DIVISAS_URL: str = os.getenv("API_DIVISAS_URL", "")
    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "5"))
    ENABLE_OFFLINE_FALLBACK: bool = os.getenv("ENABLE_OFFLINE_FALLBACK", "True").lower() in ("true", "1", "yes")