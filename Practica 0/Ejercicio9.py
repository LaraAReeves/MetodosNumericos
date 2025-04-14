"""9. Método de trisección. Implementar en Python un método para aproximar raíces
 al estilo de bisección, pero que en vez de dividir el intervalo en 2 
 subintervalos lo divida en 3, y en cada iteración elija uno de los 3 
 subintervalos que contenga una raíz. Usar una condición de parada análoga 
 a la del método de bisección."""

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 + x - 10

def triseccion(a, b, epsilon, max_pasos):
    """
    Método de trisección para aproximar una raíz de la función f(x).
    Divide el intervalo en tres partes y selecciona el subintervalo
    que contiene la raíz en cada iteración.

    Args:
        a (float): Extremo inferior del intervalo inicial.
        b (float): Extremo superior del intervalo inicial.
        epsilon (float): Tolerancia para la condición de parada.
        max_pasos (int): Número máximo de iteraciones permitidas.

    Returns:
        tuple: Raíz aproximada y número de pasos realizados.
    """
    pasos = 0
    while (b - a) / 3 >= epsilon and pasos < max_pasos:
        c1 = a + (b - a) / 3
        c2 = a + 2 * (b - a) / 3
        fc1 = f(c1)
        fc2 = f(c2)

        print("------------------------------------")
        print(f"Paso {pasos + 1}")
        print(f"Intervalo actual: [{a:.6f}, {b:.6f}]")
        print(f"c1 = {c1:.6f}, f(c1) = {fc1:.6f}")
        print(f"c2 = {c2:.6f}, f(c2) = {fc2:.6f}")
        print("------------------------------------")

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

a = 1
b = 2
epsilon = 0.001
max_pasos = 100

raiz, pasos = triseccion(a, b, epsilon, max_pasos)
print(f"Raíz aproximada: {raiz:.6f}")
print(f"Cantidad de pasos necesarios: {pasos}")

x = np.linspace(a - 1, b + 1, 400)
y = f(x)

plt.plot(x, y, label='f(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(raiz, color='red', linestyle='--', label=f'Raíz aproximada ≈ {raiz:.4f}')

plt.scatter(raiz, f(raiz), color='blue', zorder=5)
plt.text(raiz + 0.05, f(raiz), f'Raíz ≈ {raiz:.4f}', color='blue', fontsize=10)

plt.text(a + 0.3, max(y) - 2, f'Pasos: {pasos}', color='green', fontsize=12)

plt.title("Método de trisección")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend(fontsize=8)
plt.show()
