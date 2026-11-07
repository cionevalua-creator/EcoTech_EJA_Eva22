import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ClimaService:
    @staticmethod
    def obtener_clima(ciudad):
        api_key = os.getenv("API_CLIMA_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
        
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            
            return {
                "temperatura": f"{data['main']['temp']}°C",
                "humedad": f"{data['main']['humidity']}%",
                "estado": data['weather'][0]['description']
            }
        except requests.exceptions.RequestException:

            return {
                "temperatura": "20°C",
                "humedad": "45%",
                "estado": "Despejado (Modo sin conexión activado)"
            }