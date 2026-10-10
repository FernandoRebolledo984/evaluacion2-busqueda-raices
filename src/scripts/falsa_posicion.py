#Mixta f(x) = √x − cos(x)
import numpy as np


def funcion_mixta(x):
    return np.sqrt(x) - np.cos(x)


def falsa_posicion(intervalo_a, intervalo_b, tolerancia, iteraciones):
    a_evaluado = funcion_mixta(intervalo_a)
    b_evaluado = funcion_mixta(intervalo_b)
    comprobacion = comprobacion_de_raiz(a_evaluado, b_evaluado)
    if(comprobacion < 0):
        iteracion_actual = 0
        error_actual = tolerancia + 1
        lista_errores = []
        xr_anterior = intervalo_a
        while(error_actual > tolerancia and iteracion_actual < iteraciones):
            xr_actual = xr_falsa_posicion(intervalo_a, intervalo_b, a_evaluado, b_evaluado)
            error = error(xr_actual, xr_anterior)

    
def comprobacion_de_raiz(a_evaluado, b_evaluado):
    comprobacion = a_evaluado * b_evaluado
    return comprobacion


def xr_falsa_posicion(intervalo_a, intervalo_b, a_evaluado, b_evaluado):
    # Fórmula: xm = b - (f(b) * (b - a)) / (f(b) - f(a))
    numerador = b_evaluado * (intervalo_b - intervalo_a)
    denominador = b_evaluado - a_evaluado
    xm = intervalo_b - (numerador / denominador)
    return xm


def error(xr_actual, xr_anterior):
    pass


if __name__ == "__main__":
    pass
    #DECLARACION DE INTERVALOS Y LLAMADO A EL METODO CON RETORNO DE DATOS PEDIDOS PARA GARFICO
    intervalo_a = 0.1
    intervalo_b = 1.0
    tolerancia = 1e-6
    iteraciones = 100
    raiz, iters, lista_errores = falsa_posicion(intervalo_a, intervalo_b, tolerancia, iteraciones)