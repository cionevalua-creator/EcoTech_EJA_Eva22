from views.utils import leer_numero
from models.registrotiempo import RegistroTiempo
from datetime import date

class RegistroTiempoView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("     GESTION DE REGISTROS DE TIEMPO")
        print("-" * 30)
        print("1.   AGREGAR REGISTRO")
        print("2.   MOSTRAR TODOS LOS REGISTROS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return leer_numero("Seleccione una opcion: ")

    @staticmethod
    def formulario_nv_registro() -> dict:
        print("\n--- AGREGAR NUEVO REGISTRO ---")
        
        print("FECHA DEL REGISTRO:")
        anio = leer_numero(" Año: ")
        mes = leer_numero(" MES: ")
        dia = leer_numero(" DIA: ")
        fecha = date(anio, mes, dia)

        horas = leer_numero("Horas trabajadas: ")

        descripcion = input("Descripcion de la tarea: ")
        id_empleado = leer_numero("ID del Empleado: ")
        id_proyecto = leer_numero("ID del Proyecto: ")

        return {
            "fecha": fecha,
            "horas_trabajadas": horas,
            "descripcion": descripcion,
            "id_empleado": id_empleado,
            "id_proyecto": id_proyecto
        }

    @staticmethod
    def mostrar_lista_registros(registros: list[RegistroTiempo]) -> None:
        print("\n--- LISTA DE REGISTROS ---")
        if not registros:
            print("No hay registros guardados.")
        else:
            for r in registros:
                print(f"ID: {r.id_registrotiempo} | Fecha: {r.fecha} | Horas: {r.horas_trabajadas} | Emp ID: {r.id_empleado} | Proy ID: {r.id_proyecto}")
        print("-" * 30)

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[REGISTROS] {mensaje}")