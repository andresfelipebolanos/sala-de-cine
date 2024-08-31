def main():
    print('TEATRO APOLO\t DESDE 1989')
    print('1. CREAR SALA')
    print('2. VER SALA')
    print('3. ASIGNAR PUESTO')
    print('4. CARGAR SALA')
    print('5. SALIR')
    
    opcion=int(input('ELIJA UNA OPCION VALIDA 1/2/3/4/5: '))
    
    if opcion==1:
        crear_sala()
    elif opcion==2:
        ver_sala()
    elif opcion==3:
        asignar_puesto()
    elif opcion==4:
        cargar_sala()
    elif opcion==5:
        StopIteration
    else:
        print('ELIJA UNA OPCION VALIDA')
main()