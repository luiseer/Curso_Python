import sys

if len(sys.argv) == 3:
    text = sys.argv[1]
    rep = int(sys.argv[2])

    for r in range(rep):
        print(text)
else:
    print("Falta un argumento")
    print('Ejemplo: escribir_lineas.py "Texto" 5')
