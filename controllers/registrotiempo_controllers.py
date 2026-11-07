from models.registrotiempo import RegistroTiempo
from models.registrotiempo_dao import Registrotiempo_Dao
from views.registrotiempo_view import RegistroTiempoView

class RegistroTiempoController:
    def __init__(self):
        self.view = RegistroTiempoView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_registro()
            elif opcion == 2:
                self.imprimir_registros()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestion de registros...")
                break
            else:
                self.view.mostrar_mensaje("Opcion no valida.")

    def agregar_registro(self) -> None:
        datos = self.view.formulario_nv_registro()
        try:
            nuevo_registro = RegistroTiempo(None, datos['fecha'], datos['horas_trabajadas'], datos['descripcion'], datos['id_empleado'], datos['id_proyecto'])
            exito = Registrotiempo_Dao.crear(nuevo_registro)

            if exito:
                self.view.mostrar_mensaje(f"Registro agregado con exito (ID: {nuevo_registro.id_registrotiempo})")
            else:
                self.view.mostrar_mensaje("Error interno al guardar en la base de datos.")
        except ValueError as e:
            self.view.mostrar_mensaje(f"Error en los datos: {e}")

    def imprimir_registros(self) -> None:
        registros = Registrotiempo_Dao.obtener_datos()
        self.view.mostrar_lista_registros(registros)