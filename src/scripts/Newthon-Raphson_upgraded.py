#Raíz doble f(x) = (x − 2)²
import numpy as np
import os
import matplotlib.pyplot as plt


def funcion_raiz_doble(x):
    return np.power(x - 2, 2)


def derivada_primera(x):
    return 2 * (x - 2)


def derivada_segunda(x):
    return 2.0  #QUEDA LA CONSTANTE

#DESARROLLO ENTERO DE NEWTON RAPHSON MEJORADO
def newton_rapeador_son(punto_actual, tolerancia, iteraciones):
    iteracion_actual = 0
    error_actual = tolerancia + 1
    lista_errores = []
    while (error_actual > tolerancia and iteracion_actual < iteraciones):
        punto_funcion = funcion_raiz_doble(punto_actual)
        punto_deri_1 = derivada_primera(punto_actual)
        punto_deri_2 = derivada_segunda(punto_actual)
        numerador = punto_funcion * punto_deri_1
        denominador = np.power(punto_deri_1, 2) - punto_funcion * punto_deri_2
        if denominador == 0:
            print("Se está diviendo por 0 :(")
            return punto_actual, iteracion_actual, lista_errores  
        else:
            nuevo_punto = punto_actual - (numerador/denominador)
            error_actual = comprobar_error(punto_actual, nuevo_punto)
            lista_errores.append(error_actual)
            punto_actual = nuevo_punto  
            iteracion_actual += 1       
    return punto_actual, iteracion_actual, lista_errores  

#CRITERIO DE PARADA
def comprobar_error(x_actual, x_anterior):
    return np.abs(x_actual - x_anterior)


if __name__ == "__main__":
    punto_inicial = 1.2
    tolerancia = 1e-6
    iteraciones = 100
    raiz, iters, lista_errores = newton_rapeador_son(punto_inicial, tolerancia, iteraciones)
    if raiz is not None:
            print(f"\nRESULTADOS")
            print(f"Raíz aproximada: {raiz}")
            print(f"Iteraciones necesarias: {iters}")
            print(f"Error final: {lista_errores[-1]}")
    x_vals = np.linspace(0.0, 4.0, 200)
    y_vals = funcion_raiz_doble(x_vals)
        
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x) = (x - 2)²", color='aqua')
        
    plt.axhline(0, color='black', linewidth=1)
        
    plt.scatter([raiz], [0], color='red', zorder=5, label=f"Raíz = {raiz:.5f}")
        
    plt.title("Método de Newton-Raphson Mejorado")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
        
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_graficas = os.path.abspath(os.path.join(directorio_script, '..', 'assets'))
    ruta_guardado = os.path.join(ruta_graficas, 'grafica_newton_mejorado.png')

    os.makedirs(ruta_graficas, exist_ok=True)
    plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')

    
