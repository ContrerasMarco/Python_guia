#Ejemplo práctico 🚗
#Imagina que creamos una función para calcular el cobro de tu estacionamiento en pesos chilenos:
#def calcular_cobro(horas):
#    """Calcula el total a pagar a $2.000 CLP por hora."""
#    tarifa_por_hora = 2000
#    total = horas * tarifa_por_hora
#    return total

# Ahora la usamos (la llamamos) con distintas horas:
#pago1 = calcular_cobro(3)  # Devuelve 6000
#pago2 = calcular_cobro(5)  # Devuelve 10000

#print("El cliente 1 debe pagar:", pago1, "pesos")
#print("El cliente 2 debe pagar:", pago2, "pesos")

#Desafío de Funciones 🏆

#Para dar tu primer paso creando tus propias funciones, te propongo escribir una función llamada saludar_usuario.

#Requisitos de la función:

#Debe recibir un parámetro llamado nombre.
#Debe retornar (return) el mensaje de texto: "¡Hola " + nombre + ", bienvenido a Python!".
#Fuera de la función, llama a saludar_usuario("Marco"), guarda el resultado devuelto en una variable e imprímela en la consola con print().

def saludo(nombre):
    bienvenida = f"Hola {nombre}, Bienvenido a python"

    return bienvenida

saludo_bievenida=saludo("Marco")
print(saludo_bievenida)