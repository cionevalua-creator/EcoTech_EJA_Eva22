class Usuario:
    def __init__(self, id_usuario:int, login:str, contraseña:str):
        self.id_usuario = id_usuario
        self.login = login
        self.contraseña = contraseña

    @property
    def id_usuario(self) -> int:
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario:int) -> None:
        if id_usuario is not None and id_usuario <= 0:
            raise ValueError("El id debe ser mayor a 0.")
        self._id_usuario = id_usuario

    @property 
    def login(self) -> str:
        return self._login 

    @login.setter
    def login(self, login:str) -> None:
        if not login.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._login = login.strip()

    @property
    def contraseña(self) -> str:
        return self._contraseña

    @contraseña.setter
    def contraseña(self, contraseña:str) -> None:
        if not contraseña.strip():
            raise ValueError("El campo no puede estar vacio.")
        self._contraseña = contraseña.strip()
    