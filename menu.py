#importamos funciones que mejoran el estilo
import time
import sys
from colorama import Fore, Style, init
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

print("                                                            ")
print(f"{Fore.BLUE}\r|¡Bienvenido al Teatro Apolo!|{Style.RESET_ALL}")

print(f"{Fore.BLUE}\r| Que accion desea realizar  |{Style.RESET_ALL}")
print(f"{Fore.GREEN}________________________________{Style.RESET_ALL}")
print(f"{Fore.GREEN}|1-Crear sala | 2-Ver sala     |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|2-Ver sala   | 4-Cargar sala  |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|          5-Salir             |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|______________________________|{Style.RESET_ALL}")
#inicio menu
def menu():
    
      
      while True:
        try:
           Opcion = int(input("Ingrese la opcion que necesite (Número):  ")) 


           if Opcion==1:
              print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
              input()
              continue
          
           elif Opcion=="2":
              print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
              input()
              continue
            
           elif Opcion==3:
              print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
              input()
              continue
            
           elif Opcion==4:
              print(f"{Fore.GREEN}Presiona (Enter) para continuar{Style.RESET_ALL}")
              input()
              continue
           
           elif Opcion==5:
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
              print(f"{Fore.RED}Ingresa una opción válida{Style.RESET_ALL}")
              continue
        except ValueError:
         print(f"{Fore.RED}(Error) ingresa un caracter válido{Style.RESET_ALL}")
         
 

menu()



