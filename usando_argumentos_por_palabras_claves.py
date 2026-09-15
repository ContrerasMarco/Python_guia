#```
#def describir_auto(marca, modelo):
#    return f"Auto: {marca} {modelo}"

#```

#Normalmente la llamaríamos por posición: `describir_auto("Toyota", "Corolla")`.

#Pero usando **argumentos por palabra clave**, ¡puedes pasarlos en el orden que quieras especificando su nombre!:

##```
# ¡Cambiamos el orden y sigue funcionando perfecto!
#print(describir_auto(modelo="Corolla", marca="Toyota"))

#```

#### **Regla de oro de Python:**

#Si mezclas argumentos normales (posicionales) con argumentos por palabra clave, **los argumentos posicionales siempre deben ir primero**.

#* `describir_auto("Toyota", modelo="Corolla")` ➔ **Correcto**
#* `describir_auto(marca="Toyota", "Corolla")` ➔ **Error de sintaxis (SyntaxError)**

### **Desafío 🏆**

#Imagina que creamos una función para calcular el costo de estacionamiento pasando las `horas` y la `tarifa_hora`:

#```
#def calcular_estacionamiento(horas, tarifa_hora=2000):  
#    total = horas * tarifa_hora
#    return f"Total a pagar por {horas} hrs: ${total} CLP"

#```

#Quiero que llames a esta función usando **argumentos por palabra clave** (por ejemplo cambiando el orden o especificando 
# los nombres `tarifa_hora=` y `horas=`) e imprimas el resultado.

def calcular_estacionamiento(horas, tarifa_hora=2000):  
    total = horas * tarifa_hora
    return f"Total a pagar por {horas} hrs: ${total} CLP"


print(calcular_estacionamiento(tarifa_hora=2000, horas=2))