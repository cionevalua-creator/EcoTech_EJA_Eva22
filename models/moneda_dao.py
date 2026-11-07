import sqlite3

class MonedaDAO:
    @staticmethod
    def _conectar():
        conn = sqlite3.connect("ECOTECH.db")
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historial_moneda (
                id_moneda INTEGER PRIMARY KEY AUTOINCREMENT,
                moneda TEXT NOT NULL,
                valor TEXT NOT NULL,
                fecha_consulta DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        return conn

    @staticmethod
    def guardar_historial(moneda, valor):
        conn = MonedaDAO._conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO historial_moneda (moneda, valor)
            VALUES (?, ?)
        ''', (moneda, valor))
        conn.commit()
        conn.close()