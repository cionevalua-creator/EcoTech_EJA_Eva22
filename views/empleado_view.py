from views.utils import leer_numero
from models.empleado import Empleado
from datetime import date

class EmpleadoView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("     GESTION DE EMPLEADOS")
        print("-" * 30)
        print("1.   AGREGAR EMPLEADO")
        print("2.   MOSTRAR TODOS LOS EMPLEADOS")
        print("0.   VOLVER AL (MENU PRINCIAL)")
        print("-" * 30)
        return leer_numero("Seleccione una opcion: ")

    @staticmethod
    def formulario_nv_empleado() -> dict:
        print("\n--- AGREGAR NUEVO EMPLEADO ---")
        nombre = input("Nombre: ")
        correo = input("Correo: ")

        print("FECHA DE INICIO: ")
        anio = leer_numero(" Año (EJ: 2026) : ")
        mes = leer_numero(" MES (1-12) : ")
        dia = leer_numero(" DIA (1-31) : ")
        fecha_inicio = date(anio, mes, dia)

        direccion = input("Direccion: ")
        telefono = input("Telfono: ")

        while True:
            try:
                salario = float(input("Salario: "))
                break
            except ValueError:
                print("Error: Ingrese un numero valido en salario.")

        id_departamento = leer_numero("ID del departamento asignado: ")
        id_proyecto = leer_numero("ID del proyecto asignado: ")
        id_usuario = leer_numero("ID del usuario del sistema: ")

        return{"nombre":nombre, "correo":correo, "fecha_inicio":fecha_inicio, "direccion":direccion, "telefono":telefono, "salario":salario, "id_departamento":id_departamento, "id_proyecto":id_proyecto, "id_usuario":id_usuario}

    @staticmethod
    def mostrar_lista_empleados(empleados: list[Empleado]) -> None:
        print("\n--- LISTA DE EMPLEADOS ---")
        if not empleados:
            print("No hay empleados registrados.")
        else:
            for e in empleados:
                print(f"ID: {e.id_empleado} | Nombre: {e.nombre} | Correo: {e.correo} | Telefono: {e.telefono}")

        print("-" * 30)

    @staticmethod
    def mostrar_mensaje(mensaje:str) -> None:
        print(f"[EMPLEADOS] {mensaje}")

