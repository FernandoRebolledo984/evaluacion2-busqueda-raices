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
    errores = [] #Para las gráficas

    for i in range(iteracion):
        f_x = f(x_actual)
        g_x = g(x_actual)

        #Por si acaso
        if g_x == 0:
            print("La derivada es 0 en un punto, no se puede continuar.")
            return x_actual, errores

        x_nxt = x_actual - (f_x / g_x)
        error = np.abs(x_nxt - x_actual) 
        errores.append(error) #Almacenamos para las gráficas

        if error < tol:
            print(f"Convergencia en iteración {i+1}.")
            return x_nxt, errores

        x_actual = x_nxt

    print("Iteraciones máximas alcanzadas, no se logró converger.\n")
    return x_actual, errores

# ======================================== MAIN ========================================

print("\n\nMétodo Newthon-Raphson")

a = 0
b = 0
x0 = 0.5
tol = 1e-6
iteracion = 100

raiz, errores = NR(f, g, x0, tol, iteracion)
print(f"La raíz aproximada es: {raiz:.8f}\n")

# ======================================== RUTAS ========================================
script_directory = os.path.dirname(os.path.abspath(__file__))
ruta_graficas = os.path.abspath(os.path.join(script_directory, '..', 'assets'))
ruta_data = os.path.abspath(os.path.join(script_directory, '..', 'data'))
#por si acaso
os.makedirs(ruta_graficas, exist_ok=True)
os.makedirs(ruta_data, exist_ok=True)

# ======================================== GRAFICAS ========================================
# === GRÁFICA 1 ===
X = np.linspace(a, b, 200)
Y = f(X)

plt.figure(figsize=(8,5))
plt.plot(X, Y, color='blue', linewidth=2, label='f(x) = e^(-x) - x')
plt.axhline(0, color='black', linewidth=1)
plt.plot(raiz, f(raiz), 'ro', markersize=8, label=f'Raíz ≈ {raiz:.6f}')

plt.title('Función con su raíz marcada', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.xlabel('f(x)', fontsize=12)
plt.grid(True, alpha=0.4)
plt.legend()

plt.savefig(os.path.join(ruta_graficas, 'raiz_exponencial.png'), dpi=300, bbox_inches='tight')
plt.close()

# === GRÁFICA 2 ===
iteraciones_x = np.arange(1, len(errores)+1)

plt.figure(figsize=(8, 6))
plt.plot(iteraciones_x, errores, marker='o', color='blue', markeredgecolor='blue', label='Newthon-Raphson')
plt.axhline(tol, color='red', linestyle='--',linewidth=1, label='Tolerancia')
plt.yscale('log')
plt.xticks(iteraciones_x)

plt.title('Convergencia del error - Newthon-Raphson', fontsize=14)
plt.xlabel('Iteración', fontsize=12)
plt.ylabel('Error absoluto (log)', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()

plt.savefig(os.path.join(ruta_graficas, 'convergencia_newthon_raphson.png'), dpi=300, bbox_inches='tight')
plt.close()

# ======================================== ARCHIVO CSV ========================================
ruta_csv = os.path.join(ruta_data, 'Newthon_Raphson.csv')
csv_datos = np.column_stack((X,Y))
np.savetxt(ruta_csv, csv_datos, delimiter=',', header='x, f(x)', comments='', fmt=['%d', '%.8f'])