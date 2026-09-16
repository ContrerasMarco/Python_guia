###   **Parámetros Especiales (** **/** **y** **\*** **)**

#Siguiendo el orden oficial de la **Unidad 4**, la documentación muestra cómo restringir la forma en que un usuario pasa los argumentos a tus funciones[1].

#Python incluye dos símbolos especiales dentro de la lista de parámetros para definir estas reglas[1]:

#1. **La barra diagonal (** **/** **) — Solo Posicionales:** Todos los parámetros definidos **antes** de la barra `/` deben pasarse obligatoriamente por posición[1]. Intentar pasarlos con `nombre=valor` lanzará un error (`TypeError`)[1].
#2. **El asterisco (** **\*** **) — Solo Palabra Clave:** Todos los parámetros definidos **después** del asterisco `*` deben pasarse obligatoriamente escribiendo su nombre[1].

#### **Mira la estructura completa:**

#```
#def mi_funcion(pos_solamente, /, libre, *, clave_solamente):
#    print(pos_solamente, libre, clave_solamente)

#```

#* **pos\_solamente**: Obligado por posición (no acepta `pos_solamente=1`).
#* **libre**: Flexible (se puede pasar como `2` o como `libre=2`).
#* **clave\_solamente**: Obligado por nombre (requiere `clave_solamente=3`).

#### **Llamada válida:**

#```
#mi_funcion(1, 2, clave_solamente=3)
#```

### **Creador de Tickets 🎟️**

#Crea una función llamada **crear\_ticket** que cumpla con las siguientes reglas de parámetros:

#1. **id\_ticket**: Debe ser **únicamente posicional** (debe ir antes de `/`)[1].
#2. **tipo**: Puede ser libre (posicional o por palabra clave), con un valor por defecto de `"Estándar"`.
#3. **total**: Debe ser **únicamente por palabra clave** (debe ir después de `*`)[1].

#Inside the function, return an f-string with a format like: `f"Ticket N°{id_ticket} [{tipo}] - Total: ${total} CLP"`

#---

### **Tu misión en el código:**

#* Define la función con los símbolos `/` y `*` colocados correctamente.
#* Llama a la función de forma **válida** (por ejemplo: `crear_ticket(101, total=5000)`).
#* *(Opcional)* Intenta hacer una llamada incorrecta (como poner `id_ticket=101`) para comprobar cómo Python te protege de cometer un error de llamadas.

def crear_ticket(id_ticket, /, tipo="Estandar", *, total):

    return (f"El ticket n° {id_ticket} es de tipo {tipo} y el total es de {total}")

print(crear_ticket(123,total = 3000))
print(crear_ticket(123,"VIP",total = 3000))
print(crear_ticket(123))


