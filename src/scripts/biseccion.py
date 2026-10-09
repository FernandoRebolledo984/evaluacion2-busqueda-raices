#Polinomica simple
import numpy as np
from main import tolerancia
from main import iteraciones

#PREPARA LA FUNCION POLINOMICA SIMPLE ELEGIDA PARA ESTE METODO
def polinomio(x):
    return x**3 - x - 2

def biseccion(intervalo_a, intervalo_b, tolerancia, iteraciones):
    a_evaluado = polinomio(intervalo_a)
    b_evaluado = polinomio(intervalo_b)
    comprobacion = comprobacion_de_raiz(a_evaluado, b_evaluado)
    if (comprobacion)<0:
        print("Hay raíz en este intervalo :)")

    else:
        print("No existe raíz aqui :(")
    


def comprobacion_de_raiz(a_evaluado, b_evaluado):
    comprobacion = a_evaluado * b_evaluado
    return comprobacion



if __name__ == "__main__":
    pass
    #DECLARACION DE INTERVALOS Y LLAMADO A EL METODO CON RETORNO DE DATOS PEDIDOS PARA GARFICO
    intervalo_a = 1.0
    intervalo_b = 2.0
    raiz, iters, lista_errores = biseccion(intervalo_a, intervalo_b, tolerancia, iteraciones)
