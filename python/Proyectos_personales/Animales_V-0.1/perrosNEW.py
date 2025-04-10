import os 
import time

#####Residencia crear diccionario

residencias = {}


def crear_residencia():
    ag_residencia = input("¿Cómo se llama la residencia en la que esta el perro que quieres agregar? (en el caso de no haber se creará una automáticamente): ").strip().lower()
    perro = input("Ingrese el nombre del perro: ")
    
    
    if ag_residencia in residencias:
        residencias[ag_residencia].append(perro)
        print("¡Perro agregado!")
        Main()
        
    else:
        residencias[ag_residencia] = perro ### Se agrega una residencia + el perro. 
        print("Residencia y perro agregados!")
        print('\nVolviendo al Menú de opciones...')

        time.sleep(3)
        os.system('cls')
        Main()



def Main():
    while True:
        
        print("Menú:")
        print("1 - Agregar un perro al diccionario (o crear una residencia en el caso de que no exista esta).")
        print("2 - Ver los perros de cada residencia.")
        print("3 - Agregar un perro a la lista")
        print("4 - Ver la cantidad de perros que hay en total (Resultado en número)")
        print("5 - Borrar un perro de la lista")
        print("6 - Salir")
        try:
            iniciorespuesta = int(input("Qué desea hacer?: ").strip())
            if iniciorespuesta == 1:
                crear_residencia() 
        
            elif iniciorespuesta == 2:
                for res, perros in residencias:
                    print(f"{res}: {', '.join(perros)}")                
                
                
            elif iniciorespuesta == 3:
                BorrarPerroLista()
                
                
            elif iniciorespuesta == 4:
                print("Saliendo del programa... ")
                quit()
                break
                
            
        except TypeError or ValueError or AttributeError:
            print("Ingresa una respuesta válida. ")
            print("borrando consola... ")
            time.sleep(3)
            
            os.system('cls')
Main()