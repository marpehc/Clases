import pynput



def tecla_presionada(key):
    print(key)

keyboard_listener = pynput.keyboard.Listener(on_press=tecla_presionada)

with keyboard_listener:
    keyboard_listener.join()
