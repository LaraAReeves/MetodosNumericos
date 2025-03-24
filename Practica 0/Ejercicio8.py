"""8. Modificar la implementación del método de bisección para que:

a) Haga la menor cantidad posible de evaluaciones de la f en cada iteración

b) Vaya imprimiendo la secuencia de los puntos p que van aproximando a la raíz buscada

c) Que tenga una cota (grande) en la cantidad total de pasos que dará antes de devolver algo

d) Que devuelva, además del p encontrado, la cantidad de pasos que fueron necesarios para llegar a la aproximación buscad"""

def f(x):
    return x**2 + x - 12

def biseccion_modificada(a, b, epsilon, max_pasos):
    
    pasos = 0
    fa = f(a)
    fb = f(b) 

    while (b - a) / 2 >= epsilon and pasos < max_pasos:
        c = (a + b) / 2
        fc = f(c)
        print(f"Paso {pasos + 1}: p = {c}")

        if fc == 0:
            return c, pasos + 1
        elif fa * fc < 0:
            b = c
            fb = fc
        else: 
            a = c
            fa = fc 

        pasos += 1

    c = (a + b) / 2
    return c, pasos

def f(x):
    return x**3 + x - 10

def main():
    a = 1
    b = 2
    epsilon = 0.001
    max_pasos = 100

    raiz, pasos = biseccion_modificada(a, b, epsilon, max_pasos)
    print(f"Raiz aproximada: {raiz}")
    print(f"Cantidad de pasos necesarios: {pasos}")

if __name__ == "__main__":
    main()