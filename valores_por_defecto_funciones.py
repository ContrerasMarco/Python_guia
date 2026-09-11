#Valores por defecto en parámetros (Sección 4.8 / 4.9.1)

#Ahora demos el paso que dejamos pendiente: ¿Qué pasa si alguien llama a tu función saludo() sin pasarle ningún nombre dentro de los paréntesis? En Python, 
#si un parámetro es obligatorio y no se lo pasas, el programa se detiene con un error (TypeError).
#Para evitar esto, podemos asignarle un valor por defecto en la misma línea donde definimos la función

#def saludo(nombre="Amigo"):
#    bienvenida = f"Hola {nombre}, Bienvenido a python"
#    return bienvenida

#¿Cómo funciona esto?

#Si ejecutas saludo("Marco"), la variable nombre tomará el valor "Marco".
#Si ejecutas saludo(), la variable nombre usará automáticamente el valor por defecto "Amigo".

#tu Desafío 🏆

#Modifica tu código para asignarle un valor por defecto al parámetro nombre (el que tú prefieras, como "Amigo" o "Usuario").
#Luego, llama a la función dos veces en tu script:
#Una primera vez pasándole tu nombre: saludo("Marco").
#Una segunda vez sin pasarle nada: saludo().
#Imprime ambos resultados en la consola para ver la magia.

def saludo(nombre="Hermano"):
    bienvenida = f"Hola {nombre}, Bienvenido a python"
    return bienvenida



bienvenida = saludo("David")
#bienvenida = saludo()
print(bienvenida)
