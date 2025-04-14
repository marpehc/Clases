import time


class Cajero:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.historial = []
        
        
        
    
    def Consultar_saldo(self, tiempo):
        
        print(f"{tiempo} \nSaldo actual:{self.saldo}")
    
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(self.saldo)
        else:
            print("El valor que introduces no puede ser negativo!")
            
    
    def retirar(self, cantidad):
        self.saldo += 100
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"\nDinero retirado: {cantidad}. Saldo restante: {self.saldo}")
            with open("Cuentas.txt", "a", encoding="utf-8") as file:
                fecha = time.strftime("%D-%M-%Y %H:%M:%S", time.localtime())
                file.write(f"Retirada de dinero. Cantidad: {cantidad} | Saldo restante: {self.saldo}. A día {fecha}\n")
        else:
            print("No tienes saldo suficiente para hacer el retiro.")
            
                
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
            fecha = time.strftime("%D-%M-%Y %H:%M:%S", time.localtime())
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
    menu()