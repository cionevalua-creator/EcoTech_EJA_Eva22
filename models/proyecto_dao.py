from sqlite3 import Cursor
from config.database import Database
from models.proyecto import Proyecto
from datetime import date

class Proyecto_Dao:
    @staticmethod
    def crear(proyecto:Proyecto) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO proyecto (nombre, descripcion, fecha_inicio, id_departamento) VALUES(?, ?, ?, ?)",
                (proyecto.nombre, proyecto.descripcion, proyecto.fecha_inicio, proyecto.id_departamento)
            )
            conn.commit()
            proyecto.id_proyecto = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear proyecro en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_datos() -> list[Proyecto]:
        conn = Database().get_connection()
        proyectos = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_proyecto, nombre, descripcion, fecha_inicio, id_departamento FROM proyecto")
            filas = cursor.fetchall()
            for fila in filas:
                fecha_real = date.fromisoformat(fila['fecha_inicio'])
                proyectos.append(Proyecto(fila['id_proyecto'], fila['nombre'], fila['descripcion'], fecha_real, fila['id_departamento']))
        except Exception as e:
            print(f"Error al obtener proyectos: {e}")
        finally:
            conn.close()
        return proyectos
