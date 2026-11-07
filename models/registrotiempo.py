from datetime import date

class RegistroTiempo:
    def __init__(self, id_registrotiempo:int, fecha:date, horas_trabajadas:int, descripcion:str, id_empleado:int, id_proyecto:int):
        self.id_registrotiempo = id_registrotiempo
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

    @property
    def id_registrotiempo(self) -> int:
        return self._id_registrotiempo

    @id_registrotiempo.setter
    def id_registrotiempo(self, id_registrotiempo:int) -> None:
        if id_registrotiempo is not None and id_registrotiempo <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._id_registrotiempo = id_registrotiempo

    @property
    def fecha(self) -> date:
        return self._fecha

    @fecha.setter
    def fecha(self, fecha:date) -> None:
        if fecha > date.today():
            raise ValueError("La fecha no puede ser mayor que la fecha actual.")
        self._fecha = fecha

    @property
    def horas_trabajadas(self) -> int:
        return self._horas_trabajadas

    @horas_trabajadas.setter
    def horas_trabajadas(self, horas_trabajadas:int) -> None:
        if horas_trabajadas <= 0:
            raise ValueError("Las horas trabajadas deben ser mayores a 0.")
        self._horas_trabajadas = horas_trabajadas 

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion:str) -> None:
        if not descripcion.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._descripcion = descripcion.strip()

    @property
    def id_empleado(self) -> int:
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, id_empleado:int) -> None:
        if id_empleado <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._id_empleado = id_empleado

    @property
    def id_proyecto(self) -> int:
        return self._id_proyecto

    @id_proyecto.setter
    def id_proyecto(self, id_proyecto:int) -> None:
        if id_proyecto <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._id_proyecto = id_proyecto

