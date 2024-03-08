import sys

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

filtro = ""
separador = ", "

if len(sys.argv) < 3:
    umbral = int(sys.argv[1])
    pass
else:
    umbral = int(sys.argv[1])
    filtro = sys.argv[2]

def fil():
    if filtro == "mayor" or filtro == "":
        mayorUmbral = separador.join(list({k for k , v in precios.items() if v > umbral }))
        print(f"Los productos mayores al umbral son: {mayorUmbral}")
    elif filtro == "menor":
        menorUmbral = separador.join(list({k for k , v in precios.items() if v < umbral }))
        print(f"Los productos menores al umbral son: {menorUmbral}")
    else:
        print("Lo sentimos, no es una operación válida.")

#comienza filtro.py
fil()