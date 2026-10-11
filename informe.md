El informe debe responder, con sus propios datos y gráficos:
-¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?
-¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?
-¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?
-En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor? ¿Por qué?
-¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?
-¿Qué método recomiendan según el tipo de función, considerando el compromiso entre velocidad y robustez?

RESPUESTAS:

1.- El metodo que convergió más rapido fue Newton Raphson Mejorado ejecutado con la función de raiz doble f(x) = (x − 2)², se encontró la raiz en 1 iteracion siendo la raíz 2.0 y el porque de esto es que al desarrollar la segunda iteracion se topa con la situacion de division por 0 a la hora de conocer el nuevo punto.


2.- Los ordenes de convergencia son lineal (bisección, falsa posición, punto fijo), superlineal (secante ≈ 1,618) y cuadrático (Newton y Newton mejorado en raíces simples).

El informe.md debe cerrar con una conclusión argumentada que responda:
-¿Qué método elegirían para cada tipo de función y por qué (velocidad vs robustez)?
-¿Qué ocurrió en la raíz doble y qué dice eso sobre «tener raíz» frente a «cambiar de signo»?
-¿Cómo cambió el número de iteraciones al mover el intervalo o la estimación inicial?
La conclusión debe apoyarse en los números y gráficos obtenidos, no en la intuición.
