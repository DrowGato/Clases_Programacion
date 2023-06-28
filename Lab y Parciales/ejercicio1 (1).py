###A###
print("Acatividad A")
tabla_regiones= {
    " Id:14 ": { " Nombre" : "Los Ríos", "Superficie ":18429, "Habitantes":404432},
    " Id:12 ": { " Nombre" : "Magallanes", "Superficie ":1382291, "Habitantes":166533}
}
print(tabla_regiones)


###B###
print("Actividad B")
regiones = {
    "Los Ríos": {"Superficie": 18429, "Habitantes": 404432},
    "Magallanes": {"Superficie": 1382291, "Habitantes": 166533}
}


for region in regiones:
    habitantes = regiones[region]["Habitantes"]
    superficie = regiones[region]["Superficie"]
    densidad = round(habitantes / superficie, 1)
    regiones[region]["Densidad"] = densidad
print(regiones)


###C###
print("Actividad C")
Capital= {
    " Capital ": {"Valdivia","region",14},
    " Capital ": {"Punta arenas","region",12}
}
print(Capital)






###F###
print("Actividad F")
my_dict = {
    'ID': [14, 12],
    'Región': ['Los Ríos', 'Magallanes'],
    'Nombre': ['Valdivia', 'Punta Arenas'],
    'Superficie (Km2)': [18429, 1382291],
    'Habitantes (Año 2017)': [404432, 166533],
    'Densidad': [21.93,"Y", 0.12],
    'Capital': ['Valdivia', 'Punta Arenas'],
    'Comunas': [['Ranco', 'Valdivia', 'Río Bueno', 'La Unión', 'Paillaco'], ['Antártica Chilena', 'Magallanes', 'Tierra del Fuego', 'Última Esperanza']],
    'Provincia': [('Ranco', 'Valdivia'), ('Antártica Chilena', 'Magallanes', 'Tierra del Fuego', 'Última Esperanza')]
}
print("lista de todos los Datos",my_dict)