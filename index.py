print('repositorio para el proyecto sala de cine')
import pickle
import time
import sys
from colorama import Fore, Style, init

def guardar_matriz(matriz, filename):
    """Guarda la matriz en un archivo utilizando pickle."""
    with open(filename, 'wb') as archivo:
        pickle.dump(matriz, archivo)
    print(f"{Fore.GREEN}Sala Cargada Exitósamente en: {filename}{Style.RESET_ALL}")

def cargar_matriz(filename):
    """Carga la matriz desde un archivo utilizando pickle."""
    try:
        with open(filename, 'rb') as archivo:
            matriz = pickle.load(archivo)
        print(f"{Fore.GREEN}Sala Cargada Exitósamente desde: {filename}{Style.RESET_ALL}")
        return matriz
    except FileNotFoundError:
        print(f"{Fore.RED}Archivo '{filename}' no encontrado. {Style.RESET_ALL}")
        return []
    except pickle.PickleError as e:
        print(f"{Fore.RED}Error al cargar el archivo {e} {Style.RESET_ALL}")
        return []

def  crear_sala(f,c):
    global sala
    acu=0
    sala=[]
    for i in range (f):
        sala.append([])
        for j in range (c):
            sala[i].append(0)
    for i in range (f):
            for j in range(c):
                acu+=1 
                sala[i][j]=acu
    print()


def ver_sala():
    
  for f in sala :
      print("   ", end="   ")
      for c in f:
         print("{:2}".format(c), end='  ')
      print('')

def asignar_p():
    """Asigna un puesto en la sala."""
    while True:
        try:
            ver_sala()
            print("")
            asiento = int(input("Ingrese el número del asiento para reservar: "))
            for f in sala:
                if asiento in f:
                    index = f.index(asiento)
                    f[index] = f"{Fore.GREEN}X{Style.RESET_ALL}"
                    print(f"{Fore.GREEN}Asiento {asiento} reservado exitósamente.{Style.RESET_ALL}")
                    print("")
                    ver_sala()
                    print("")
                    print("")
                    return
            print(f"{Fore.RED}Ingrese un carácter válido{Style.RESET_ALL}")
            False
        except ValueError:
            print(f"{Fore.RED}Ingrese un carácter válido{Style.RESET_ALL}")
            break
      
print()
#importamos funciones que mejoran el estilo

Matriz_Pricinpal=[]
#inicio del programa con breve intro del cine
print(f"{Fore.GREEN}______________________________{Style.RESET_ALL}")
print(f"{Fore.GREEN}|                            |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|       TEATRO APOLO         |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|____________________________|{Style.RESET_ALL}")
print(f"{Fore.GREEN}|                            |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|     35 años generando      |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|   Historias inolvidables   |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|____________________________|{Style.RESET_ALL}\n")


print(f"{Fore.BLUE} |-------|Cargando...|-------|  {Style.RESET_ALL}", end='', flush=True)
time.sleep(3)  # Pausa de 3 segundos
sys.stdout.write('\r' + ' ' * 100)
#una intro del cine
print("                                                            ")
def mostrar_menu():
 print(f"{Fore.BLUE}\r|¡Bienvenido al Teatro Apolo!|{Style.RESET_ALL}")

 print(f"{Fore.BLUE}\r| Que accion desea realizar  |{Style.RESET_ALL}")
 print(f"{Fore.GREEN}____________________________________{Style.RESET_ALL}")
 print(f"{Fore.GREEN}|1-Crear sala     | 2-Ver sala     |{Style.RESET_ALL}")
 print(f"{Fore.GREEN}|3-Asignar Puestos| 4-Guardar sala |{Style.RESET_ALL}")
 print(f"{Fore.GREEN}|5-Cargar Sala    | 6-Salir        |{Style.RESET_ALL}")
 print(f"{Fore.GREEN}|_________________|________________|{Style.RESET_ALL}")
