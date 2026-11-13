import sqlite3
import sys
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from controllers.main_controller import MainController

ph = PasswordHasher()

def encriptar_contrasena(contrasena):
    return ph.hash(contrasena)

def iniciar_sesion():
    conexion = sqlite3.connect("ECOTECH.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", 
                       ('admin', encriptar_contrasena('admin123')))
        conexion.commit()

    print("\n--- INICIO DE SESIÓN SEGURO (ECOTECH) ---")
    intentos = 0
    while intentos < 3:
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()

        if not usuario or not contrasena:
            print("[ERROR] Las credenciales no pueden estar vacías.\n")
            intentos += 1
            continue

        cursor.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

        if resultado:
            try:
                ph.verify(resultado[0], contrasena)
                print("\nBienvenido, Administrador.\n")
                conexion.close()
                return True
            except VerifyMismatchError:
                pass

        intentos += 1
        print(f"[ERROR] Usuario o contraseña incorrectos. Intentos restantes: {3 - intentos}\n")

    print("[SISTEMA] Máximo de intentos alcanzado. Cerrando programa...")
    conexion.close()
    return False

if __name__ == "__main__":
    if iniciar_sesion():
        app = MainController()
        app.ejecutar()
    else:
        sys.exit()