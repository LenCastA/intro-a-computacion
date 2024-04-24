p = int(input('Cuántas personas como máximo entran en el ascensor?: '))
w = int(input('Cuántas kilos como máximo soprta el ascensor?: '))
n =int(input('Cuántas personas hay en cola (<=5)?: '))
pesos = []

if n <= 5:
    for i in range(0,n+1):
        peso = float(input(f'Introduzca el peso de la persona {i}'))
        pesos.append(peso)

