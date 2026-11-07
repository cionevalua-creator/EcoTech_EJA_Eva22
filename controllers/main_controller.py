from views.main_view import MainView
from controllers.empleado_controller import EmpleadoController
from controllers.departamento_controllers import DepartamentoController
from controllers.proyecto_controller import ProyectoController
from controllers.registrotiempo_controllers import RegistroTiempoController
from controllers.usuario_controller import UsuarioController
from controllers.clima_controller import ClimaController
from controllers.moneda_controller import MonedaController

class MainController:
    def __init__(self):
        self.view = MainView()
        self.empleado_controller = EmpleadoController()
        self.departamento_controller = DepartamentoController()
        self.proyecto_controller = ProyectoController()
        self.registrotiempo_controller = RegistroTiempoController()
        self.usuario_controller = UsuarioController()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.empleado_controller.ejecutar()
            elif opcion == 2:
                self.departamento_controller.ejecutar()
            elif opcion == 3:
                self.proyecto_controller.ejecutar()
            elif opcion == 4:
                self.registrotiempo_controller.ejecutar()
            elif opcion == 5:
                self.usuario_controller.ejecutar()
            elif opcion == 6:
                clima_app = ClimaController()
                clima_app.ejecutar()
            elif opcion == 7:
                moneda_app = MonedaController()
                moneda_app.ejecutar()
            elif opcion == 0:
                self.view.mostrar_mensaje("Gracias por usar el sistema ECOTECH. ¡Hasta pronto!")
                break
            else:
                self.view.mostrar_mensaje("Opcion no valida. Por favor intente nuevamente.")