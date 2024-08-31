matriz_principal=[]
fila=(100)
colum=(100)
for i in range (fila):
        matriz_principal.append([])
        for j in range (colum):
            matriz_principal[i].append(None)
#crear metodo para crear sala recibiendo la matriz principal del programa
def crear_sala():
    def llenar_sala():
        fila = int(input('Ingrese numero de filas: '))
        colum= int (input('ingresa nuemro de columnas: '))
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
                matriz_principal=sala
        print (sala)
    llenar_sala()


opc=str(input('crear sala? s/n'))
if opc == 's':
    crear_sala()
elif opc=='n':
    main()
else:
    print('seleccione opcion valida')


