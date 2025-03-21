import pynput
from pynput.keyboard import Controller
import time

keyboard = Controller

def tecla_presionada(key):
    print(key)

keyboard_listener = pynput.keyboard.Listener(on_press=tecla_presionada)

with keyboard_listener:
    keyboard_listener.join()

time.sleep(3)
keyboard.type("Hola, esto es un mensaje automático.")