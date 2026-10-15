from datetime import date

class RegistroTiempo:
    def __init__(self, fecha:date, horas_trabajadas:int, descripcion:str):
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion = descripcion

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
    