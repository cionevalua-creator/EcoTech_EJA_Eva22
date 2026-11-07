from config.database import Database
import sqlite3

class ClimaDAO:
    @staticmethod
    def _conectar():
        conn = sqlite3.connect("ECOTECH.db")
        cursor = conn.cursor()  
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historial_clima (
                id_clima INTEGER PRIMARY KEY AUTOINCREMENT,
                ciudad TEXT NOT NULL,
                temperatura TEXT NOT NULL,
                humedad TEXT NOT NULL,
                estado TEXT NOT NULL,
                fecha DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')      
        
        try:
            cursor.execute("ALTER TABLE historial_clima ADD COLUMN humedad TEXT DEFAULT '0%'")
        except sqlite3.OperationalError:
            pass 
            
        conn.commit()
        return conn

    @staticmethod
    def guardar_historial(ciudad, temperatura, humedad, estado):
        conn = ClimaDAO._conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO historial_clima (ciudad, temperatura, humedad, estado)
            VALUES (?, ?, ?, ?)
        ''', (ciudad, temperatura, humedad, estado))
        conn.commit()
        conn.close()