#inicio menu
def menu():
    global sala
    sala = []
    while True:
        print("")
        mostrar_menu()
        try:
           Opcion = int(input("Ingrese la opcion que necesite (Número):  ")) 
           print("")
           #aqui se elige el numero

           if Opcion==1:
              print(f"{Fore.GREEN}¡Haz seleccionado Crear sala!{Style.RESET_ALL}")
              while True:
                  try:
                      
                      f=int(input("ingrese el numero de filas: "))
                      c=int(input("ingresa el numero de columnas: "))
                      crear_sala(f,c)
                      print(f"{Fore.GREEN}Sala Creada Exitósamente{Style.RESET_ALL}")
                      print(" ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")      
                      print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
                      input()
                      print("")
                      print("")
                      break
                  except ValueError:
                    print(f"{Fore.RED}(Error) ingresa un caracter válido{Style.RESET_ALL}")
                    False
              
           
          
           elif Opcion==2:
              print(f"{Fore.GREEN}¡Haz seleccionado ver sala!{Style.RESET_ALL}")
              print("")
              try:
                  if sala:   
                     ver_sala()
                     print("")
                  else:
                     print(f"{Fore.RED}(Error) No hay salas disponibles{Style.RESET_ALL}")   
              except NameError:
                 print(f"{Fore.RED}(Error) No hay Salas disponibles{Style.RESET_ALL}") 
              print(" ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")
              print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
              input()
              print("")
              print("")
              continue
            
           elif Opcion==3:
                try:
                    if sala:
                     asignar_p()
                    else:
                        print(f"{Fore.RED}(Error) No hay Salas disponibles{Style.RESET_ALL}")
                except NameError:
                    print(f"{Fore.RED}(Error) No hay salas disponibles{Style.RESET_ALL}") 
                print(" ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓")
                print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
                input()
                print("")
                print("")
                continue
            
              
            
           elif Opcion==4:
              print(f"{Fore.GREEN}¡Haz seleccionado guardar sala!{Style.RESET_ALL}")
              while True:
               
                   nombre_archivo_guardar = input("Ingrese el nombre del archivo para guardar la matriz (con extensión .pkl): ")
                   if sala:  # Solo guarda si la sala existe
                     guardar_matriz(sala, nombre_archivo_guardar)
                     break
                   else:
                     print(f"{Fore.RED}(Error) No hay salas disponibles{Style.RESET_ALL}")
                     break
              print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
              input()
              print("")
              print("")
              continue
              
           
           elif Opcion==5:
              nombre_archivo_cargar = input("Ingrese el nombre de su factura (con extensión .pkl): ")
              sala= cargar_matriz(nombre_archivo_cargar)
              if sala:
                    de= nombre_archivo_cargar[:-4]
                    print(f"{Fore.GREEN}Su factura: {de}{Style.RESET_ALL}")
                    ver_sala()
                    matriz_cargada = cargar_matriz(nombre_archivo_cargar)
              print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
              input()
              print("")
              print("")
              continue 
           
           elif Opcion==6:
              #aqui termina el programa, dando una breve despedida amigable
              print(f"{Fore.BLUE}|-----|Gracias por utilizar nuestros|------|\n{Style.RESET_ALL}", end='', flush=True)
              print(f"{Fore.BLUE}|-------------|Servicios|------------------|\n{Style.RESET_ALL}", end='', flush=True)
              time.sleep(4)
              sys.stdout.write('\r' + ' ' * 100)
              print("                                                            ")
              print(f"{Fore.GREEN}______________________________{Style.RESET_ALL}") 
              print(f"{Fore.GREEN}|                            |{Style.RESET_ALL}")
              print(f"{Fore.GREEN}|       TEATRO APOLO         |{Style.RESET_ALL}")
              print(f"{Fore.GREEN}|____________________________|{Style.RESET_ALL}")
              print(f"{Fore.GREEN}|                            |{Style.RESET_ALL}")
              print(f"{Fore.GREEN}|     35 años generando      |{Style.RESET_ALL}")
              print(f"{Fore.GREEN}|   Historias inolvidables   |{Style.RESET_ALL}")
              print(f"{Fore.GREEN}|____________________________|{Style.RESET_ALL}\n")
              break
           else:
              #por si no se ingresa una opcion valida
              print(f"{Fore.RED}Ingresa una opción válida{Style.RESET_ALL}")
              continue
           #por si no se ingresa un caracter valido
        except ValueError:
         print(f"{Fore.RED}(Error) ingresa un caracter válido{Style.RESET_ALL}")
         
 

menu()
