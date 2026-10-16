#Funcion a utilizar = Logaritmica    ln(x) + x − 4 en [2,3]

# Elegir 2 valores iniciales diferentes cercanos a la raíz (x0 y x1)
# Utilizar x_{n+2} = x_{n+1} - ( f(x_{n+1})*(x_n - x_{n+1}) ) / ( f(x_n) - f(x_{n+1}) )
# Calcular x2 a partir de x0 y x1 con x_2 = x_1 - ( f(x_1)*(x_0 - x_1) ) / ( f(x_0) - f(x_1) )
# Iterar N veces o hasta alcanzar el criterio de error

import numpy as np
import matplotlib.pyplot as plt
import os


# ======================================== CÓDIGO PRINCIPAL ========================================
#Función
def f(x):
    return np.log(x) + x - 4

#Operaciones para secante
def secante(f,x0,x1,tol,iteraciones):
    errores = [] #Para la tabla
    for i in range(iteraciones):
        f_x0 = f(x0)
        f_x1 = f(x1)

        x2 = x1 - f_x1*(x0-x1) / (f_x0 - f_x1) #Fórmula del método secante
        error = abs(x2-x1)
        errores.append(error)

        #Comprobamos tolerancia
        if error < tol:
            print(f"Convergencia en iteración {i+1}.")
            return x2, errores

        #Cambiamos los valores para la siguiente iteración
        x0 = x1
        x1 = x2

    #Al alcanzar el num maximo de iteraciones:
    print("Se alcanzó el máximo de iteraciones (100)\n")
    return x1, errores

# ======================================== MAIN ========================================
print("\n\nMétodo de la secante")
#Estimación inicial dada por el profesor
a = 2
b = 3
x_0 = 2
x_1 = 3
tol = 1e-6
iteraciones = 100

raiz, errores = secante(f, x_0, x_1, tol, iteraciones)
print(f"La raíz aproximada es {raiz:.6f}\n")

# ======================================== RUTAS ========================================
script_directory = os.path.dirname(os.path.abspath(__file__))
ruta_graficas = os.path.abspath(os.path.join(script_directory, '..', 'assets'))
ruta_data = os.path.abspath(os.path.join(script_directory, '..', 'data'))
#por si acaso
os.makedirs(ruta_graficas, exist_ok=True)
os.makedirs(ruta_data, exist_ok=True)

# ======================================== GRÁFICAS ========================================
# === GRÁFICA 1 ===
X = np.linspace(a, b, 200)
Y = f(X)

plt.figure(figsize=(8,5))
plt.plot(X, Y, color='blue', linewidth=2, label='f(x) = ln(x) + x - 4')
plt.axhline(0, color='black', linewidth=1)
plt.plot(raiz, f(raiz), 'ro', markersize=8, label=f'Raíz ≈ {raiz:.6f}')

plt.title('Función con su raíz marcada', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.grid(True, alpha=0.4)
plt.legend()

plt.savefig(os.path.join(ruta_graficas, 'raiz_secante.png'), dpi=300, bbox_inches='tight')
plt.close()

# === GRÁFICA 2 ===
iteraciones_x = np.arange(1, len(errores)+1)

plt.figure(figsize=(8,6))
plt.plot(iteraciones_x, errores, marker='o', color='blue', markeredgecolor='blue', linewidth=2, label='Secante')
plt.axhline(tol, color='red', linestyle='--', linewidth=1, label='Tolerancia')
plt.yscale('log')
plt.xticks(iteraciones_x) #Enteros

plt.title('Convergencia del error - Método de la Secante', fontsize=14)
plt.xlabel('Iteración', fontsize=12)
plt.ylabel('Error absoluto (log)', fontsize=12)
plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.legend()

plt.savefig(os.path.join(ruta_graficas, 'convergencia_secante.png'), dpi=300, bbox_inches='tight')
plt.close()

# ======================================== ARCHIVO CSV ========================================
ruta_csv = os.path.join(ruta_data, 'secante.csv')
csv_datos = np.column_stack((X,Y))
np.savetxt(ruta_csv, csv_datos, delimiter=',', header='x, f(x)', comments='', fmt=['%d', '%.8f'])