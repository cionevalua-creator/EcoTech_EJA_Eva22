from sqlite3 import Cursor
from config.database import Database
from models.departamento import Departamento

class DepartamentoDao:
    @staticmethod
    def crear(departamento: Departamento) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO departamento (nombre, gerente_asociado) VALUES (?, ?)",
                (departamento.nombre, departamento.gerente_asociado)
            )
            conn.commit()
            departamento.id_departamento = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear departamento en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_datos() -> list[Departamento]:
        conn = Database().get_connection()
        departamentos = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_departamento, nombre, gerente_asociado FROM departamento")
            filas = cursor.fetchall()
            for fila in filas:
                departamentos.append(Departamento(fila['nombre'], fila['gerente_asociado'], fila['id_departamento']))
        except Exception as e:
            print(f"Error al obtener departamentos: {e}")
        finally:
            conn.close()
        return departamentos