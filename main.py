from datetime import date
from models.departamento import Departamento
from models.departamento_dao import DepartamentoDao
from models.empleado import Empleado
from models.empleado_dao import EmpleadoDao
from models.proyecto import Proyecto
from models.proyecto_dao import Proyecto_Dao
from models.registrotiempo import RegistroTiempo
from models.registrotiempo_dao import Registrotiempo_Dao
from models.usuario import Usuario
from models.usuario_dao import Usuario_Dao
from controllers.main_controller import MainController

if __name__ == "__main__":
    app = MainController()
    app.ejecutar()

nuevo_departamento = Departamento(None, 'Finasas', 'Jose')

resultado = DepartamentoDao.crear(nuevo_departamento)
if resultado:
    print(f"El departamento se creo con exito: {nuevo_departamento.id_departamento}")
else: 
    print("A ocurrido un error no se pudo crear el departamento.")

nuevo_empleado = Empleado(None, 'Jose', 'joseco@gmail.com', date(2026, 10, 16), 'Madrid 133', '+56912213443', 500000.00, 12, 1, 1)

resultado = EmpleadoDao.crear(nuevo_empleado)
if resultado:
    print(f"El empleado se creo con exito: {nuevo_empleado.id_empleado}")
else:
    print("A ocurrido un error no se pudo crear el empleado.")

nuevo_proyecto = Proyecto(None, 'Proteccion de amenazas a la infancia', 'Proyecto dedicado a proteger a los menores de las amenzas digitales', date(2026, 10, 16), 1)

resultado = Proyecto_Dao.crear(nuevo_proyecto)
if resultado:
    print(f"El proyecto se creo con exito {nuevo_proyecto.id_proyecto}")
else:
    print("A ocurrido un error no se a podido crear el proyecto.")

nuevo_registrotiempo = RegistroTiempo(None, date(2026, 10, 17), 6, 'Hoy tabaje solo 6 porque es viernes y se trabaja medio dia', 1, 1)

resultado = Registrotiempo_Dao.crear(nuevo_registrotiempo)
if resultado:
    print(f"El registrotiempo se creo con exito: {nuevo_registrotiempo.id_registrotiempo}")
else:
    print("A ocurrido un error no se a podido crear el registrotiempo.")

nuevo_usuario = Usuario(None, 'gta_6', 'gta6.')

resultado = Usuario_Dao.crear(nuevo_usuario)
if resultado:
    print(f"El usuario se creo con exito {nuevo_usuario.id_usuario}")
else:
    print("A ocurrido un error no se a podido crear el usuario.")