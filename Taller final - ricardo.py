
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


def ver_sala():  
  for f in sala :
      print("", end="")
      for c in f:
         print("{:4}".format(c), end='')
      print('')
      
print()


def crear_sala():
    try:
        filas = int(input("Ingrese el número de filas de la sala: "))
        columnas = int(input("Ingrese el número de columnas de la sala: "))
        
        nueva_sala = []
        n_asiento = 1  
        for _ in range(filas):
            fila = []
            for _ in range(columnas):
                fila.append(n_asiento)
                n_asiento += 1
            nueva_sala.append(fila)

        numero_sala = len(salas) + 1
        new_func(nueva_sala, numero_sala)

