import funciones

def menu():
  funciones.limpiar_consola()
  print("""
   / \  / ___| / ___|_ _|_ _|    / \   _ __| |_ 
  / _ \ \___ \| |    | | | |    / _ \ | '__| __|   
 / ___ \ ___) | |___ | | | |   / ___ \| |  | |_   
/_/   \_\____/ \____|___|___| /_/   \_\_|   \__| 
        
                           """)
  print("""
          
           Menú
══════════════════════════

1. Mostrar un ASCII ART
2. Rotar 90 grados en sentido anti ho-
rario
3. Rotar 90 grados en sentido anti ho-
rario
4. Rotar 180 grados en sentido horario
5. Rotar 180 grados en sentido anti ho-
rario
6. Frecuencias de caracteres
0. Salir del programa
        
  """)
  opcion = str(input("Ingrese una Opcion --→ "))
  return opcion