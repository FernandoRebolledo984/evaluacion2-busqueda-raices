El informe debe responder, con sus propios datos y gráficos:
-¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?
-¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?
-¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?
-En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor? ¿Por qué?
-¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?
-¿Qué método recomiendan según el tipo de función, considerando el compromiso entre velocidad y robustez?

RESPUESTAS:

1.- El metodo que convergió más rapido fue Newton Raphson Mejorado ejecutado con la función de raiz doble f(x) = (x − 2)², se encontró la raiz en 1 iteracion siendo la raíz 2.0 y el porque de esto es que al desarrollar la segunda iteracion se topa con la situacion de division por 0 a la hora de conocer el nuevo punto.

2.- Los métodos de Bisección, Falsa Posición y Punto Fijo tienen convergencia lineal viendose como una recta diagonal descendente en el gráfico, el método de la Secante es superlineal, y los métodos de Newton son cuadráticos, lo que se ve como una curva cóncava que cae rapidamente hacia cero

3.- Los métodos que requieren un intervalo con cambio de signo son la Bisección y la Falsa Posición, mientras que Newton-Raphson (normal y mejorado), Punto Fijo y Secante no lo necesitan ya que son cerrados

4.-En la función de raíz doble fallan los métodos de Bisección y Falsa Posición porque al no cruzar el eje X no existe el cambio de signo que necesitan para funcionar, no como en Newton-Raphson Mejorado se comporta mejor, igualmente dando division por cero pero cortando ahi la iteracion, da la respuesta.

5.-S el intervalo o el valor inicial dado es mas lejano a la raiz, el metodo se vera envuelto en mas iteraciones y mas calculos lo que se traduce en más tiempo de convergencia. 

6.-Se recomienda Bisección para máxima robustez al asegurar siempre la convergencia, Newton-Raphson (Normal o Mejorado) para máxima velocidad si las derivadas son fáciles de calcular, y la Secante como el mejor equilibrio general porque es rápida y no requiere derivadas.

El informe.md debe cerrar con una conclusión argumentada que responda:
-¿Qué método elegirían para cada tipo de función y por qué (velocidad vs robustez)?
-¿Qué ocurrió en la raíz doble y qué dice eso sobre «tener raíz» frente a «cambiar de signo»?
-¿Cómo cambió el número de iteraciones al mover el intervalo o la estimación inicial?
La conclusión debe apoyarse en los números y gráficos obtenidos, no en la intuición.

RESPUESTAS:

1.-Elección de métodos: Elegiríamos Bisección si necesitamos asegurar el resultado sí o sí (robustez). Secante es un buen punto medio para evitar calcular derivadas, y Newton es el elegido si buscamos velocidad pura y derivar es fácil.

2.-Raíz doble y cambio de signo: La gráfica tocó el cero en el eje X pero rebotó. O sea, tiene raíz pero no cambia de signo. Esto demuestra por qué fallan los métodos de intervalo que obligan a cumplir la condición f(a) * f(b) < 0 y por qué tuvimos que usar Newton Mejorado.

3.-Cambio de iteraciones: Mientras más lejos pusimos el intervalo o el punto inicial, más iteraciones tardó el código en alcanzar la tolerancia exigida. Elegir un punto cercano desde el principio ahorra muchos cálculos.