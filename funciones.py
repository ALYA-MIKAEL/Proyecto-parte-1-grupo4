import os  #Funciones del sistema operativo
import platform  #Funciones para averiguar cosas sobre la plataforma
def limpiar_consola():
    """
    -Trabaja con los módulos "platform" y "os"

    -Esta funcion limpia la consola dependiendo que         sistema operativo estes usando
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
