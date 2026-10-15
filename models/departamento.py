class Departamento:
    def __init__(self, id:int, nombre:str, gerente_asociado:str):
        self.id = id
        self.nombre = nombre
        self.gerente_asociado = gerente_asociado

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
    def gerente_asociado(self) -> str:
        return self._gerente_asociado

    @gerente_asociado.setter
    def gerente_asociado(self, gerente_asociado:str) -> None:
        if not gerente_asociado.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._gerente_asociado = gerente_asociado.strip()
        