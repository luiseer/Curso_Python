import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("El valor ingresado no es lo esperado")
        print("Ejemplo número entero positivo '99'")
    else:
        # logica
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print("{:04d}".format(int(cadena[longitud-1-i]) * 10 ** i))
else:
    print("El valor ingresado no es lo esperado")
    print("Ejemplo número entero positivo '99'")
