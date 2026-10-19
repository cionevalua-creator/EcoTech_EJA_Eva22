from models.proyecto import Proyecto
from models.proyecto_dao import Proyecto_Dao
from views.proyecto_view import ProyectoView

class ProyectoController:
    def __init__(self):
        self.view = ProyectoView()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_proyecto()
            elif opcion == 2:
                self.mostrar_lista_proyectos()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestion de proyectos...")
                break
            else:
                self.view.mostrar_mensaje("Opcion no valida.")

    def agregar_proyecto(self) -> None:
        datos = self.view.formulario_nv_proyecto()
        try:
            nuevo_proyecto = Proyecto(None, datos['nombre'], datos['descripcion'], datos['fecha_inicio'], datos['id_departamento'])
            exito = Proyecto_Dao.crear(nuevo_proyecto)

            if exito:
                self.view.mostrar_mensaje(f"Proyecto agregado con exito: (ID: {nuevo_proyecto.id_proyecto})")
            else:
                self.view.mostrar_mensaje("Error interno al guardar en la base de datos.")
        except ValueError as e:
            self.view.mostrar_mensaje(f"Error en la base de datos: {e}")

    def mostrar_lista_proyectos(self) -> None:
        proyectos = Proyecto_Dao.obtener_datos()
        self.view.mostrar_lista_proyectos(proyectos)