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
        iteracion_actual = 0
        error_actual = tolerancia + 1
        lista_errores = []
        xm_anterior = intervalo_a
        while error_actual > tolerancia and iteracion_actual < iteraciones:
            xm = calcular_xm(intervalo_a, intervalo_b)

            # --- CÁLCULO DE ERROR ---
            error_actual = comprobar_error(xm, xm_anterior)
            if iteracion_actual > 0: # Evita guardar el primer error falso
                lista_errores.append(error_actual)
            
            # Es importante recalcular el a_evaluado porque el intervalo_a pudo haber cambiado
            a_evaluado_actual = polinomio(intervalo_a)
            evaluacion_fronteras = comprobar_fronteras(a_evaluado_actual, xm)
            
            if(evaluacion_fronteras == 0):
                print("xm es la raiz")
                break # Rompe el ciclo si la encuentra exacta
            elif(evaluacion_fronteras > 0):
                intervalo_a = xm
            else:
                intervalo_b = xm
            
            # Prepara la siguiente iteración
            xm_anterior = xm
            iteracion_actual += 1
            
        # --- RETURN NECESARIO PARA EVITAR EL ERROR EN LA LÍNEA 54 ---
        return xm, iteracion_actual, lista_errores
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


def comprobar_error():

    pass


if __name__ == "__main__":
    pass
    #DECLARACION DE INTERVALOS Y LLAMADO A EL METODO CON RETORNO DE DATOS PEDIDOS PARA GARFICO
    intervalo_a = 1.0
    intervalo_b = 2.0
    tolerancia = 1e-6
    iteraciones = 100
    raiz, iters, lista_errores = biseccion(intervalo_a, intervalo_b, tolerancia, iteraciones)
