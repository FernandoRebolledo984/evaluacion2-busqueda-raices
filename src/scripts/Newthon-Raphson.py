#Función a utilizar = Exponencial   e**(-x) - x en [0,1]

# Definir la primera derivada de la función
# Bolzano
# Se escoge el valor inicial x_0, fijandose que la derivada en ese punto no sea 0
# Aplicar la fórmula x_{n+1} = x_n - ( f(x_n) / g(x_n) )
# Comprobar el error

import numpy as np
import matplotlib.pyplot as plt
import os

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
            print(f"Convergencia en iteración {i+1}.")
            return x_nxt

        x_actual = x_nxt

    print("Iteraciones máximas alcanzadas, no se logró converger.\n")
    return x_actual

# ======================================== MAIN ========================================

print("\n\nMétodo Newthon-Raphson")

a = 0
b = 0
x0 = 0.5
tol = 1e-6
iteracion = 100

f_a = f(a)
f_b = f(b)
comprobacion = f_a * f_b
if comprobacion < 0:
    print(f"Comprobación Bolzano: f(a)*f(b) = {comprobacion} < 0, por lo que la raíz está en el rango.")
else:
    print(f"Comprobación Bolzano: f(a)*f(b) = {comprobacion} >= 0, por lo que los valores no sirven.")

raiz = NR(f, g, x0, tol, iteracion)
print(f"La raíz aproximada es: {raiz:.8f}\n")

# ======================================== GRAFICA ========================================
X = np.linspace(-0.5, 1.0, 400)
Y = f(X)

plt.figure(figsize=(8, 6))
plt.plot(X, Y, label=r'f(x) = e^{-x} - x', color='aqua', linewidth=2)

plt.plot(raiz, f(raiz), 'ro', markersize=5, label=f'Raíz ≈ {raiz:.4f}') #Marcamos la raíz

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.title('Método Numérico - Newthon-Raphson')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_graficas = os.path.abspath(os.path.join(directorio_script, '..', 'assets'))
ruta_guardado = os.path.join(ruta_graficas, 'grafica_newton_raphson.png')

os.makedirs(ruta_graficas, exist_ok=True)
plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')

# ======================================== ARCHIVO CSV ========================================
ruta_data = os.path.abspath(os.path.join(directorio_script, '..', 'data'))
os.makedirs(ruta_data, exist_ok=True)
ruta_csv = os.path.join(ruta_data, 'Newthon_Raphson.csv')
csv_datos = np.column_stack((X,Y))
np.savetxt(ruta_csv, csv_datos, delimiter=',', header='x, f(x)', comments='', fmt='%.6f')