import time
import platform
import os
from tarjetas import tarjetas_disponibles, añadir_tarjeta, eliminar_tarjeta
INTENTOS_MAXIMOS = 3

def clear_console():
  """Clears the console screen, compatible with Windows, Linux, and macOS."""
  system_name = platform.system()
  if system_name == "Windows":
    os.system('cls')
  else: # Assuming Linux or macOS
    os.system('clear')






def verificar_pin(tarjeta):
    intentos, penalizacion = 0, 0
    
    while intentos < INTENTOS_MAXIMOS:
        try:
            res_pin = int(input("Introduce el PIN: "))
            if res_pin == int(tarjeta.pin):
                print("PIN correcto. ¡Bienvenido!")
                return True
            else:
                intentos += 1
                penalizacion += 10
                print(f"PIN incorrecto. Intentos restantes: {INTENTOS_MAXIMOS - intentos}")
                
                
                for i in range(penalizacion):
                    print(f"Tiempo restante: {(penalizacion)- i} segundos")
                    time.sleep(1) #CUIDADO QUE ANTES HABÍA PUESTO time.sleep(i) y eso estaria mal.
                    
                
                    
                for _ in range(3):
                    print(".", end="", flush=True)
                    time.sleep(1)
                    
                clear_console()
        except ValueError:
            print("Introduce un número válido.")
    print("Demasiados intentos. Acceso denegado.")
    print("vuelve a intentarlo dentro de 10 minutos...")
    time.sleep(600)
    return False


    
    
    
    


class Cajero:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.historial = []

        # Cargar historial desde Cuentas.txt si existe
        try:
            with open("Cuentas.txt", "r", encoding="utf-8") as file:
                for linea in file:
                    self.historial.append(linea.strip())
        except FileNotFoundError:
            with open("Cuentas.txt", "w", encoding="utf-8") as file:
                pass
    
    def clear_console():
        """Clears the console screen, compatible with Windows, Linux, and macOS."""
        system_name = platform.system()
        if system_name == "Windows":
            os.system('cls')
        else: # Assuming Linux or macOS
            os.system('clear')
 
    
    
    def Consultar_saldo(self, tiempo):
        print(f"\n{tiempo} \nSaldo actual: {self.saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            fecha = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
            self.historial.append(f"Depósito: {cantidad} | Saldo: {self.saldo} | Fecha: {fecha}")
            print(f"Depósito exitoso. Saldo actual: {self.saldo}")
            
            with open("Cuentas.txt", "a", encoding="utf-8") as file:
                file.write(f"Depósito de dinero. Cantidad: {cantidad} | Saldo actual: {self.saldo}. A día {fecha}\n")
        else:
            print("El valor que introduces no puede ser negativo.")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            fecha = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
            self.historial.append(f"Retiro: {cantidad} | Saldo: {self.saldo} | Fecha: {fecha}")
            print(f"\nDinero retirado: {cantidad}. Saldo restante: {self.saldo}")
            with open("Cuentas.txt", "a", encoding="utf-8") as file:
                file.write(f"Retirada de dinero. Cantidad: {cantidad} | Saldo restante: {self.saldo}. A día {fecha}\n")
        else:
            print("No tienes saldo suficiente para hacer el retiro.")

    def mostrar_historial(self):
        if not self.historial:
            print("No hay transacciones en el historial.")
        else:
            print("\n--- Historial de transacciones ---")
            for transaccion in self.historial:
                print(transaccion)


def menu(cajero, tarjeta): 
    

    while True:
        print("\n--- Cajero automático ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial de transacciones")
        print("5. Cambiar tarjeta")
        print("6. Añadir tarjeta")
        print("7. Eliminar tarjeta")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            fecha = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
            cajero.Consultar_saldo(fecha)
        
        elif opcion == "2":
            try:
                monto = float(input("Ingrese el monto a depositar: "))
                cajero.depositar(monto)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
        elif opcion == "3":
            try:
                monto = float(input("Ingrese el monto a retirar: "))
                cajero.retirar(monto)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
        elif opcion == "4":
            cajero.mostrar_historial()
        
        elif opcion == "5":
            nueva_tarjeta = cambiar_tarjeta()
            if nueva_tarjeta:
                tarjeta = nueva_tarjeta
                cajero = Cajero(tarjeta.saldo)
        
        elif opcion == "6":
            #AÑADE LA NUEVA TARJETA A TARJETAS_DISPONIBLES. Agrega la acción a Cuentas.txt
            
            nueva_tarjeta = añadir_tarjeta()
            fecha = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
            if nueva_tarjeta and verificar_pin(nueva_tarjeta):
                
                with open("Cuentas.txt", "a", encoding="utf-8") as file:
                    file.write(f"Tarjeta {tarjeta.numero} añadida correctamente. | Fecha: {fecha}\n") 
                
            cajero.historial.append(f"Tarjeta {tarjeta.numero} Añadida correctamente. | Fecha: {fecha}")
            
            tarjeta = nueva_tarjeta
            cajero = Cajero(tarjeta.saldo)
             
        elif opcion == "7":
            
            #ELIMINA LA TARJETA Y ESCRIBE LA ACCIÓN EN CUENTAS.TXT
            tarjeta_eliminar = eliminar_tarjeta()
            fecha = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
            with open("Cuentas.txt", "a", encoding="utf-8") as file:
               file.write(f"Tarjeta {tarjeta_eliminar.numero} eliminada correctamente. | Fecha: {fecha}\n") 
            
            cajero.historial.append(f"Tarjeta {tarjeta_eliminar.numero} eliminada correctamente. | Fecha: {fecha}")
            
               
            
            if tarjeta_eliminar:
                tarjeta = tarjeta_eliminar
                cajero = Cajero(tarjeta.saldo) 
                     
        elif opcion == "8":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            tarjeta.saldo = cajero.saldo
            break


        else:
            print("Opción no válida. Intenta de nuevo.")

def seleccionar_tarjeta():
    while True:
        try:
            numero = input("Introduce el número de la tarjeta: ")
            cvv = input("Introduce el CVV: ")
            for tarjeta in tarjetas_disponibles:
                if tarjeta.numero == numero and tarjeta.cvv == cvv and tarjeta.pin:
                    print("✅Tarjeta seleccionada. Accediendo al cajero...")
                    return tarjeta
            print("❌ Tarjeta no encontrada o datos incorrectos.")
            return None
            
        except ValueError:
            print("Introduce un número válido.")


def cambiar_tarjeta():
    tarjeta_actual = seleccionar_tarjeta()





if __name__ == "__main__":
    tarjeta_actual = seleccionar_tarjeta()
    if tarjeta_actual and verificar_pin(tarjeta_actual):
        cajero = Cajero(tarjeta_actual.saldo)
        menu(cajero, tarjeta_actual)



#1234-5678-9123-4567 COPIAR