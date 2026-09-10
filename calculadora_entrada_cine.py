#Desafío: Calculadora de Entradas de Cine 🎬

#Imagina que estás programando el sistema de cobro automático para la boletería de un cine.
#  Tu programa debe pedirle al usuario su edad (como número entero) y calcular el precio de su 
# entrada según los siguientes rangos:

#Menores de 4 años (edad < 4): La entrada es Gratis ($0).
#Entre 4 y 17 años (ambos inclusive): Paga tarifa de Niño/Joven ($5).
#Entre 18 y 64 años (ambos inclusive): Paga tarifa de Adulto ($10).
#65 años o más (edad >= 65): Paga tarifa de Adulto Mayor ($6).

#logica programa

edad_cliente = int(input("Ingrese la edad del usuario " ":"))

if edad_cliente < 4:
    print("Puede ingresar gratis")
elif edad_cliente <=17:
    print("Su entrada es de niño/joven y debe pagar 5000 mil pesos")
elif edad_cliente <= 64:
    print("Su entrada es de adulto y sale 10000 mil pesos")
else:
    print("Su entrada es de adulto mayor y su entrada sale 6000 mil pesos")            