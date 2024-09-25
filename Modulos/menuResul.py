import Modulos.utils as ut

tabla = []
def menuResul(fechas:list):
    try:
        isValid = True
        while isValid:
            print("1. Registrar resultados\n2. Ver Registrar\n3.Salir")
            opc = str(input(": "))
            if(opc ==1):
                regiResul(fechas)
            elif(opc == 2):
                pass
            elif(opc ==3):
                isValid = False
            else:
                print("Escogió un valor invalido")
                input("Presione cualquier tecla para continuar...")
                ut.limpiarConsola()
    except ValueError:
        print("Error en el sistema")
    
    
def regiResul(fechas):
    print(fechas)
    print("A que encuentro le quiere registrar el resultado: ")
    