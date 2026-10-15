import sqlite3
from sqlite3 import Connection, Cursor

class Database:
    _instance = None
    _ecotech_db = "ECOTECH.db"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_connection(self) -> Connection:
        conn = sqlite3.connect(self._ecotech_db)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self) -> None:
        conn = self.get_connection()
        try:
            cursor:Cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuario (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL,
                    contraseña TEXT NOT NULL
                    )
                """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departamento(
                    id_departamento INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    gerente_asociado TEXT NOT NULL
                    )
                """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyecto(
                    id_proyecto INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    descripcion TEXT NOT NULL,
                    fecha_inicio TEXT NOT NULL,
                    id_departamento INTEGER,
                    FOREIGN KEY(id_departamento) 
                        REFERENCES departamento(id_departamento) ON DELETE SET NULL
                        )
                """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleado(
                    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    correo TEXT NOT NULL,
                    fecha_inicio TEXT NOT NULL,
                    direccion TEXT NOT NULL,
                    telefono TEXT NOT NULL,
                    salario REAL NOT NULL,
                    id_departamento INTEGER,
                    id_proyecto INTEGER,
                    id_usuario INTEGER,
                    FOREIGN KEY(id_departamento)
                        REFERENCES departamento(id_departamento) ON DELETE SET NULL,
                    FOREIGN KEY(id_proyecto)
                        REFERENCES proyecto(id_proyecto) ON DELETE SET NULL,
                    FOREIGN KEY(id_usuario) 
                        REFERENCES usuario(id_usuario) ON DELETE SET NULL
                        )
                """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS registrotiempo(
                    id_registro INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    horas_trabajadas INTEGER NOT NULL,
                    descripcion TEXT NOT NULL,
                    id_empleado INTEGER,
                    id_proyecto INTEGER,
                    FOREIGN KEY (id_empleado)
                        REFERENCES empleado(id_empleado) ON DELETE SET NULL,
                    FOREIGN KEY (id_proyecto)
                        REFERENCES proyecto(id_proyecto) ON DELETE SET NULL
                        )
                """)           

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    db = Database()
    db.init_db()
    print("Base de datos inicializada correctamente.")