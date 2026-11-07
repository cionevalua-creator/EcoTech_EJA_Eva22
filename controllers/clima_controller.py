from views.clima_view import ClimaView
from services.clima_service import ClimaService
from models.clima_dao import ClimaDAO

class ClimaController:
    def __init__(self):
        self.vista = ClimaView()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == 1:
                self.consultar_clima()
            elif opcion == 0:
                break
            else:
                print("Opción no válida.")

    def consultar_clima(self):
        ciudad = self.vista.pedir_ciudad()
        if ciudad:
            datos_clima = ClimaService.obtener_clima(ciudad)
            self.vista.mostrar_resultado(datos_clima)
            
            if "error" not in datos_clima:
                ClimaDAO.guardar_historial(
                    ciudad=ciudad,
                    temperatura=datos_clima["temperatura"],
                    humedad=datos_clima["humedad"], 
                    estado=datos_clima["estado"]
                )