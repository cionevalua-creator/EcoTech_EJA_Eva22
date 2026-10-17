from sqlite3 import Cursor
from config.database import Database
from models.registrotiempo import RegistroTiempo

class Registrotiempo_Dao:
    @staticmethod
    def crear(registrotiempo:RegistroTiempo) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO registrotiempo(fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto) VALUES(?, ?, ?, ?, ?)",
                (registrotiempo.fecha, registrotiempo.horas_trabajadas, registrotiempo.descripcion, registrotiempo.id_empleado, registrotiempo.id_proyecto)
            )
            conn.commit()
            registrotiempo.id_registrotiempo = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear el registrotiempo en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_datos() -> list[RegistroTiempo]:
        conn = Database().get_connection()
        registrostiempos = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_registrotiempo, fecha, horas_trabajadas, descripcion, id_empleado, id_proyecto FROM registrotiempo")
            filas = cursor.fetchall()
            for fila in filas:
                registrostiempos.append(RegistroTiempo(fila['fecha'], fila['horas_trabajadas'], fila['descripcion'], fila['id_empleado'], fila['id_proyecto']))
        except Exception as e:
            print(f"Error al obtener registrostiempos: {e}")
        finally:
            conn.close()
        return registrostiempos