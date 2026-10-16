from sqlite3 import Cursor
from config.database import Database
from models.empleado import Empleado

class EmpleadoDao:
    @staticmethod
    def crear(empleado:Empleado) -> bool:
        conn = Database().get_connection()
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO empleado (nombre, correo, fecha_inicio, direccion, telefono, salario, id_departamento, id_proyecto, id_usuario) VALUES (?,?,?,?,?,?,?,?,?)" ,
                (empleado.nombre, empleado.correo, empleado.fecha_inicio, empleado.direccion, empleado.telefono, empleado.salario, empleado.id_departamento, empleado.id_proyecto, empleado.id_usuario)
            )
            conn.commit()
            empleado.id_empleado = cursor.lastrowid
            return True
        except Exception as e:
            print(f"Error al crear un empleado en BD: {e}")
            return False
        finally:
            conn.close()

    @staticmethod
    def obtener_datos() -> list[Empleado]:
        conn = Database().get_connection()
        empleados = []
        try:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT id_empleado, nombre, correo, fecha_inicio, direccion, telefono, salario, id_departamento, id_proyecrto, id_usuario FROM empleado")
            filas = cursor.fetchall()
            for fila in filas:
                empleados.append(Empleado(fila['nombre'], fila['correo'], fila['fecha_inicio'], fila['direccion'], fila['telefono'], fila['salario'], fila['id_departamento'], fila['id_proyecto'], fila['id_usuario']))
        except Exception as e:
            print(f"Error al obtener empleados: {e}")
        finally:
            conn.close()
        return empleados