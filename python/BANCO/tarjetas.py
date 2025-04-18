class Tarjeta:
    def __init__(self, numero, fecha_expiracion, cvv, pin, saldo=0):
        self.numero = numero
        self.fecha_expiracion = fecha_expiracion
        self.cvv = cvv
        self.pin = pin
        self.saldo = saldo
      
tarjetas_disponibles = [
    Tarjeta("1234-5678-9123-4567", "12/25", "123", "7123", saldo=1000)]

        
        

        
        
        