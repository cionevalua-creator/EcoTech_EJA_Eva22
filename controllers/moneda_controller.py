from views.moneda_view import MonedaView
from services.moneda_service import MonedaService
from models.moneda_dao import MonedaDAO

class MonedaController:
    def __init__(self):
        self.vista = MonedaView()

    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            if opcion == 1:
                self.consultar_moneda()
            elif opcion == 0:
                break
            else:
                print("Opción no válida.")

    def consultar_moneda(self):
        moneda = self.vista.pedir_moneda()
        if moneda:
            datos = MonedaService.obtener_indicador(moneda)
            self.vista.mostrar_resultado(datos)
            
            if "error" not in datos:
                MonedaDAO.guardar_historial(
                    moneda=datos["moneda"],
                    valor=datos["valor"]
                )