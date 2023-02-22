def suma(a,b):
    try:
        return a + b
    except TypeError:
        print("Error: Tipo de dato invalido")
    else:
        return a + b

def resta(a,b):
    try:
        return a - b
    except TypeError:
        print("Error: Tipo de dato invalido")
    else:
        return a - b

def multiplicacion(a,b):
    try:
        return a * b
    except TypeError:
        print("Error: Tipo de dato invalido")
    else:
        return a * b
        
def division(a,b):
    try:
        return a / b
    except TypeError:
        print("Error: Tipo de dato invalido")
    except ZeroDivisionError:
        print("No es posible la división entre 0 batido!")
    else:
        return a * b
