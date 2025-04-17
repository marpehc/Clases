import time
import platform
import os
PIN_CORRECTO = 7123
INTENTOS_MAXIMOS = 3

def clear_console():
  """Clears the console screen, compatible with Windows, Linux, and macOS."""
  system_name = platform.system()
  if system_name == "Windows":
    os.system('cls')
  else: # Assuming Linux or macOS
    os.system('clear')


def verificar_pin():
    intentos, penalizacion = 0, 0
    
    while intentos < INTENTOS_MAXIMOS:
        try:
            res_pin = int(input("Introduce el PIN: "))
            if res_pin == PIN_CORRECTO:
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
    
    return False


class Cajero:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.historial = []

        # Cargar historial desde Cuentas.txt si existe
        try:
            with open("Cuentas.txt", "r", encoding="utf-8") as file:
                for linea in file:
                    self.historial.append(linea.strip())
        except FileNotFoundError:
            # Si el archivo no existe, continuar con historial vacío
            pass

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


def menu():
    cajero = Cajero()

    while True:
        print("\n--- Cajero automático ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial de transacciones")
        print("5. Salir")

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
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    if verificar_pin():
        menu()
