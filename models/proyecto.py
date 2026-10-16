from datetime import date 

class Proyecto:
    def __init__(self, id_proyecto:int, nombre:str, descripcion:str, fecha_inicio:date, id_departamento:int):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.id_departamento = id_departamento


    @property
    def id_proyecto(self) -> int:
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, id_proyecto:int) -> None:
        if id_proyecto <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._id_proyecto = id_proyecto

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str) -> None:
        if not nombre.strip():
            raise ValueError("El campo no puede quedar vacio.")
        self._nombre = nombre.strip()

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion:str) -> None:
        if not descripcion.strip():
            raise ValueError("El campo no puede quedar vacio.")
        self._descripcion = descripcion.strip()

    @property
    def fecha_inicio(self) -> date:
        return self._fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio:date) -> None:
        if fecha_inicio > date.today():
            raise ValueError("La fecha de inicio no puede ser mayor a la fecha actual.")
        self._fecha_inicio = fecha_inicio

    @property
    def id_departamento(self) -> int:
        return self._id_departamento

    @id_departamento.setter
    def id_departamento(self, id_departamento:int) -> None:
        if id_departamento is not None and id_departamento <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._id_departamento = id_departamento