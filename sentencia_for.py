#El Reto de la Unidad 4 🏆
#
# Para ver cómo funciona esto en tus manos antes de seguir con las funciones, hagamos un ejercicio muy rápido. Imagina que tienes esta lista con tus películas o series favoritas:
#favoritas = ["Matrix", "Inception", "Gladiador"]

#Quiero que escribas un mini código en tu editor que recorra esa lista utilizando un bucle for y range(), y que muestre en la consola un top numerado de esta forma:

#Puesto 0 : Matrix
#Puesto 1 : Inception
#Puesto 2 : Gladiador
#
# (Pista: recuerda usar len(favoritas) dentro de range() para que el rango se adapte automáticamente al largo de tu lista

listas_peliculas = ["Matrix", "Inception", "Gladiador"]

for pelis in range(len(listas_peliculas)):
    print("Puesto", pelis ,":", listas_peliculas[pelis])