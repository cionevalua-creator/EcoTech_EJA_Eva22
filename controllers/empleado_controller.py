from models.empleado import Empleado
from models.empleado_dao import EmpleadoDao 
from views.empleado_view import EmpleadoView

class EmpleadoController:
    def __init__(self):
        self.view = EmpleadoView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_empleado()
            elif opcion == 2:
                self.imprimir_empleados()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestion de empleados.....")
                break
            else:
                self.view.mostrar_mensaje("Opcion no valida.")

    def agregar_empleado(self) -> None:
        datos = self.view.formulario_nv_empleado()
        try:
            nuevo_empleado = Empleado(None, datos['nombre'], datos['correo'], datos['fecha_inicio'], datos['direccion'], datos['telefono'], datos['salario'], datos['id_departamento'], datos['id_proyecto'], datos['id_usuario'])
            exito = EmpleadoDao.crear(nuevo_empleado)

            if exito:
                self.view.mostrar_mensaje(f"Empleado agregado con exto (ID: {nuevo_empleado.id_empleado})")
            else:
                self.view.mostrar_mensaje("Error interno al guardar en la base de datos.")
        except ValueError as e:
            self.view.mostrar_mensaje(f"Error en los datos: {e}")

    def imprimir_empleado(self) -> None:
        empleados = EmpleadoDao.obtener_datos()
        self.view.mostrar_lista_empleados(empleados)