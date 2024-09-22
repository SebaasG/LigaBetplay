import os

def crearMenu():
    options = [1,2,3,4,5]
    valid = True
    while valid:
        try:
            print("*****************************************************")
            print("****               LIGA BETPLAY                  ****")
            print("*****************************************************")
            menu = (
                "1. Registro equipos torneo \n"
                "2. Registro plantel \n"
                "3. Programar partidos \n"
                "4. Registrar resultado fecha \n"
                "5. Salir \n"
            )
            print(menu)
            resul = int(input(":"))
            if not(resul in options):
                print("Su opción no es válida escoja otra")
                os.system("pause")
                os.system("cls")
                return crearMenu()

        except ValueError as e:
            print(f"El dato no es valido xd {e}")

            os.system("pause")
            os.system("cls")
            crearMenu()

        else:
            valid == False
            return resul
        
        
        
        
        
        
        
       

 

