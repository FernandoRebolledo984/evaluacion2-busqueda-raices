#Polinomica simple
import numpy as np

def f_poli_simple(x):
        return x**3 - x - 2

def biseccion(f, a, b, tol, max_iter):
    """
    Encuentra la raíz de f(x) en el intervalo [a, b] usando bisección.
    Retorna la raíz, la cantidad de iteraciones y una lista con los errores.
    """
    # Validar el cambio de signo inicial (Teorema de Bolzano)
    if f(a) * f(b) >= 0:
        print("Error: No hay cambio de signo en el intervalo dado.")
        return None, 0, []

    iteracion = 0
    error_actual = tol + 1 # Inicializar un error mayor a la tolerancia
    errores = []           # Lista para guardar el error por iteración (útil para graficar después)
    c_old = a              # Para calcular el error |x_i - x_{i-1}|

    while error_actual > tol and iteracion < max_iter:
        # Calcular el punto medio
        c = (a + b) / 2.0
        
        # Calcular el error (diferencia entre el c actual y el anterior)
        if iteracion > 0:
            error_actual = np.abs(c - c_old)
            errores.append(error_actual)
            
        # Actualizar el intervalo
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
            
        c_old = c
        iteracion += 1

    return c, iteracion, errores


if __name__ == "__main__":
    pass

    intervalo_a = 1.0
    intervalo_b = 2.0
    tolerancia = 1e-6
    iteraciones = 100
    print("--- MÉTODO DE BISECCIÓN ---")
    raiz, iters, lista_errores = biseccion(f_poli_simple, intervalo_a, intervalo_b, tolerancia, iteraciones)
    if raiz is not None:
        print(f"Raíz encontrada: {raiz:.6f}")
        print(f"Iteraciones necesarias: {iters}")
        print(f"Error final: {lista_errores[-1]:.2e}" if lista_errores else "Error final: 0")