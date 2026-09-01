#1. Ejercicio Teórico (Análisis de Memoria)
#"Analiza el siguiente fragmento de código paso a paso y dime qué imprimirá la terminal al final:
original = [10, 20, 30] #lista original
alias = original #copia de la lista original por nombre y apunta al mismo sector de memoria
copia = original[:] #copia real de la lista original.

alias.append(40) #a la copia por nombre se le agrega un nuevo elemento (40) 
copia.append(50) #a la copia real se le asigna otro elemento (50)

print("Original:", original)#imprime 10,20,30,40
print("Copia:", copia)#imprime 10,20,30,50

#2. Ejercicio Práctico (Manipulación de tu Estacionamiento)

#Escribe un pequeño programa en Python para resolver este prototipo:
#Crea una lista llamada estacionamiento con tres patentes iniciales: "AA-11", "BB-22", "CC-33".
#Un auto con la patente "DD-44" ingresa. Agrégalo al final de la lista usando el método correspondiente.
#El primer auto ("AA-11") paga y se retira. Modifica el valor de la primera posición para que ahora diga "Vacio".
#Muestra la lista final usando print().

estacionamiento = ["AA-11", "BB-22","CC-33"]
estacionamiento.append("DD-44")
estacionamiento.remove("AA-11")# alternativa de codigo estacionamiento ="Vacio"
estacionamiento.insert(0, "Vacio") #al hacer la liena de codigo de arriba comentada esta linea no deberia usarse
print(estacionamiento)

