#Polinomica simple
import numpy as np

#PREPARA LA FUNCION POLINOMICA SIMPLE ELEGIDA PARA ESTE METODO
def polinomio(x):
    return x**3 - x - 2


def biseccion(intervalo_a, intervalo_b, tolerancia, iteraciones):
    a_evaluado = polinomio(intervalo_a)
    b_evaluado = polinomio(intervalo_b)
    comprobacion = comprobacion_de_raiz(a_evaluado, b_evaluado)
    if (comprobacion)<0:
        print("Hay raíz en este intervalo :)")
        xm = calcular_xm(intervalo_a,intervalo_b)
        evaluacion_fronteras = comprobar_fronteras(a_evaluado, xm)
        if(evaluacion_fronteras == 0):
            print("xm es la raiz")
        elif(evaluacion_fronteras > 0):
            intervalo_a = xm
        else:
            intervalo_b = xm
    else:
        print("No existe raíz aqui :(")


def comprobacion_de_raiz(a_evaluado, b_evaluado):
    comprobacion = a_evaluado * b_evaluado
    return comprobacion


def calcular_xm(intervalo_a,intervalo_b):
    xm = (intervalo_b + intervalo_a)/2
    return xm


def comprobar_fronteras(a_evaluado, xm):
    xm_evaluado = polinomio(xm)
    comprobacion_comprobacionaria = a_evaluado * xm_evaluado
    return comprobacion_comprobacionaria

if __name__ == "__main__":
    pass
    #DECLARACION DE INTERVALOS Y LLAMADO A EL METODO CON RETORNO DE DATOS PEDIDOS PARA GARFICO
    intervalo_a = 1.0
    intervalo_b = 2.0
    tolerancia = 1e-6
    iteraciones = 100
    raiz, iters, lista_errores = biseccion(intervalo_a, intervalo_b, tolerancia, iteraciones)
