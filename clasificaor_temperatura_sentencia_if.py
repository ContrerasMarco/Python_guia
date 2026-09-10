 #Ejercicio de la Sección 4.1 🏆
#Para dominar por completo esta sección antes de pasar a la siguiente, te propongo un ejercicio de lógica muy sencillo para tu consola.
#Imagina que estás programando un Clasificador de Temperaturas. Debes pedirle al usuario que ingrese la temperatura actual (como un número entero) y tu programa debe mostrar un mensaje según estas reglas:

#Si la temperatura es menor que 0, debe imprimir: "Hace un frío extremo".
#Si la temperatura es exactamente 0, debe imprimir: "Punto de congelación alcanzado".
#Si la temperatura está entre 1 y 15 (inclusive), debe imprimir: "El clima está frío".

#Para cualquier otra temperatura (mayor a 15), debe imprimir: "El clima está agradable".

#Pista: Recuerda usar int(input(...)) para convertir la entrada de texto a número entero, y utiliza 
# correctamente los comparadores <, ==, <=. o >=.

#Clasificador de tempratura

#pedirle al usuario que ingrese la temperatura

temperatura = int(input("Ingrese la temperatura " ":"))

if temperatura == 0:
    print("Punto de congelacion alcanzado")
elif temperatura < 0:
    print("Hace un frio extremo")
elif temperatura >= 1 and temperatura <= 15:
    print("El cima esta frio")      
elif temperatura > 15:
    print("El clima esta agradable")      