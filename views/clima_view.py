class ClimaView:
    def mostrar_menu(self):
        print("\n--- MÓDULO CLIMA ---")
        print("1. Consultar clima de una ciudad")
        print("0. Volver al menú principal")
        print("-" * 40)
        return int(input("Seleccione una opción: "))

    def pedir_ciudad(self):
        while True:
            ciudad = input("Ingrese la ciudad a consultar: ").strip()
            if ciudad:
                return ciudad
            print("Error: La ciudad no puede estar vacía. Intente de nuevo.")

    def mostrar_resultado(self, datos):
        if "error" in datos:
            print("-" * 40)
            print(f"Error: {datos['error']}")
            print("-" * 40)
        else:
            print("_" * 60)
            print(f"Temperatura actual: {datos['temperatura']}")
            print(f"Humedad: {datos['humedad']}")
            print(f"Estado del clima: {datos['estado']}")
            print("_" * 60)