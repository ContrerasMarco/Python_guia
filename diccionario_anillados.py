#* Crea un diccionario llamado **estacionamiento** que contenga 2 casillas como claves principales:

#* `"casilla_1"` ➔ debe tener adentro el diccionario: `{"patente": "AA123BB", "horas": 2}`
#* `"casilla_2"` ➔ debe tener adentro el diccionario: `{"patente": "CC456DD", "horas": 5}`

#* **Modificación:** El auto de la `"casilla_1"` se quedó una hora extra. Accede a las horas de la `"casilla_1"` y súmale 1 hora (debe pasar de 2 a 3).

#*(Pista para acceder a un diccionario anidado:* *estacionamiento["casilla\_1"]["horas"]* *)*.

#* **Agregar un nuevo elemento:** Agrega una nueva casilla al diccionario principal llamada `"casilla_3"` con el valor `{"patente": "EE789FF", "horas": 1}`.
#* Imprime el diccionario **estacionamiento** completo para verificar la estructura final.

estacionamiento = {
    "casilla1": {"patente": "AA123BB", "horas": 2}, 
    "casilla2": {"patente":"CC456DD", "horas": 5}
    }

estacionamiento["casilla1"]["horas"] =3
estacionamiento["casilla3"]= {"patente": "EE789FF", "horas": 1}

print(estacionamiento)
#print(estacionamiento["casilla1"])
#print(estacionamiento["casilla2"])