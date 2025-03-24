"""2. Implementar en Python un proceso al estilo del anterior, pero que use dos funciones, 
una f y una g, y que la aplicación iterada sea una vez f, luego g, luego f, luego g, y así siguiendo, 
alternando una con otra, en total las veces que se especifique por el parámetro n, y finalmente devuelva 
el resultado obtenido tras la última aplicación."""

from math import cos

def aplicar_funciones_alternadas(f, g, x, n):
    for i in range(n):
        if i % 2 == 0:  
            x = f(x)
        else:           
            x = g(x)
    return x

if __name__ == "__main__":
    f = lambda x: cos(x**2 - 1)
    g = lambda x: x / 2 + 1

    x_inicial = 1.0
    iteraciones = 10

    resultado = aplicar_funciones_alternadas(f, g, x_inicial, iteraciones)
    print(f"Resultado despues de alternar las funciones {iteraciones} veces: {resultado}")