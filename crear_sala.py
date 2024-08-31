#defino la matriz principal para fines de prueba, pues esta habita en el main del programa
matriz_principal=[]
fil=(100)
col=(100)
for i in range (fil):
        matriz_principal.append([])
        for j in range (col):
            matriz_principal[i].append(0)
#crear metodo para crear sala modificando la matriz principal
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
    print (sala)
crear_sala()

