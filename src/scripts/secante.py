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
x_0 = 2
x_1 = 3
tol = 1e-6
iteraciones = 100

raiz, errores = secante(f, x_0, x_1, tol, iteraciones)
print(f"La raíz aproximada es {raiz:.6f}\n")

# ======================================== SECCIÓN DE LA GRÁFICA ========================================
iteraciones_x = np.arange(1, len(errores)+1)

plt.figure(figsize=(8,6))
plt.plot(iteraciones_x, errores, marker='o', color='blue', markeredgecolor='blue', linewidth=2, label='Error absoluto')
plt.axhline(tol, color='red', linestyle='--', linewidth=1, label=f'Tolerancia')

plt.title('Convergencia del error - Método de la Secante ')
plt.xlabel('Iteración')
plt.ylabel('Error absoluto')
plt.xticks(iteraciones_x)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_graficas = os.path.abspath(os.path.join(directorio_script, '..', 'assets'))
ruta_guardado = os.path.join(ruta_graficas, 'grafica_secante.png')

os.makedirs(ruta_graficas, exist_ok=True)
plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')

# ======================================== ARCHIVO CSV ========================================
ruta_data = os.path.abspath(os.path.join(directorio_script, '..', 'data'))
os.makedirs(ruta_data, exist_ok=True)
ruta_csv = os.path.join(ruta_data, 'secante.csv')
csv_datos = np.column_stack((iteraciones_x,errores))
np.savetxt(ruta_csv, csv_datos, delimiter=',', header='iteracion, error_absoluto)', comments='', fmt=['%d', '%.8f'])