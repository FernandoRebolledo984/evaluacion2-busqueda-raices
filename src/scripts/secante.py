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
    for i in range(iteraciones):
        f_x0 = f(x0)
        f_x1 = f(x1)

        x2 = x1 - f_x1*(x0-x1) / (f_x0 - f_x1) #Fórmula del método secante

        #Comprobamos tolerancia
        if abs(x2 - x1) < tol:
            print(f"\nMétodo de la secante: Raíz encontrada en la iteración {i+1}.\n")
            return x2

        #Cambiamos los valores para la siguiente iteración
        x0 = x1
        x1 = x2

    #Al alcanzar el num maximo de iteraciones:
    print("Se alcanzó el máximo de iteraciones (100)\n")
    return x1


#Estimación inicial dada por el profesor
x_0 = 2
x_1 = 3

tol = 1e-6
iteraciones = 100

raiz = secante(f, x_0, x_1, tol, iteraciones)

# ======================================== SECCIÓN DE LA GRÁFICA ========================================
X = np.linspace(0.1, 5, 400) #0,1 debido a que ln(0) no existe
Y = f(X)

plt.figure(figsize=(8,6))
plt.plot(X, Y, label='f(x) = ln(x) + x - 4', color='aqua', linewidth=2)

plt.plot(raiz, f(raiz), 'ro', markersize=5, label=f'Raíz ≈ {raiz:.4f}') #Marcamos la raíz con un punto rojo

#Líneas 'x' y 'y'
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

plt.title('Métodos numéricos - Secante ')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

#Guardamos en el directorio de assets
directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_graficas = os.path.abspath(os.path.join(directorio_script, '..', 'assets'))
ruta_guardado = os.path.join(ruta_graficas, 'grafica_secante.png')

#En caso de que la ruta no exista
os.makedirs(ruta_graficas, exist_ok=True)

plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')