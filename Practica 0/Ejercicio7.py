"""7. Aplicar el método de bisección para aproximar un x que cumpla cos(x) = -1, 
con error menor que epsilon = 1/10. Notar que esto sirve para encontrar aproximaciones de pi."""

import math

def f(x):
    return math.cos(x) + 1

def biseccion(a, b, epsilon):
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

def main():
    a = 3
    b = 4
    epsilon = 0.1

    raiz_aproximada = biseccion(a, b, epsilon)

    valor_pi = math.pi
    print(f"Raiz por biseccion: {raiz_aproximada}")
    print(f"Valor exacto de pi: {valor_pi}")
    print(f"Diferencia: {abs(raiz_aproximada - valor_pi)}")

if __name__ == "__main__":
    main()