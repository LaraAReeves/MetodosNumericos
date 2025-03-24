"""4. Aplicar el método de bisección para hallar una raíz aproximada 
de la función f(x) = x^3 + x - 5, comenzando con el intervalo [1,2], 
y el error epsilon = 0.5."""

"""4. Aplicar el método de bisección para hallar una raíz aproximada 
de la función f(x) = x^3 + x - 5, comenzando con el intervalo [1,2], 
y el error epsilon = 0.5."""

def f(x):
    return x**3 + x - 5

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
    print(f"Raiz aproximada encontrada: {c} ")
    return c

def main():
    a = 1
    b = 2
    epsilon = 0.5

    biseccion(a, b, epsilon)

if __name__ == "__main__":
    main()