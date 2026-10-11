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

        x_nxt = x_actual - (f_x / g_x)
        error = np.abs(x_nxt - x_actual) 
        errores.append(error) #Almacenamos para las gráficas

        if error < tol or np.abs(f(x_nxt)) < tol:
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

# ======================================== GRAFICA ========================================
iteraciones_x = np.arange(1, len(errores)+1)

plt.figure(figsize=(8, 6))
plt.plot(iteraciones_x, errores, marker='o', color='blue', markeredgecolor='blue', label='Error absoluto')
plt.axhline(tol, color='red', linestyle='--',linewidth=1, label='Tolerancia')

plt.title('Convergencia del error - Newthon-Raphson')
plt.xlabel('Iteración')
plt.ylabel('Error absoluto')
plt.xticks(iteraciones_x)
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
csv_datos = np.column_stack((iteraciones_x,errores))
np.savetxt(ruta_csv, csv_datos, delimiter=',', header='x, f(x)', comments='', fmt='%.6f')