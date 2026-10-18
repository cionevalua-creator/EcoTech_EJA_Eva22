from views.main_view import MainView
from controllers.departamento_controllers import DepartamentoController
from controllers.empleado_controller import EmpleadoController

class MainController:
    def __init__(self):
        self.view = MainView()
        self.departamento_controller = DepartamentoController()
        self.empleado_controller = EmpleadoController()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.departamento_controller.ejecutar()
            elif opcion == 2:
                self.empleado_controller.ejecutar()
            elif opcion == 3:
                self.view.mostrar_mensaje("Modulos de proyectos en construccion...")
            elif opcion == 4:
                self.view.mostrar_mensaje("Modulo de registros en construccion...")
            elif opcion == 0:
                self.view.mostrar_mensaje("Gracias por usar el sistema ECOTECH hasta pronto.")
                break
            else:
                self.view.mostrar_mensaje("Opcion no valida. por favor intente nuevamente.")
                