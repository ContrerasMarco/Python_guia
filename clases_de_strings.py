#Tus Ejercicios de Clase (Unidad 3.1.2)
#Pongamos en práctica lo aprendido con tu teclado nuevo.
#1. Ejercicio Teórico (Análisis de Código)
#Imagina que tenemos la siguiente variable en Python:
materia = "Programacion"
#Analiza las siguientes operaciones lógicas y dime qué valor o qué error devolverá cada línea:
print(materia[0:4])
print(materia[-3:])
materia
 #= "g"

# 2. Ejercicio Práctico (Escritura de tu Script)
#Escribe un pequeño programa en Python para resolver este problema:
#Tu universidad te pide generar un "nombre de usuario" automático para los alumnos nuevos usando sus datos personales.
#Crea una variable llamada nombre con el valor "Carlos".
#Crea una variable llamada apellido con el valor "Mendoza".
#El nombre de usuario debe ser: la primera letra del nombre (en minúscula) seguida de las primeras tres letras del apellido (en minúscula). 
# (Pista: Para este ejercicio no te preocupes por convertir a minúsculas mediante métodos complejos si aún no los vemos, simplemente concatena rebanando las partes que necesitas directamente 
# si lo deseas, o si sabes cómo hacerlo, aplícalo).
#Une (concatena) las partes para formar la variable username y muéstrala en pantalla usando print().

#Declaracion de las variables pedidas.
nombre = "Carlos"
apellido = "Mendoza"

#Rebanando las variables para concatenar despues

nombre_usuario= nombre[0]  + apellido[0:3]

#imprimiendo el resultado pedido.
print(nombre_usuario.lower())

                                    


