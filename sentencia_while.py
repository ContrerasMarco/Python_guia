#. Ejercicio Teórico (La lógica del while)
#aliza el siguiente código y dime:
#Qué imprimirá exactamente en pantalla?
#Por qué se detiene el bucle?

# x = 5 #e declara variable inicializando en 5
# while x: #mientras la condicion sea verdadera el ciclo se inicia
 #   print(x, end=' ') #imprime en forma horinzontal cada elemento 
  #  x = x - 1 #cada vez que se cumple toda la condicion al valor de entrada se le resta 1

#este pedazo de codigo imprimira primero el 5 luego el 3, el 2, el 1 y cuando llegue al0 el ciclo se habra cumplido pero no lo va a mostrar por pantalla

#. Ejercicio Práctico (Asignación y Bucle)

#scribe un pequeño programa en Python que resuelva la siguiente tarea de automatización:
#ienes una variable limite = 100. Escribe un bucle while que imprima todos los números que sean múltiplos de 15 que se encuentren entre el 1 y el 100, ordenados horizontalmente y 
# separados por un guion medio (-).
#ista 1: Puedes usar el operador módulo % para saber si un número es múltiplo de 15 (si numero % 15 == 0, entonces es múltiplo).
#ista 2: Utiliza el parámetro end en tu print() para que los números salgan horizontales y separados por '-'.


limite = 15
while limite < 100:
    limite % 15 == 0
    print(limite, end='-')
    limite = limite + 15

