from sqlite3 import Cursor
from config.database import Database
from models.usuario import Usuario

class Usuario_Dao:
    @staticmethod
    def crear(usuario:Usuario) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuario(login, contraseña) VALUES(?, ?)",
                (usuario.login, usuario.contraseña)
            )
            conn.commit()
            usuario.id_usuario = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear usuario en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_datos() -> list[Usuario]:
        conn = Database().get_connection()
        usuarios = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_usuario, login, contraseña FROM usuario")
            filas = cursor.fetchall()
            for fila in filas:
                usuarios.append(Usuario(fila['id_usuario'], fila['login'], fila['contraseña']))
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
        finally:
            conn.close()
        return usuarios