#Función a utilizar = Trigonometrica    cos(x) - x en [0,1]

# Transformar 'f(x) = 0' a 'x = f(x)'
# Garantizar que |g'(x)| < 1. Si es mayor que 1, volver al paso 1 y buscar un despeje distinto
# Definir el valor iniciarl x_0
# Aplicar fórmula del método x_{n+1} = g(x_n)
# Verificar que el resultado de la resta entre el valor anterior y el actual sea menor a la tolerancia. De lo contrario, repetir el paso anterior

import numpy as np
import matplotlib.pyplot as plt
import os

# ======================================== CÓDIGO PRINCIPAL ========================================

#Función original e iterativa
def f(x):
    return np.cos(x) - x
def g(x):
    return np.cos(x)

def punto_fijo(g, x0, tol, iteracion):
    x_actual = x0
    errores = [] #Para las tablas

    for i in range(iteracion):
        x_nxt = g(x_actual) #Fórmula método
        error = np.abs(x_nxt - x_actual)
        errores.append(error)

        if error < tol:
            print(f"Convergencia en iteración {i+1}")
            return x_nxt, errores

        x_actual = x_nxt

    print("El método no convergió en el número máximo de iteraciones") #En caso de pasarse
    return x_actual, errores

# ======================================== MAIN ========================================

print("\n\nMétodo del Punto Fijo")

a = 0
b = 1
x0 = 0.5
tol = 1e-6
iteracion = 100

#Bolzano
print(f"Comprobación bolzano: f(a)*f(b)<0 = {f(a):.6f} * {f(b):.6f} < 0\n")

raiz, errores = punto_fijo(g, x0, tol, iteracion)

print(f"La raíz aproximada es {raiz:.7f}\n")

# ======================================== RUTAS ========================================
script_directory = os.path.dirname(os.path.abspath(__file__))
ruta_graficas = os.path.abspath(os.path.join(script_directory, '..', 'assets'))
ruta_data = os.path.abspath(os.path.join(script_directory, '..', 'data'))

#Por si acaso
os.makedirs(ruta_graficas, exist_ok=True)
os.makedirs(ruta_data, exist_ok=True)

# ======================================== GRÁFICAS ========================================

# === GRÁFICA 1 ===
X = np.linspace(a, b, 200)
Y = f(X)

plt.figure(figsize=(8,5))
plt.plot(X, Y, color='blue', linewidth=2, label='f(x) = cos(x) - x')
plt.axhline(0, color='black', linewidth=1)
plt.plot(raiz, f(raiz), 'ro', markersize=8, label=f'Raíz ≈ {raiz:.6f}')

plt.title("Función con su raíz marcada", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.grid(True, alpha=0.4)
plt.legend()

plt.savefig(os.path.join(ruta_graficas, 'raiz_punto_fijo.png'), dpi=300, bbox_inches='tight')
plt.close()

# === GRÁFICA 2 ===
iteraciones_x = np.arange(1, len(errores)+1)

plt.figure(figsize=(8,5))
plt.plot(iteraciones_x, errores, marker='o', color='blue', markeredgecolor='blue', linewidth=2, label='Punto fijo')
plt.axhline(tol, color='red', linestyle='--', linewidth=1, label='Tolerancia')
plt.yscale('log')   #Por pauta

plt.title("Convergencia de error - Punto Fijo", fontsize=14)
plt.xlabel("Iteración", fontsize=12)
plt.ylabel("Error absoluto (log)", fontsize=12)
plt.grid(True, which='both', alpha=0.4)
plt.legend()

plt.savefig(os.path.join(ruta_graficas, 'convergencia_punto_fijo.png'), dpi=300, bbox_inches='tight')

# ======================================== ARCHIVO CSV ========================================
ruta_csv = os.path.join(ruta_data, 'punto_fijo.csv')
csv_datos = np.column_stack((X,Y))
np.savetxt(ruta_csv, csv_datos, delimiter=',', header='x, f(x)', comments='')