#Polinomica simple    f(x) = x^3 - x - 2  en [1, 2]
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
    #DECLARACION DE INTERVALOS Y LLAMADO A EL METODO CON RETORNO DE DATOS PEDIDOS PARA GRAFICO
    intervalo_a = 1.0
    intervalo_b = 2.0
    tolerancia = 1e-6
    iteraciones = 100

    # ======================================== AMBIENTE CONTROLADO (BOLZANO) ========================================
    fa = polinomio(intervalo_a)
    fb = polinomio(intervalo_b)
    print("\n\nMétodo de Bisección")
    print(f"f(a) = {fa:.6f}, f(b) = {fb:.6f}, f(a)*f(b) = {fa*fb:.6f}")

    raiz, iters, lista_errores = biseccion(intervalo_a, intervalo_b, tolerancia, iteraciones)

    if raiz is not None:
        print(f"\nRESULTADOS BISECCION")
        print(f"Raíz aproximada: {raiz}")
        print(f"Iteraciones necesarias: {iters}")
        if lista_errores:
            print(f"Error final: {lista_errores[-1]}")

        # ======================================== RUTAS ========================================
        directorio_script = os.path.dirname(os.path.abspath(__file__))
        ruta_graficas = os.path.abspath(os.path.join(directorio_script, '..', 'assets'))
        ruta_data = os.path.abspath(os.path.join(directorio_script, '..', 'data'))
        os.makedirs(ruta_graficas, exist_ok=True)
        os.makedirs(ruta_data, exist_ok=True)

        # ======================================== GRAFICA 1: FUNCION CON SU RAIZ ========================================
        x_vals = np.linspace(intervalo_a, intervalo_b, 200)
        y_vals = polinomio(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, color='blue', linewidth=2, label='f(x) = x³ - x - 2')
        plt.axhline(0, color='black', linewidth=1)  # eje x
        plt.plot(raiz, polinomio(raiz), 'ro', markersize=8, label=f'Raíz ≈ {raiz:.6f}')
        plt.title("Función polinómica con su raíz marcada", fontsize=14)
        plt.xlabel("x", fontsize=12)
        plt.ylabel("f(x)", fontsize=12)
        plt.grid(True, alpha=0.4)
        plt.legend()
        plt.savefig(os.path.join(ruta_graficas, 'raiz_biseccion.png'), dpi=300, bbox_inches='tight')
        plt.close()

        # ======================================== GRAFICA 2: CONVERGENCIA (ESCALA LOG) ========================================
        # El primer error se descarta, por eso la lista parte en la iteración 2
        eje_x_iteraciones = np.arange(2, len(lista_errores) + 2)

        plt.figure(figsize=(8, 5))
        plt.plot(eje_x_iteraciones, lista_errores, marker='o', color='blue', linewidth=2, label='Bisección')
        plt.axhline(tolerancia, color='red', linestyle='--', linewidth=1, label='Tolerancia')
        plt.yscale('log')
        plt.xticks(eje_x_iteraciones)  # una marca por iteración (enteros)
        plt.title("Convergencia del error - Bisección", fontsize=14)
        plt.xlabel("Iteración", fontsize=12)
        plt.ylabel("|Error| (escala log)", fontsize=12)
        plt.grid(True, which="both", linestyle='--', alpha=0.7)
        plt.legend()
        plt.savefig(os.path.join(ruta_graficas, 'convergencia_biseccion.png'), dpi=300, bbox_inches='tight')
        plt.close()

        # ======================================== ARCHIVO CSV (x, f(x)) ========================================
        ruta_csv = os.path.join(ruta_data, 'biseccion.csv')
        csv_datos = np.column_stack((x_vals, y_vals))
        np.savetxt(ruta_csv, csv_datos, delimiter=',', header='x,f(x)', comments='', fmt='%.8f')