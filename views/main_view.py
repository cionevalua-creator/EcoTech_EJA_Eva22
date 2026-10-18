from views.utils import leer_numero

class MainView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("     ECOTECH - MENU PRINCIPAL")
        print("-" * 30)
        print("1.   GESTION DE EMPLEADOS")
        print("2.   GESTION DE DEPARTAMENTOS")
        print("3.   GESTION DE PROYECTOS")
        print("4.   REGISTRO TIEMPO")
        print("0.   SALIR")
        print("-" * 30)
        return leer_numero("Seleccione una opcion: ")

    @staticmethod
    def mostrar_mensaje(mensaje:str) -> None:
        print(f"\n [SISTEMA] {mensaje}")
        