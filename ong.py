#definicion de funciones
def fact_(n):
    return 1 if (n == 1 or n == 0) else n * fact_(n - 1)

def prod_(lista):
    paso = 1
    for nu in lista:
        paso = paso * nu
    return paso

#calculos con multiples argumentos
def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if "fact" in clave:
            print(f"El factorial de {valor} es {fact_(valor)}")
        elif "prod" in clave:
            print(f"La productoria de {valor} es {prod_(valor)}")


calcular(
    fact_1 = 5 , prod_1 = [4,6,7,4,3] , fact_2 = 6
)