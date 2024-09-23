import os
import Modulos.menuEquipos as me

def menuPlantel(equipos:list):
    try:
        me.limpiarConsola()
        print("este es el menu del plantel ")
        isValid = True

        while isValid:
            print("1. Registrar Jugadores \n2. Ver jugadores \n3. Registrar entrenador\n4.Ver entrenadores\n5. Volver ")
            opc = int(input(": "))

            if(opc == 1):
                validaEquipoDispo(equipos)
            elif(opc ==2):
                pass
            elif(opc == 3):
                pass
            elif(opc == 4):
                pass
            elif(opc == 5):
                isValid = False
            else:
                print("Opción no válida, intente nuevamente.")
    except ValueError:
        print("Error en la ejecucion del programa")


def registrarJugador ():
    listaJugadores = []
    nom = str(input("Ingrese el nombre del jugador: "))
    dorsal = int(input("Ingrese el dorsal del jugador: "))
    pos = str(input("Ingrese la posición del jugador: "))
    listaJugadores= [nom,dorsal,pos]
    print(f"El jugador registrado es el siguiente {listaJugadores}")


def validaEquipoDispo(equipos:list):
    equiposDispo = []
    for i in range(0, len(equipos)):
        equiposDispo.append(equipos[i][0])
    nomEquipo = str(input(f"Ingrese el nombre del equipo, los disponibles son los siguientes:{equiposDispo}"))
    if (nomEquipo in equiposDispo):
        print("si esta")
        registrarJugador()
    return nomEquipo

    


