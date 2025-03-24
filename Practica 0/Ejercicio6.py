"""6. Aplicar el método de bisección para hallar una aproximación de un x que cumpla x^2 + x = 12. 
Calcular luego el valor exacto de otra manera, y comparar."""

import math

def f(x):
    return x**2 + x - 12

def biseccion(a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("El metodo no es aplicable en este intervalo.")
        return None

    iteracion = 0
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        print(f"Iteracion {iteracion}: a = {a}, b = {b}, c = {c}, f(c) = {f(c)}")
        
        if f(c) == 0: 
            print("Se encontro la raiz exacta.")
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        iteracion += 1

    c = (a + b) / 2
    print(f"Raiz aproximada encontrada: {c}")
    return c

def calcular_exacto():
    a = 1
    b = 1
    c = -12
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None  
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return x1, x2

def main():
    a = 0
    b = 10
    epsilon = 0.5

    raiz_aproximada = biseccion(a, b, epsilon)

    valores_exactos = calcular_exacto()

    print(f"Raiz aproximada por biseccion: {raiz_aproximada}")
    print(f"Valores exactos calculados: {valores_exactos}")

if __name__ == "__main__":
    main()