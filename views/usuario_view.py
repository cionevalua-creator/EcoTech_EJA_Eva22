from views.utils import leer_numero
from models.usuario import Usuario

class UsuarioView:
    @staticmethod
    def mostrar_menu() -> int:
        print("\n" + "-" * 30)
        print("     GESTION DE USUARIOS")
        print("-" * 30)
        print("1.   AGREGAR USUARIO")
        print("2.   MOSTRAR TODOS LOS USUARIOS")
        print("0.   VOLVER AL (MENU PRINCIPAL)")
        print("-" * 30)
        return leer_numero("Seleccione una opcion: ")

    @staticmethod
    def formulario_nv_usuario() -> dict:
        print("\n--- AGREGAR NUEVO USUARIO ---")
        login = input("Ingrese el nombre de usuario (login): ")
        contrasena = input("Ingrese la contrasena: ")

        return {
            "login": login,
            "contrasena": contrasena
        }

    @staticmethod
    def mostrar_lista_usuarios(usuarios: list[Usuario]) -> None:
        print("\n--- LISTA DE USUARIOS ---")
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            for u in usuarios:
                print(f"ID Usuario: {u.id_usuario} | Login: {u.login} | Contraseña: {u.contraseña[:15]}...")
        print("-" * 30)

    @staticmethod
    def mostrar_mensaje(mensaje: str) -> None:
        print(f"[USUARIOS] {mensaje}")
