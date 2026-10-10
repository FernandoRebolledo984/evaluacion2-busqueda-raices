#Raíz doble f(x) = (x − 2)²
import numpy as np


def funcion_raiz_doble(x):
    return np.power(x - 2, 2)


def derivada_primera(x):
    return 2 * (x - 2)


def derivada_segunda(x):
    return 2.0  #QUEDA LA CONSTANTE


def newton_rapeador_son(punto_inicial, tolerancia, iteraciones):
    punto_funcion = funcion_raiz_doble(punto_inicial)
    punto_deri_1 = derivada_primera(punto_inicial)
    punto_deri_2 = derivada_segunda(punto_inicial)
    pass


if __name__ == "__main__":
    punto_inicial = 1.2
    tolerancia = 1e-6
    iteraciones = 100
    raiz, iters, lista_errores = newton_rapeador_son(punto_inicial, tolerancia, iteraciones)
