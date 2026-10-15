class Usuario:
    def __init__(self, login:str, contraseña:str):
        self.login = login
        self.contraseña = contraseña

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
    