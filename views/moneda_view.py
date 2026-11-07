class MonedaView:
    def mostrar_menu(self):
        print("\n--- MÓDULO INDICADORES ECONÓMICOS ---")
        print("1. Consultar valor de moneda (dolar, euro)")
        print("0. Volver al menú principal")
        print("-" * 40)
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            return -1

    def pedir_moneda(self):
        while True:
            moneda = input("Ingrese la moneda a consultar (dolar, euro): ").strip().lower()
            if moneda:
                return moneda
            print("Error: La moneda no puede estar vacía. Intente de nuevo.")

    def mostrar_resultado(self, datos):
        if "error" in datos:
            print("-" * 40)
            print(f"Error: {datos['error']}")
            print("-" * 40)
        else:
            print("_" * 60)
            print(f"Moneda: {datos['moneda'].capitalize()}")
            print(f"Valor: {datos['valor']}")
            print(f"Fecha de indicador: {datos['fecha']}")
            print("_" * 60)