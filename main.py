import sqlite3
import hashlib
import sys
from controllers.main_controller import MainController

def encriptar_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def iniciar_sesion():
    conexion = sqlite3.connect('ECOTECH.db')
    cursor = conexion.cursor()
    
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (usuario TEXT, contrasena TEXT)")
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", 
                       ('admin', encriptar_contrasena('admin123')))
        conexion.commit()

    print("\n" + "="*40)
    print("=== SISTEMA ECOTECH - INICIO DE SESIÓN ===")
    print("="*40)
    
    intentos = 0
    while intentos < 3:
        usuario = input("Ingrese su usuario: ").strip()
        contrasena = input("Ingrese su contraseña: ").strip()
    
        if not usuario or not contrasena:
            print("[ERROR] El usuario y contraseña no pueden estar vacíos.\n")
            continue
            
        contrasena_encriptada = encriptar_contrasena(contrasena)
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contrasena_encriptada))
        
        if cursor.fetchone():
            print(f"\n[ÉXITO] ¡Bienvenido al sistema, {usuario}!\n")
            conexion.close()
            return True
        else:
            print("[ERROR] Credenciales incorrectas. Intente nuevamente.\n")
            intentos += 1
            
    print("[SISTEMA] Demasiados intentos fallidos. Acceso denegado.")
    conexion.close()
    return False

if __name__ == "__main__":
    if iniciar_sesion():
        app = MainController()
        app.ejecutar()
    else:
        sys.exit()