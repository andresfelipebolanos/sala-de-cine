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
        print(f"{Fore.RED}Sala Cargada Exitósamente desde: {filename}{Style.RESET_ALL}")
        return matriz
    except FileNotFoundError:
        print(f"{Fore.RED}Archivo '{filename}' no encontrado. {Style.RESET_ALL}")
        return []
    except pickle.PickleError as e:
        print(f"{Fore.RED}Error al cargar el archivo {e} {Style.RESET_ALL}")
        return []