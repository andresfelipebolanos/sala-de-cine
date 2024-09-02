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
crear_sala()

