#Funcion a utilizar = Logaritmica    ln(x) + x − 4 en [2,3]

# Elegir 2 valores iniciales diferentes cercanos a la raíz (x0 y x1)
# Utilizar x_{n+2} = x_{n+1} - ( f(x_{n+1})*(x_n - x_{n+1}) ) / ( f(x_n) - f(x_{n+1}) )
# Calcular x2 a partir de x0 y x1 con x_2 = x_1 - ( f(x_1)*(x_0 - x_1) ) / ( f(x_0) - f(x_1) )
# Iterar N veces o hasta alcanzar el criterio de error

import numpy as np
from main import tolerancia as tol, iteraciones as iter

#Función
def funcion(x):
    return np.ln(x) + x - 4

def secante():
    pass

if __name__ == "__main__":
    x_0 = 2
    x_1 = 3

    raiz = secante()