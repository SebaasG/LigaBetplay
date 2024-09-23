
import os
def subMenuEquipo(equipos:list):
    try:
        limpiarConsola()
        isValid =True
        while isValid:
            
            print("1. Registrar equipo \n2. Ver Equipos \n3. Volver ")
            opc = int(input(": "))
            if (opc == 1):
                regEquipo(equipos)
                print("se ha registrado correctamente su equipo")
            elif (opc == 2):
                 limpiarConsola()
                 if(equipos == []):
                     print("Aun no se han registrado equipos")
                     input('Presione cualquier tecla para continuar...')
                     limpiarConsola()
                 else:
                    print(f"Los siguientes son los equipos registrados:\n {equipos[0][0]}")
                    input('Presione cualquier tecla para continuar...')
                    limpiarConsola()

            elif (opc == 3):
                isValid = False  
                limpiarConsola()
            else:
                print("Opción no válida, intente nuevamente.")
            
    except ValueError:
        print("Hubo un error en el proceso, intente nuevamente.")

def regEquipo(eq:list):
    equipo = pedirDatos()
    eq.append(equipo)
    print("Su equipo es: ", equipo)

def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")
    
def pedirDatos ():
    
    name = str(input("Ingrese el nombre de su equipo: ")).lower()
    pj = int(input(f"ingrese la cantidad de partidos jugados para {name}: "))
    pg = int(input(f"ingrese la cantidad de partidos ganados para {name}: "))
    pp = int(input(f"ingrese la cantidad de partidos perdidos para {name}: "))
    pe = int(input(f"ingrese la cantidad de partidos empatados para {name}: "))
    gf = int(input(f"ingrese la cantidad goles a favor para {name}: "))
    gc = int(input(f"ingrese la cantidad goles en contra para {name}: "))
    datos = [name, pj, pg,pp,pe,gf,gc]
    return datos