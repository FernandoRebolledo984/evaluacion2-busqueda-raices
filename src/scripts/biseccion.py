#Polinomica simple
import numpy as np
import os
import matplotlib.pyplot as plt


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
            #CÁLCULO DE ERROR
            error_actual = comprobar_error(xm, xm_anterior)
            if iteracion_actual > 0: # Evita guardar el primer error falso
                lista_errores.append(error_actual)
            a_evaluado_actual = polinomio(intervalo_a)
            evaluacion_fronteras = comprobar_fronteras(a_evaluado_actual, xm)
            if(evaluacion_fronteras == 0):
                print("Caiste justo en el 0")
                break
            elif(evaluacion_fronteras > 0):
                intervalo_a = xm
            else:
                intervalo_b = xm
            xm_anterior = xm
            iteracion_actual += 1
        return xm, iteracion_actual, lista_errores
    else:
        print("No existe raíz aqui :(")
        return None, 0, []


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


def comprobar_error(xm_actual, xm_anterior):
    error = np.abs(xm_actual - xm_anterior)
    return error


if __name__ == "__main__":
    #DECLARACION DE INTERVALOS Y LLAMADO A EL METODO CON RETORNO DE DATOS PEDIDOS PARA GARFICO
    intervalo_a = 1.0
    intervalo_b = 2.0
    tolerancia = 1e-6
    iteraciones = 100
    raiz, iters, lista_errores = biseccion(intervalo_a, intervalo_b, tolerancia, iteraciones)
    if raiz is not None:
        print(f"\nRESULTADOS")
        print(f"Raíz aproximada: {raiz}")
        print(f"Iteraciones necesarias: {iters}")
        print(f"Error final: {lista_errores[-1]}")

    # ======================================== GRAFICA ========================================
    x_val = np.linspace(0.5, 2.5, 200)
    y_val = polinomio(x_val)
        
    plt.figure(figsize=(8, 5))
    plt.plot(x_val, y_val, label="f(x) = x³ - x - 2", color='aqua')
        
    plt.axhline(0, color='black', linewidth=1)
        
    plt.scatter([raiz], [0], color='red', zorder=5, label=f"Raíz = {raiz:.5f}")
        
    plt.title("Método Numérico - Bisección")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
        
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_graficas = os.path.abspath(os.path.join(directorio_script, '..', 'assets'))
    ruta_guardado = os.path.join(ruta_graficas, 'grafica_biseccion.png')

    os.makedirs(ruta_graficas, exist_ok=True)
    plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')