x1 = float(input('Ingrese la coordenada x del primer punto: '))
y1 = float(input('Ingrese la coordenada y del primer punto: '))
x2 = float(input('Ingrese la coordenada x del segundo punto: '))
y2 = float(input('Ingrese la coordenada y del segundo punto: '))
x3 = float(input('Ingrese la coordenada x del tercer punto: '))
y3 = float(input('Ingrese la coordenada y del tercer punto: '))

dist12 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
dist23 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
dist13 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

if dist12 + dist23 == dist13:
    print('Los puntos son colineales')
else:
    print('Los puntos no son colineales')