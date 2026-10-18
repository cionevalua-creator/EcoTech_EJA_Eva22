from models.departamento import Departamento
from models.departamento_dao import DepartamentoDao
from views.departamento_view import DepartamentoView

class DepartamentoController:
    def __init__(self):
        self.view = DepartamentoView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_departamento()
            elif opcion == 2:
                self.mostrar_departamento()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestion de departamentos.")
                break
            else:
                self.view.mostrar_mensaje("Opcion no valida.")

    def agregar_departamento(self) -> None:
        datos = self.view.formaulario_nv_departamento()
        try:
            nuevo_departamento = Departamento(None, datos['nombre'], datos['gerente_asociado'])
            exito = DepartamentoDao.crear(nuevo_departamento)

            if exito:
                self.view.mostrar_mensaje(f"Departamento agregado con exito (ID: {nuevo_departamento.id_departamento})")
            else:
                self.view.mostrar_mensaje(f"Error al intentar guardar en la base de datos.")
        except ValueError as e:
            self.view.mostrar_mensaje(f"Error en los datos ingresados: {e}")

    def mostrar_departamento(self) -> None:
        departamentos = DepartamentoDao.obtener_datos()
        self.view.mostrar_lista_departamentos(departamentos)