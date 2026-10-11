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

    for i in range(iteracion):
        x_nxt = g(x_actual) #Fórmula método

        error = np.abs(x_nxt - x_actual)

        print(f"Iteración {i+1}: x = {x_nxt:.7f}, error = {error:.7f}\n")

        if error < tol:
            print(f"Convergencia en iteración {i+1}\n")
            return x_nxt

        x_actual = x_nxt

    print("El método no convergió en el número máximo de iteraciones\n") #En caso de pasarse
    return 0

# ======================================== MAIN ========================================

print("\n\nMétodo del Punto Fijo\n")

a = 0
b = 1
x0 = 0.5
tol = 1e-6
iteracion = 100

print(f"Demostración de existencia de la raíz:")
f_a = f(a)
f_b = f(b)
print(f"f({a}) = {f_a} // f({b}) = {f_b}")
if f_a * f_b < 0:
    print(f"{f_a} * {f_b} < 0, por lo que existe raíz.\n")
else:
    print(f"{f_a} * {f_b} >= 0, por lo tanto no existe raíz.\n") #Nunca se ejecutará por los valores que ya definimos

raiz = punto_fijo(g, x0, tol, iteracion)

print(f"La raíz aproximada es {raiz:.7f}\n")

# ======================================== GRÁFICA ========================================
x_val = np.linspace(-1, 2, 400)
y_val = f(x_val)

plt.figure(figsize=(8,5))
plt.plot(x_val, y_val, label=r'$f(x) = \cos(x) - x$', color='aqua', linewidth=2)
plt.axhline(0,color='black',linewidth=1,linestyle='--') #Eje X

plt.plot(raiz,0,'ro',markersize=8,label=f'Raíz aprox: {raiz:.6f}') #Marcador de la raíz

plt.title("Método numérico - Punto Fijo", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid(True, alpha=0.4)
plt.legend(loc='upper right', fontsize=10)

directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_graficas = os.path.abspath(os.path.join(directorio_script, '..', 'assets'))
ruta_guardado = os.path.join(ruta_graficas, 'grafica_punto_fijo.png')

#En caso de que la ruta no exista
os.makedirs(ruta_graficas, exist_ok=True)

plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')