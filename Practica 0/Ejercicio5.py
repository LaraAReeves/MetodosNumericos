"""5. Aplicar el método de bisección para hallar una raíz 
aproximada de la función f(x) = x^3 + x - 10 haciendo 4 pasos."""

def f(x):
    return x**3 + x - 10

def sgn(z):
    if z == 0:
        return 0
    elif z > 0:
        return 1
    else:
        return -1

def biseccion_por_pasos(a, b, pasos):
    if f(a) * f(b) >= 0:
        print("El metodo no es aplicable en este intervalo.")
        return None

    for iteracion in range(pasos):
        c = (a + b) / 2
        print(f"Paso {iteracion + 1}: a = {a}, b = {b}, c = {c}, f(c) = {f(c)}")
        
        if f(c) == 0: 
            print("Se encontro la raíz exacta.")
            return c
        elif sgn(f(c)) * sgn(f(a)) < 0: 
            b = c
        else: 
            a = c

    c = (a + b) / 2
    print(f"Raiz aproximada: {c}")
    return c

def main():
    a = 1
    b = 2
    pasos = 4

    biseccion_por_pasos(a, b, pasos)

if __name__ == "__main__":
    main()