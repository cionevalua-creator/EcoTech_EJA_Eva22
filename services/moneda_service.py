import requests
import os
from dotenv import load_dotenv

load_dotenv()

class MonedaService:
    @staticmethod
    def obtener_indicador(moneda):
        api_key = os.getenv("API_MONEDA_KEY", "clave_segura_simulada")
        url = f"https://mindicador.cl/api/{moneda}"
        
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            return {
                "moneda": moneda,
                "valor": f"${data['serie'][0]['valor']} CLP",
                "fecha": data['serie'][0]['fecha'][:10]
            }
        except (requests.exceptions.RequestException, KeyError, IndexError):
            return {
                "moneda": moneda,
                "valor": "$950.00 CLP (Modo sin conexión activado)",
                "fecha": "Actual"
            }