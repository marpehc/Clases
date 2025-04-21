import os
import platform
import time 



def clear_console():
  """Clears the console screen, compatible with Windows, Linux, and macOS."""
  system_name = platform.system()
  if system_name == "Windows":
    os.system('cls')
  else: # Assuming Linux or macOS
    os.system('clear')


class Tarjeta:
    
    
    
    def __init__(self, numero, fecha_expiracion, cvv, pin, saldo=0):
        self.numero = numero
        self.fecha_expiracion = fecha_expiracion
        self.cvv = cvv
        self.pin = pin
        self.saldo = saldo
      
tarjetas_disponibles = [
    Tarjeta("1234-5678-9123-4567", "12/25", "123", "7123", saldo=1000)]


def añadir_tarjeta():
    numero = input("Introduce el número de la tarjeta a añadir: ")
    for tarjeta in tarjetas_disponibles:
        if tarjeta.numero == numero:    
            print('Tarjeta existente...')
            time.sleep(1.5)
            clear_console()
            exit(1)
    fecha_expiracion = input("Introduce la fecha de expiración de la tarjeta a añadir: ")
    cvv = input("Introduce el CVV de la tarjeta a añadir: ")
    pin = input("Introduce el PIN de la tarjeta a añadir: ")
    
    clear_console()
    saldo = float(input("Introduce el saldo actual de la tarjeta: "))
    tarjeta_nueva = Tarjeta(numero, fecha_expiracion, cvv, pin, saldo)
    tarjetas_disponibles.append(tarjeta_nueva)
    print("Tarjeta añadida correctamente.")
    return tarjeta_nueva
    
    
def eliminar_tarjeta():
    numero = input("Introduce el número de la tarjeta a borrar: ")
    for tarjeta_eliminar in tarjetas_disponibles:
        tarjetas_disponibles.remove(tarjeta_eliminar)
        
        print("Tarjeta eliminada correctamente.")
        return tarjeta_eliminar

    print("La tarjeta no se encuentra en la lista.")
    return None 
        
