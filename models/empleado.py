from datetime import date
class Empleado:
    def __init__(self, id:int, nombre:str, correo:str, fecha_inicio:date, direccion:str, telefono:str, salario:float):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.fecha_inicio = fecha_inicio
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario

    @property
    def id(self) -> int:
        return self._id 

    @id.setter
    def id(self, id:int) -> None:
        if id <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._id = id 

    @property 
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str) -> None:
        if not nombre.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._nombre = nombre.strip()

    @property 
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, correo:str) -> None:
        if not correo.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._correo = correo.strip()

    @property 
    def fecha_inicio(self) -> date:
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio:date) -> None:
        if fecha_inicio > date.today():
            raise ValueError("La fecha de inicio no puede ser mayor a la fecha actual.")
        self._fecha_inicio = fecha_inicio

    @property
    def direccion(self) -> str:
        return self._direccion

    @direccion.setter
    def direccion(self, direccion:str) -> None:
        if not direccion.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._direccion = direccion.strip()

    @property 
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, telefono:str) -> None:
        if not telefono.strip():
            raise ValueError("El campo no puede estar vacio.")
        if not telefono.strip().replace("+", "").isdigit():
            raise ValueError("El numero solo puede contener numeros y es opcional el (+)")
        if len(telefono.strip()) < 9:
            raise ValueError("El numero debe tener al menos 9 caracteres.")
        self._telefono = telefono.strip()

    @property
    def salario(self) -> float:
        return self._salario

    @salario.setter
    def salario(self, salario:float) -> None:
        if salario < 1 or salario > 999999999.99:
            raise ValueError("El salario debe estar entre 1 y 999.999.999.99")
        self._salario = salario