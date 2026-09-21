### **Métodos útiles para Listas**

#Las listas son colecciones mutables y cuentan con una variedad de métodos integrados para manipular sus elementos directamente en memoria[1][2]:

#* **.append(x)** **:** Añade un elemento al final de la lista[2].
#* **.insert(i, x)** **:** Inserta el elemento `x` en la posición del índice `i`[2].
#* **.remove(x)** **:** Elimina la primera aparición del valor `x` (lanza `ValueError` si no existe)[2].
#* **.pop([i])** **:** Elimina y **retorna** el elemento en el índice `i`. Si no se indica el índice, elimina y devuelve el último[2].
#* **.sort()** **y** **.reverse()** **:** Ordenan o invierten los elementos directamente en la lista original[2].

#&gt; ⚠️ **Regla de oro de Python:** Todos los métodos que modifican listas directamente en memoria (*in-place*), como `.sort()` o `.reverse()`, devuelven por defecto el valor especial `None`[2][3]. 
# Por eso **no debes hacer** `lista = lista.sort()`, ya que borrarías tu lista guardando un `None`.

### **Comprensión de Listas (** **List Comprehensions** **)**

#Esta es una de las características más elegantes y queridas de Python. Te permite crear nuevas listas en **una sola línea de código** a partir de otras secuencias, evitando escribir bucles `for` 
# tradicionales de varias líneas[4][5].

#### **Sintaxis básica:**

#```
#[expresion for elemento in secuencia if condicion]
#``` [4]

#### **Comparación práctica:**

#Imagina que quieres filtrar los números pares de una lista:

#* **Forma tradicional con `for`:**
#  ```python
#  numeros = [1, 6-10]
#  pares = []
#  for x in numeros:
#      if x % 2 == 0:
#          pares.append(x)
#  ``` [5]

#* **Con List Comprehension (¡en 1 sola línea!):**
#  ```python
#  numeros = [1, 6-10]
#  pares = [x for x in numeros if x % 2 == 0]
#  ``` [5]

### **Desafío 🏆**

#Escribe una **List Comprehension** en **una sola línea**[1][2] para crear una nueva lista llamada `precios_altos` que contenga solo los precios mayores o iguales a $3.000 CLP 
# (`&gt;= 3000`)[2].

#Recuerda la estructura básica: `[expresion for elemento in secuencia if condicion]`

lista_precios = [2000, 3000, 15000, 1700, 45000, 3001, 2999]

precios_altos = [precios for precios in lista_precios if precios >= 3000]

print(precios_altos)