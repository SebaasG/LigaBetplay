import Modulos.menu as index
import Modulos.menuEquipos as menuE
import Modulos.menuPlantel as menuP

if (__name__ == "__main__"):
    equipos  = []
   
    activeMenu = True
    while activeMenu:
        
        res =  index.crearMenu()
       
        print (res)
        if(res == 1):
            try:
               menuE.subMenuEquipo(equipos)
            except:
                print("Ha ocurrido un error intentelo despues")
                
        elif(res == 2):
            try:
                menuP.menuPlantel(equipos)
            except ValueError:
                print("ocurrio un error")
        if(res == 3 ):
            pass
        elif(res == 4):
            pass
        elif(res == 5):
            activeMenu = False
            
      
        