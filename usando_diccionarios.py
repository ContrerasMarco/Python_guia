#Un diccionario almacena información en pares de **clave: valor**. Piensa en un diccionario real: buscas una palabra (**clave**) y encuentras su definición (**valor**).

#### **Sintaxis básica:**

# Se definen con llaves {} y dos puntos :
#auto = {
#    "patente": "AA123BB",
#    "marca": "Toyota",
#    "año": 2022
#}

# Acceder a un valor usando su clave:
#print(auto["marca"])  # Imprime: Toyota

# Agregar o modificar una clave:
#auto["color"] = "Azul"  # Agrega una nueva clave
#auto["año"] = 2024     # Modifica el valor existente


###########################################################################################################################################################################


### **Desafío de Diccionarios 🏆**

#Imagina que queremos guardar el estado de una casilla en nuestro estacionamiento:

#**Tu misión:**

#1. Crea un diccionario llamado **casilla** con las siguientes claves y valores:
#  * `"numero"` ➔ `10`
#  * `"ocupada"` ➔ `True`
#  * `"patente"` ➔ `"CC456DD"`
#2. Cambia el estado de `"ocupada"` a `False` (como si el auto se hubiera ido).
#3. Imprime el diccionario para ver el cambio.

casilla = {
    "numero":"10",
    "ocupada": True,
    "patente": "dddd45" 
}
casilla["ocupada"]= False
print(casilla["ocupada"])