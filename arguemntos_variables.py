### **1\.** **\*args** **(Argumentos Posicionales Variables)**

#El asterisco `*args` le dice a Python: *"Recibe todos los argumentos posicionales extra que te envíen y guárdalos dentro de una* **tupla** *"*[1].

#### **Ejemplo real:**

#Imagina una función que calcula el total a pagar de una compra, pero no sabe cuántos productos lleva el cliente en el carro (pueden ser 2, 5 o 10):

#```
#def sumar_precios(*precios):
#    # 'precios' es una tupla con todos los números pasados
#    total = sum(precios)
#    return f"Total a pagar: ${total} CLP"

# ¡Podemos pasarle la cantidad de precios que queramos!
#print(sumar_precios(1500, 2000))            # Total: $3500 CLP
#print(sumar_precios(1000, 500, 3000, 4500))  # Total: $9000 CLP
#```

#########################################################################################################################################################

### **2\.** **\*\*kwargs** **(Argumentos por Palabra Clave Variables)**

#Los dos asteriscos `**kwargs` le dicen a Python: *"Recibe todos los argumentos nombrados extra (* *nombre=valor* *) y guárdalos en un* **diccionario** *"*[1].

#### **Ejemplo real:**

#Imagina registrar los datos de un cliente o auto, donde algunos datos son opcionales:

#```
#def registrar_cliente(nombre, **datos_extra):
#    print(f"Cliente: {nombre}")
#    # 'datos_extra' es un diccionario con las parejas clave-valor
#    for clave, valor in datos_extra.items():
#        print(f" - {clave}: {valor}")

# Podemos agregar cualquier dato extra con nombre=valor
#registrar_cliente("Marco", auto="Toyota", casilla=2, estado="Pagado")
#```
##########################################################################################################################################################

### **Desafío Práctico 🏆**

#Para poner a prueba `*args`, escribe una función llamada **calcular\_promedio(\*notas)**.

#**Requisitos:**

#1. Debe recibir cualquier cantidad de notas numéricas usando `*args`.
#2. Debe calcular el promedio de esas notas (suma de notas dividido por la cantidad de notas `len(notas)`).
#3. Debe retornar el promedio.

#Llama a tu función pasándole 3 o 4 notas (por ejemplo: `7.0, 6.5, 5.0`) e imprime el resultado.

def calcular_notas(*notas):
    promedio =sum( notas)/ len(notas)
    return f"el promedio del alumno es : {promedio}"

print(calcular_notas(7.0, 6.8, 4.8))

### **Desafío de** **\*\*kwargs** **🚗**

#Ahora vamos con el ejercicio para dominar **\*\*kwargs** (argumentos por palabra clave variables)[1].

#Recuerda que `**kwargs` empaqueta todos los datos nombrados (`clave=valor`) que le pases a la función dentro de un **diccionario**[1]. Para recorrer 
# las parejas clave-valor de un diccionario en un bucle `for`, tus apuntes sugieren usar el método `.items()`[2].

#### **Desafío: Registro de Vehículos**

#Crea una función llamada **registrar\_auto(patente, \*\*detalles)**:

#1. Debe recibir la `patente` como parámetro obligatorio[1].
#2. Debe recibir cualquier cantidad de información extra usando **\*\*detalles** (como `marca="Toyota"`, `color="Azul"`, `ano=2024`)[1].
#3. Dentro de la función:
#  * Imprime: `f"--- Auto Patente: {patente} ---"`
#  * Usa un bucle `for clave, valor in detalles.items():` para imprimir cada detalle adicional[2].
#4. Prueba llamar a la función pasándole la patente y al menos 2 o 3 datos extra con el formato `nombre=valor`.

def registrar_patentes(patente, **detalles):

    print(f"La patente registrada es {patente}")

    for detalles_extras, mas_detalles  in detalles.items():
        print (f"Los detalles del auto son : {detalles_extras} - {mas_detalles}")

registrar_patentes("aaee-98", marca="suzuki", color="azul", tipo="van")        
