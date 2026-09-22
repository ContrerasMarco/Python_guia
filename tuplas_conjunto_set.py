### **Tuplas y Conjuntos (** **Sets** **) 🚀**

#Siguiendo nuestros apuntes y el Roadmap de MoureDev, las siguientes estructuras de datos clave son las **Tuplas** y los **Conjuntos**:

#1. **Tuplas (** **tuple** **):** Son colecciones ordenadas pero **inmutables** (no se pueden modificar una vez creadas)[1]. Se definen con paréntesis `()`
#  o simplemente separando valores con comas[1].

#2. **Conjuntos (** **set** **):** Son colecciones **desordenadas** que **no permiten elementos duplicados**[2]. Se definen con llaves `{}` y 
# son ideales para eliminar duplicados o hacer operaciones de conjuntos (unión, intersección, etc.)


### **Desafío rápido de Tuplas y Conjuntos 🏆**

#Imagina que recibes un listado de patentes ingresadas en el estacionamiento, pero por error algunas se registraron varias veces:

#patentes_registradas = ["AA123BB", "CC456DD", "AA123BB", "EE789FF", "CC456DD"]

#**Tu misión:**

#1. Crea un **conjunto (** **set** **)** a partir de esa lista para eliminar automáticamente las patentes duplicadas.

#2. Imprime el resultado para verificar cuántas patentes únicas quedan.

patentes_registradas = ["AA123BB", "CC456DD", "AA123BB", "EE789FF", "CC456DD"]

limpiar_registro = set(patentes_registradas)

print(limpiar_registro)