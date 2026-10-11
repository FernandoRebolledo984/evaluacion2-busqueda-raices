#Mixta f(x) = √x − cos(x)
import numpy as np
import os
import matplotlib.pyplot as plt


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
            error_actual = comprobar_error(xr_actual, xr_anterior)
            if iteracion_actual > 0:
                lista_errores.append(error_actual)
            comprobacion_fronteras = fronteras(xr_actual, a_evaluado)
            if comprobacion_fronteras == 0:
                break
            elif comprobacion_fronteras > 0:
                intervalo_a = xr_actual
                a_evaluado = funcion_mixta(intervalo_a) # Actualizar a_evaluado
            else:
                intervalo_b = xr_actual
                b_evaluado = funcion_mixta(intervalo_b) # Actualizar b_evaluado
            
            xr_anterior = xr_actual
            iteracion_actual += 1

    return xr_actual, iteracion_actual, lista_errores

    
def comprobacion_de_raiz(a_evaluado, b_evaluado):
    comprobacion = a_evaluado * b_evaluado
    return comprobacion


def xr_falsa_posicion(intervalo_a, intervalo_b, a_evaluado, b_evaluado):
    # Fórmula: xm = b - (f(b) * (b - a)) / (f(b) - f(a))
    numerador = b_evaluado * (intervalo_b - intervalo_a)
    denominador = b_evaluado - a_evaluado
    xm = intervalo_b - (numerador / denominador)
    return xm


def comprobar_error(xr_actual, xr_anterior):
    error_actual = np.abs(xr_actual - xr_anterior)
    return error_actual


def fronteras(xr_actual, a_evaluado):
    xm_evaluado = funcion_mixta(xr_actual)
    comprobacion_comprobacionaria = a_evaluado * xm_evaluado
    return comprobacion_comprobacionaria


if __name__ == "__main__":
    #DECLARACION DE INTERVALOS Y LLAMADO A EL METODO CON RETORNO DE DATOS PEDIDOS PARA GARFICO
    intervalo_a = 0.1
    intervalo_b = 1.0
    tolerancia = 1e-6
    iteraciones = 100
    raiz, iters, lista_errores = falsa_posicion(intervalo_a, intervalo_b, tolerancia, iteraciones)
    if raiz is not None:
        print(f"\nRESULTADOS")
        print(f"Raíz aproximada: {raiz}")
        print(f"Iteraciones necesarias: {iters}")
        print(f"Error final: {lista_errores[-1]}")
    x_vals = np.linspace(0.0, 1.5, 200)
    y_vals = funcion_mixta(x_vals)
        
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x) = √x - cos(x)", color='aqua')
        
    plt.axhline(0, color='black', linewidth=1)
        
    #Marcar la raíz 
    plt.scatter([raiz], [0], color='red', zorder=5, label=f"Raíz = {raiz:.5f}")
        
    plt.title("Método Numérico - Falsa Posición")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
        
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_graficas = os.path.abspath(os.path.join(directorio_script, '..', 'assets'))
    ruta_guardado = os.path.join(ruta_graficas, 'grafica_falsa_posicion.png')

    os.makedirs(ruta_graficas, exist_ok=True)
    plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')