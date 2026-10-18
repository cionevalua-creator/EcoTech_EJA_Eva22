from argon2 import PasswordHasher
from models.usuario import Usuario
from models.usuario_dao import UsuarioDao
from views.usuario_view import UsuarioView

class UsuarioController:
    def __init__(self):
        self.view = UsuarioView()
        self.ph = PasswordHasher()

    def ejecutar(self) -> None:
        while True:
            opcion = self.view.mostrar_menu()
            if opcion == 1:
                self.agregar_usuario()
            elif opcion == 2:
                self.imprimir_usuarios()
            elif opcion == 0:
                self.view.mostrar_mensaje("Saliendo de la gestion de usuarios...")
                break
            else:
                self.view.mostrar_mensaje("Opcion no valida.")

    def agregar_usuario(self) -> None:
        datos = self.view.formulario_nv_usuario()
        try:
            hash_pass = self.ph.hash(datos['contrasena'])
            nuevo_usuario = Usuario(None, datos['login'], hash_pass)
            exito = UsuarioDao.crear(nuevo_usuario)

            if exito:
                self.view.mostrar_mensaje(f"Usuario agregado con exito (ID: {nuevo_usuario.id_usuario})")
            else:
                self.view.mostrar_mensaje("Error interno al guardar en la base de datos.")
        except ValueError as e:
            self.view.mostrar_mensaje(f"Error en los datos: {e}")

    def imprimir_usuarios(self) -> None:
        usuarios = UsuarioDao.obtener_datos()
        self.view.mostrar_lista_usuarios(usuarios)