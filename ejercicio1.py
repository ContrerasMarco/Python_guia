#print("hola mundo")
#Ejercicio Teórico (Comprensión Lógica)
#imagina que estás ejecutando código en tu intérprete de Python. Analiza las siguientes tres operaciones y dime qué tipo de dato devolverá cada una (int o float) y cuál será su valor final:
#resultado_a = 20 // 4 entero
#resultado_b = 20 / 4 flot
#resultado_c = 15 % 4 el residuo de la operacion

#. Ejercicio Práctico (Escritura de Código)
#escribe un pequeño programa (unas pocas líneas de código en Python) que resuelva la siguiente situación de la vida real:
#tenes un presupuesto total de 150 dólares. Vas a comprar videojuegos que cuestan 40 dólares cada uno.
#crea na variable llamada presupuesto con el valor inicial.
#crea una variable llamada costo_juego con el valor de cada juego.
#calcula cuántos juegos completos puedes comprar (sin decimales) y guárdalo en una variable llamada juegos_comprados.
#calcula cuánto dinero te sobrará después de hacer esa compra y guárdalo en una variable llamada dinero_restante.
#muestra ambos resultados en pantalla.

# Definimos el presupuesto disponible y el costo de cada videojuego
presuesto=150
costo_juego=40
# Calculamos la cantidad máxima de juegos completos que podemos comprar
juegos_comprados = presuesto // costo_juego
# Calculamos el vuelto o dinero sobrante usando el operador residuo (módulo)
dinero_restante = presuesto % costo_juego
# Mostramos los resultados en la terminal
print(juegos_comprados)
print(dinero_restante)
