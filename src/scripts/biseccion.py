#Polinomica simple
import numpy as np
from main import tolerancia
from main import iteraciones

#PREPARA LA FUNCION POLINOMICA SIMPLE ELEGIDA PARA ESTE METODO
def f_poli_simple(x):
        return x**3 - x - 2

def biseccion(f, a, b, tol, max_iter):
    pass


if __name__ == "__main__":
    pass
    #DECLARACION DE INTERVALOS Y LLAMADO A EL METODO CON RETORNO DE DATOS PEDIDOS PARA GARFICO
    intervalo_a = 1.0
    intervalo_b = 2.0
    raiz, iters, lista_errores = biseccion(f_poli_simple, intervalo_a, intervalo_b, tolerancia, iteraciones)
