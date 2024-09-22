def regEquipo(eq:list):
    equipo = eq
    print("Su equipo es: ", equipo)
    
def pedirDatos ():
    name = str(input("Ingrese el nombre de su equipo: "))
    pj = int(input(f"ingrese la cantidad de partidos jugados para {name}: "))
    pg = int(input(f"ingrese la cantidad de partidos ganados para {name}: "))
    pp = int(input(f"ingrese la cantidad de partidos perdidos para {name}: "))
    pe = int(input(f"ingrese la cantidad de partidos empatados para {name}: "))
    gf = int(input(f"ingrese la cantidad goles a favor para {name}: "))
    gc = int(input(f"ingrese la cantidad goles en contra para {name}: "))
    datos = [name, pj, pg,pp,pe,gf,gc]
    return datos