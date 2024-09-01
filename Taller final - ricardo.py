
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

salas = {
    1: [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ],
    2: [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]
}

# Inicio del programa con breve intro del cine
print(f"{Fore.GREEN}______________________________{Style.RESET_ALL}")
print(f"{Fore.GREEN}|                            |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|       TEATRO APOLO         |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|____________________________|{Style.RESET_ALL}")
print(f"{Fore.GREEN}|                            |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|     35 años presentando    |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|   Historias inolvidables   |{Style.RESET_ALL}")
print(f"{Fore.GREEN}|____________________________|{Style.RESET_ALL}\n")

print(f"{Fore.BLUE} |-------|Cargando...|-------|  {Style.RESET_ALL}", end='', flush=True)
time.sleep(3)  # Pausa de 3 segundos
sys.stdout.write('\r' + ' ' * 100)

print(f"{Fore.BLUE}\r|¡Bienvenido a Teatro Apolo!|{Style.RESET_ALL}")

def mostrar_menu():
    print(f"{Fore.BLUE}\r|   ¿Qué acción desea realizar?   |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}___________________________________{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|1-Crear sala     | 2-Ver sala     |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|3-Asignar puesto | 4-Cargar sala  |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|             5-Salir              |{Style.RESET_ALL}")
    print(f"{Fore.GREEN}|__________________________________|{Style.RESET_ALL}")

def crear_sala():
    try:
        filas = int(input("Ingrese el número de filas de la sala: "))
        columnas = int(input("Ingrese el número de columnas de la sala: "))
        
        nueva_sala = []
        n_asiento = 1
        for _ in range(filas):
            fila = []
            for _ in range(columnas):
                fila.append(str(n_asiento))
                n_asiento += 1
            nueva_sala.append(fila)

        numero_sala = len(salas) + 1
        salas[numero_sala] = nueva_sala
        print(f"Sala {numero_sala} creada exitosamente.")
        ver_sala(numero_sala)
    except ValueError:
        print(f"{Fore.RED}Por favor, ingrese un número válido.{Style.RESET_ALL}")

def ver_sala(numero_sala):
    if numero_sala in salas:
        print(f"Sala {numero_sala}:")
        for fila in salas[numero_sala]:
            print(" ".join(fila))
    else:
        print(f"{Fore.RED}La sala {numero_sala} no existe.{Style.RESET_ALL}")

def asignar_puesto():
    try:
        numero_sala = int(input("Ingrese el número de la sala: "))
        if numero_sala in salas:
            ver_sala(numero_sala)
            asiento = input("Ingrese el número del asiento que desea reservar: ")
            for fila in salas[numero_sala]:
                if asiento in fila:
                    fila[fila.index(asiento)] = (f"{Fore.GREEN}■{Style.RESET_ALL}")
                    print(f"Asiento {asiento} reservado exitosamente.")
                    ver_sala(numero_sala)
                    return
            print(f"{Fore.RED}El asiento {asiento} no está disponible.{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}La sala {numero_sala} no existe.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Por favor, ingrese un número válido.{Style.RESET_ALL}")

def menu():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese la opción que necesite (Número):  ")) 

            if opcion == 1:
                print(f"{Fore.GREEN}Has seleccionado 'Crear sala'.{Style.RESET_ALL}")
                crear_sala()
                input(f"{Fore.GREEN}Presiona (Enter) para continuar...{Style.RESET_ALL}")
            
            elif opcion == 2:
                print(f"{Fore.GREEN}Has seleccionado 'Ver sala'.{Style.RESET_ALL}")
                numero_sala = int(input("Ingrese el número de la sala: "))
                ver_sala(numero_sala)
                input(f"{Fore.GREEN}Presiona (Enter) para continuar...{Style.RESET_ALL}")
            
            elif opcion == 3:
                print(f"{Fore.GREEN}Has seleccionado 'Asignar puesto'.{Style.RESET_ALL}")
                asignar_puesto()
                input(f"{Fore.GREEN}Presiona (Enter) para continuar...{Style.RESET_ALL}")
            
            elif opcion == 4:
                print(f"{Fore.GREEN}Has seleccionado 'Cargar sala'.{Style.RESET_ALL}")
                # Aquí podrías cargar la sala desde un archivo o base de datos si lo necesitas
                input(f"{Fore.GREEN}Presiona (Enter) para continuar...{Style.RESET_ALL}")
            
            elif opcion == 5:
                print(f"{Fore.BLUE}|-----|Gracias por utilizar nuestros servicios|------|\n{Style.RESET_ALL}")
                print(f"{Fore.BLUE}|-------------|Hasta pronto|------------------|\n{Style.RESET_ALL}")
                time.sleep(2)
                break
            else:
                print(f"{Fore.RED}Ingresa una opción válida (1-5).{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}(Error) Ingresa un número válido.{Style.RESET_ALL}")

menu()
