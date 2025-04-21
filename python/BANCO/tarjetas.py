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
    
    def to_string(self):
        """Convierte la tarjeta a un string para guardarla en archivo de texto"""
        return f"{self.numero}|{self.fecha_expiracion}|{self.cvv}|{self.pin}|{self.saldo}"

# Función para cargar tarjetas desde el archivo
def cargar_tarjetas():
    try:
        tarjetas = []
        with open("Tarjetas.txt", "r", encoding="utf-8") as file:
            for linea in file:
                linea = linea.strip()
                if linea:
                    datos = linea.split("|")
                    if len(datos) == 5:
                        tarjetas.append(Tarjeta(
                            datos[0],
                            datos[1],
                            datos[2],
                            datos[3],
                            float(datos[4])
                        ))
        if tarjetas:
            return tarjetas
        else:
            # Si el archivo está vacío, devuelve una lista con una tarjeta predeterminada
            return [Tarjeta("1234-5678-9123-4567", "12/25", "123", "7123", saldo=1000)]
    except FileNotFoundError:
        # Si el archivo no existe, devuelve una lista con una tarjeta predeterminada
        return [Tarjeta("1234-5678-9123-4567", "12/25", "123", "7123", saldo=1000)]

# Función para guardar tarjetas en el archivo
def guardar_tarjetas(tarjetas):
    with open("Tarjetas.txt", "w", encoding="utf-8") as file:
        for tarjeta in tarjetas:
            file.write(tarjeta.to_string() + "\n")

# Cargar tarjetas al iniciar el programa
tarjetas_disponibles = cargar_tarjetas()

def añadir_tarjeta():
    numero = input("Introduce el número de la tarjeta a añadir: ")
    for tarjeta in tarjetas_disponibles:
        if tarjeta.numero == numero:    
            print('Tarjeta existente...')
            time.sleep(1.5)
            clear_console()
            return None
    fecha_expiracion = input("Introduce la fecha de expiración de la tarjeta a añadir: ")
    cvv = input("Introduce el CVV de la tarjeta a añadir: ")
    pin = input("Introduce el PIN de la tarjeta a añadir: ")
    saldo = float(input("Introduce el saldo actual de la tarjeta: "))

    # Crear una nueva tarjeta y agregarla a la lista
    tarjeta_nueva = Tarjeta(numero, fecha_expiracion, cvv, pin, saldo)
    tarjetas_disponibles.append(tarjeta_nueva)
    print("Tarjeta añadida correctamente.")
    
    # Guardar las tarjetas después de añadir una nueva
    guardar_tarjetas(tarjetas_disponibles)
    
    return tarjeta_nueva
    
def eliminar_tarjeta():
    numero = input("Introduce el número de la tarjeta a borrar: ")
    for i, tarjeta in enumerate(tarjetas_disponibles):
        if tarjeta.numero == numero:
            tarjeta_eliminada = tarjetas_disponibles.pop(i)
            print("Tarjeta eliminada correctamente.")
            
            # Guardar las tarjetas después de eliminar una
            guardar_tarjetas(tarjetas_disponibles)
            
            return tarjeta_eliminada

    print("La tarjeta no se encuentra en la lista.")
    return None
        
