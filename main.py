import Modulos.menu as index
import Modulos.menuEquipos as menuE
import Modulos.menuPlantel as menuP
import Modulos.menuPartidos as MenuPar
import Modulos.menuResul as menuRes

if (__name__ == "__main__"):
    equipos  = []
    fechas = []
    activeMenu = True
    while activeMenu:
        print(fechas)
        res =  index.crearMenu()
        print (res)
        if(res == 1):
            try:
               menuE.subMenuEquipo(equipos)
            except ValueError:
                print("Ha ocurrido un error intentelo despues")
                
        elif(res == 2):
            try:
                menuP.menuPlantel(equipos)
            except ValueError:
                print("ocurrio un error")
        if(res == 3 ):
            resul = MenuPar.menuPartidos(equipos)
            fechas.append(resul)
        elif(res == 4):
            menuRes.menuResul(fechas)
        elif(res == 5):
            activeMenu = False
            
      
        