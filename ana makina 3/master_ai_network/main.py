from models.air_ai import AirAI
from config.settings import SYSTEM_NAME
from config.security import initialize_security

def main():
    try:
        print(f"{SYSTEM_NAME} initializing...")
        air = AirAI()
        response = air.respond("Test command")
        print(f"AI Response: {response}")
    except Exception as e:
        print(f"Hata oluştu: {type(e).__name__}\n{e}")
