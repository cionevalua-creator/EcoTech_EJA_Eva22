from datetime import date
from models.departamento import Departamento
from models.departamento_dao import DepartamentoDao
from models.empleado import Empleado
from models.empleado_dao import EmpleadoDao

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
