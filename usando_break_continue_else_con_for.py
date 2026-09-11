#Desafío práctico 🏆
#Imagina que estás buscando un producto específico en una lista de inventario:
#inventario = ["manzana", "perra", "platano", "kiwi"]

#Escribe un programa con un bucle for que recorra la lista inventario:
#Si el producto es "platano", debe imprimir "¡Encontrado: platano!" y detener el bucle de inmediato usando break

#Mientras no sea el producto buscado, debe imprimir "Buscando...".

inventario = ["manzana", "pera", "platano", "kiwi"]

for producto in inventario:
    if producto =="platano":
        print("Has encontrado  : ", producto)
        break    
    else:
        print("Buscando")
        
