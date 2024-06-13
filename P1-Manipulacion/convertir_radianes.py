import math

def print_angulos(lista_normalizada):
    for i in lista_normalizada:
        print(i, end= ' ')
    print()

def rango(lista_radianes):
    lista_normalizada = []
    for i in lista_radianes:
        angulo_normalizado = i % (2 * math.pi)
        if angulo_normalizado > math.pi:
            angulo_normalizado -= 2 * math.pi
        lista_normalizada.append(angulo_normalizado)
    return lista_normalizada

def grados_radianes(lista_grados):
    lista_radianes = []
    for i in lista_grados:
        radianes = i * math.pi / 180
        lista_radianes.append(radianes)
    return lista_radianes


if __name__ == '__main__':
    grados = dict() # Contiene listas con los grados

    for key, value in grados.items():
        lista_normalizada = rango(grados_radianes(value))
        print(key)
        print(lista_normalizada)