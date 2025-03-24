"""0. Tomar una calculadora de mano. Elegir una función existente. Introducir un número x en el display. 
Calcular la función aplicada a ese número que se ve. Aplicar nuevamente la función, y otra vez más, y así siguiendo. 
Probar esto con distintos x. ¿Ocurre algo notable... a veces?

1. Implementar en Python el proceso anterior, que use una función (externa implementada, o bien pasada como parámetro), 
que lea el x como parámetro y un n natural, y luego sobre el ex inicial aplique la f n veces, finalmente devolviendo el 
resultado obtenido tras la última aplicación."""

from math import cos

def aplicar_funcion_repetidamente(f, x, n):
    for _ in range(n):
        x = f(x)
    return x

if __name__ == "__main__":
    funcion = lambda x: cos(x**2 + x - 1)
    x_inicial = 1.0
    iteraciones = 10

    resultado = aplicar_funcion_repetidamente(funcion, x_inicial, iteraciones)
    print(f"Resultado despues de aplicar la funcion {iteraciones} veces: {resultado}")