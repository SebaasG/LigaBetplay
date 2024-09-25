

import Modulos.utils as ui
def menuPartidos(equipos:list):
    try:
        isValid= True
        
        while isValid:
            ui.limpiarConsola()
            print("1. Programar partido \n2. Ver partidos \n3. Salir")
            opc = int(input(": "))
            if(opc == 1):
                ui.limpiarConsola()
                print("entra quoi")
                programar(equipos)
            elif(opc ==2):
                ui.limpiarConsola()
                pass
            elif(opc ==3 ):
                isValid = False
                ui.limpiarConsola()
            else:
                print("Dato no valido intente con otro")
                input("presione cualquier tecla...")
                ui.limpiarConsola()
    except ValueError:
        print("Error en el sistema")
        
        
def programar (equipos:list):
    print(f"Estos son los equipos sdisponibles: {equipos}")
    