#Función a utilizar = Exponencial   e**(-x) - x en [0,1]

# Definir la primera derivada de la función
# Bolzano
# Se escoge el valor inicial x_0, fijandose que la derivada en ese punto no sea 0
# Aplicar la fórmula x_{n+1} = x_n - ( f(x_n) / g(x_n) )
# Comprobar el error

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x) - x

def g(x):
    return -np.exp(-x) - 1

def NR(f, g, x0, tol, iteracion):
    x_actual = 0

    for i in range(iteracion):
        f_x = f(x_actual)
        g_x = g(x_actual)

        x_nxt = x_actual - (f_x / g_x)
        error = np.abs(x_nxt - x_actual) 

        if error < tol or np.abs(f(x_nxt)) < tol:
            print(f"Convergencia en iteración {i}.\n")
            return x_nxt

        x_actual = x_nxt

    print("Iteraciones máximas alcanzadas, no se logró converger.\n")
    return x_actual

# ======================================== MAIN ========================================

print("\n\nMétodo Newthon-Raphson\n")

a = 0
b = 0
x0 = 0.5
tol = 1e-6
iteracion = 100

print("Demostración de la existencia de la raíz")
f_a = f(a)
f_b = f(b)
comprobacion = f_a * f_b
if comprobacion < 0:
    print(f"Comprobación Bolzano: f(a)*f(b) = {comprobacion} < 0, por lo que la raíz está en el rango.\n")
else:
    print(f"Comprobación Bolzano: f(a)*f(b) = {comprobacion} >= 0, por lo que los valores no sirven.\n")

raiz = NR(f, g, x0, tol, iteracion)
print(f"La raíz aproximada es: {raiz:.8f}\n")