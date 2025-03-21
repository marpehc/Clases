import os
import time

Lista_Perros = []
Lista_Años_Perro = []

def LimpiarConsola():
    os.system('cls')


    
def agregarlista():
    while True:
        Perro = input(("Escribe el nombre del perro que quieras agregar: "))
        Edad = input("Escribe los años del perro: ")
        Lista_Perros.append(Perro)
        Lista_Años_Perro.append(Edad)
#Imprime lista_perros en bruto y lo separa con "" y ,
        print("\nLista de perros y sus edades: ")
        for i in range(len(Lista_Años_Perro)):
                print(f"{Lista_Perros[i]} - {Lista_Años_Perro[i]} años")
        inicio()
    




def MostrarCantidadLista():
    Lista_Perros.sort()
    print(f"cantidad de perros totales: ",len(Lista_Perros))


def BorrarPerroLista():
    PerroBorrar = input("¿Qué perro deseas borrar (escribelo correctamente)?: ")
    #idea sencilla para borrar 
    Lista_Perros.remove(PerroBorrar)
    print("perro borrado correctamente")
    print("Volviendo al menú...")
    #tiempo de retardo 2 secs...
    time.sleep(2)





#empieza el inicio.
#saluda y pide ordenes.
def inicio():
    while True:
        
        print("Menú:")
        print("1 - Agregar un perro a la lista")
        print("2 - Ver la cantidad de perros en la lista")
        print("3 - Borrar un perro de la lista")
        print("4 - Salir")
        try:
            iniciorespuesta = int(input("Qué desea hacer?: ").strip())
            if iniciorespuesta == 1:
                agregarlista()
        
            elif iniciorespuesta == 2:
                MostrarCantidadLista()
            
            
            
            elif iniciorespuesta == 3:
                BorrarPerroLista()
            
            
            elif iniciorespuesta == 4:
                print("Saliendo del programa... ")
                quit()
                break
            
        
        except ValueError:
            print("Ingresa una respuesta válida. ")
            print("borrando consola... ")
            time.sleep(3)
            
            os.system('cls')
            
        
        



inicio()

