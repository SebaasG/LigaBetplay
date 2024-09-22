import Modulos.menu as menuP
import Modulos.menuEquipos as menuE

if (__name__ == "__main__"):
    
    activeMenu = True
    while activeMenu:
        res =  menuP.crearMenu()
        print (res)
        if(res == 1):
            try:
                result = menuE.pedirDatos()
                menuE.regEquipo(result)
                print("se ha registrado correctamente su equipo")
            except:
                print("Ha ocurrido un error intentelo despues")
                
        elif(res == 2):
            pass
        if(res == 3 ):
            pass
        elif(res == 4):
            pass
        elif(res == 5):
            activeMenu = False
            
      
        