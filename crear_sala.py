
def crear_sala():
    fila = int(input('Ingrese numero de filas: '))
    colum= int(input('ingresa nuemro de columnas: '))
    acu=0
    sala=[]
    for i in range (fila):
        sala.append([])
        for j in range (colum):
            sala[i].append(0)
    for i in range (fila):
            for j in range(colum):
                acu+=1 
                sala[i][j]=acu
    print()
    for fila in sala:
        print("", end="")
        for elemento in fila:
            print("{:4}".format(elemento), end='')
        print('')
    print()

crear_sala()

