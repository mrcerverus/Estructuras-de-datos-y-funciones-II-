#Ingreso de variables en lista - contiene las velocidades
velocidad = [
    25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
    14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21
]
#calculo del promedio sin uso de librerias
promedio = sum(velocidad) / len(velocidad)
print(promedio)
#conversion de lista a diccionario - método enumarete como k
nuevaLista = dict(enumerate(velocidad))
#filtrado de diccionario sobre el promedio de velocidad
resultado = list({k : v for k , v in nuevaLista.items() if v > promedio})
#respuesta
print(f"Las maquinas con velocidades mayores al promedio ({promedio}) de velocidad son: \n")
print(resultado)