from views.utils import leer_numero
from models.proyecto import Proyecto
from datetime import date

class ProyectoView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("     GESTION DE PROYECTOS")
        print("-" * 30)
        print("1.   AGREGAR PROYECTOS")
        print("2.   MOSTRAR TODOS LOS PROYECTOS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return leer_numero("Seleccione una opcion: ")

    @staticmethod
    def formulario_nv_proyecto() -> dict:
        print("\n--- AGREGAR NUEVO PROYECTO ---")
        nombre = input("Nombre del proyecto: ")
        descripcion = input("Descripcion: ")

        print("FECHA DE INICIO: ")
        anio = leer_numero(" Año: ")
        mes = leer_numero(" Mes: ")
        dia = leer_numero(" Día: ")
        fecha_inicio = date(anio, mes, dia)

        id_departamento = leer_numero("Ingrese el (ID) del departamento a cargo: ")

        return {"nombre": nombre, "descripcion": descripcion, "fecha_inicio": fecha_inicio, "id_departamento": id_departamento}

    @staticmethod
    def mostrar_lista_proyectos(proyectos: list[Proyecto]) -> None:
        print("\n--- LISTA DE PROYECTOS ---")
        if not proyectos:
            print("No hay proyectos registrados.")
        else:
            for p in proyectos:
                print(f"ID: {p.id_proyecto} | Nombre: {p.nombre} | ID Departamento: {p.id_departamento}")
        print("-" * 30)

    @staticmethod
    def mostrar_mensaje(mensaje:str) -> None:
        print(f"[PROYECTO] {mensaje}")