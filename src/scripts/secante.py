#Funcion a utilizar = Logaritmica    ln(x) + x − 4 en [2,3]

# Elegir 2 valores iniciales diferentes cercanos a la raíz (x0 y x1)
# Utilizar x_{n+2} = x_{n+1} - ( f(x_{n+1})*(x_n - x_{n+1}) ) / ( f(x_n) - f(x_{n+1}) )
# Calcular x2 a partir de x0 y x1 con x_2 = x_1 - ( f(x_1)*(x_0 - x_1) ) / ( f(x_0) - f(x_1) )
# Iterar N veces o hasta alcanzar el criterio de error

import numpy as np
from main import tolerancia as tol, iteraciones as iter

#Función
def f(x):
    return np.ln(x) + x - 4

#Operaciones para secante
def secante(f,x0,x1,tol,iter):
    for i in range(iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        x2 = x1 - f_x1*(x0-x1) / (f_x0 - f_x1) #Fórmula del método secante

        #Comprobamos tolerancia
        if abs(x2 - x1) < tol:
            print(f"Raíz encontrada en la iteración {i+1}.\n")
            return x2

        #Cambiamos los valores para la siguiente iteración
        x0 = x1
        x1 = x2

    #Al alcanzar el num maximo de iteraciones:
    print("Se alcanzó el máximo de iteraciones (100)\n")
    return x1

if __name__ == "__main__":
    x_0 = 2
    x_1 = 3

    raiz = secante(f, x_0, x_1, tol, iter)