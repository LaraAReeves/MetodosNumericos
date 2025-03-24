"""9. Método de trisección. Implementar en Python un método para aproximar raíces
 al estilo de bisección, pero que en vez de dividir el intervalo en 2 
 subintervalos lo divida en 3, y en cada iteración elija uno de los 3 
 subintervalos que contenga una raíz. Usar una condición de parada análoga 
 a la del método de bisección."""

def f(x):
    return x**3 + x - 10

def triseccion(a, b, epsilon, max_pasos):

    pasos = 0

    while (b - a) / 3 >= epsilon and pasos < max_pasos:
        c1 = a + (b - a) / 3
        c2 = a + 2 * (b - a) / 3
        fc1 = f(c1)
        fc2 = f(c2)

        print(f"Paso {pasos + 1}: c1 = {c1}, f(c1) = {fc1}, c2 = {c2}, f(c2) = {fc2}")

        if fc1 == 0:
            return c1, pasos + 1
        elif fc2 == 0:
            return c2, pasos + 1
        elif f(a) * fc1 < 0:
            b = c1
        elif fc1 * fc2 < 0:
            a = c1
            b = c2
        else:
            a = c2

        pasos += 1

    p = (a + b) / 2
    return p, pasos

def main():
    a = 1
    b = 2
    epsilon = 0.001
    max_pasos = 100

    raiz, pasos = triseccion(a, b, epsilon, max_pasos)
    print(f"Raiz aproximada: {raiz}")
    print(f"Cantidad de pasos necesarios: {pasos}")

if __name__ == "__main__":
    main()