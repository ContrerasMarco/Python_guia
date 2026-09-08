#Mini Proyecto 1: El Tablero del Estacionamiento

#En este es tu primer proyecto de integración para consolidar el uso de listas, bucles y condicionales.

#El Desafío

#Crea un programa en consola que simule el estado de un estacionamiento para exactamente 4 autos (posiciones de la 0 a la 3).

#Especificaciones del Código:

#Inicialización: Crea una lista llamada lugares con 4 textos iniciales: ["Vacio", "Vacio", "Vacio", "Vacio"].

#Bucle Principal: Usa un bucle while para que el programa se ejecute continuamente.

#Visualización: Muestra en cada vuelta el estado actual del estacionamiento.

#Entradas (input()): Pide al operador ingresar una acción: "entrar", "salir" o "cerrar".

#Lógica:
#Si es "entrar": Pregunta el índice (0-3) y la patente del auto para guardarla.
#Si es "salir": Pregunta el índice (0-3) para reestablecerlo a "Vacio".
#Si es "cerrar": Termina el programa mostrando una despedida.

lugares = ["Vacio", "Vacio","Vacio","Vacio"]
programa_activo = True
while programa_activo:
    
    estado_patente = input("Ingrese el estado de la patente, 1.Entrar, 2.Salir, 3.Cerrar : ")
    if  estado_patente == "Entrar":
        indice_lista = input ("Ingrese el indice de numero desde 0 a 3 : ")
        indice = int(indice_lista)
        ingrese_patente = input("Ingrese la patente con el siguiente formato AA-00 : ")
        lugares[indice] = ingrese_patente
        #print(lugares)
    elif  estado_patente == "Salir":
        indice_lista = input ("Ingrese el indice de numero desde 0 a 3 : ")
        indice = int(indice_lista)
        lugares[indice] = "Vacio"
        #print(lugares)
       
    elif estado_patente == "Cerrar":
            print("Gracias por su visita")
            programa_activo=False

    if programa_activo:
        i=0
        while i < 4:
            print("El auto est aocupando la casilla", i , ":", lugares[i] )
            i=i+1





























































































