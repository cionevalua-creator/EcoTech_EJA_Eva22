from views.utils import leer_numero
from models.departamento import Departamento

class DepartamentoView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("     GESTION DE DEPARTAMENTOS")
        print("-" * 30)
        print("1.   AGREGAR DEPARTAMENTO")
        print("2.   MOSTRAR TODOS LOS DEPARTAMENTOS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return leer_numero("Seleccione una opcion.")

    @staticmethod
    def formaulario_nv_departamento() -> dict:
        print("\n--- AGREGAR NUEVO DEPARTAMENTO ---")
        nombre = input("Ingrese el nombre del departamento: ")
        gerente = input("Ingrese el nombre del gerente asociado: ")

        return {
            "nombre":nombre,
            "gerente_asociado":gerente
        }

    @staticmethod
    def mostrar_lista_departamentos(departamentos: list[Departamento]) -> None:
        print("\n--- LISTA DE DEPARTAMENTOS ---")
        if not departamentos:
            print("No hay departamentos registrados.")
        else:
            for d in departamentos:
                print(f"Id: {d.id_departamento} | Nombre: {d.nombre} | Gerente: {d.gerente_asociado}")
        print("-" * 30)

    @staticmethod
    def mostrar_mensaje(mensaje:str) -> None:
        print(f"[DEPARTAMENTOS] {mensaje}")