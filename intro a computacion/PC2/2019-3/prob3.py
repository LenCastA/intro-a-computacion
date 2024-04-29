p = int(input('Cuántas personas como máximo entran en el ascensor?: '))
w = int(input('Cuántas kilos como máximo soprta el ascensor?: '))
n =int(input('Cuántas personas hay en cola (<=5)?: '))
pesos = []

if n <= 5:
    for i in range(1,n+1):
        peso = float(input(f'Introduzca el peso de la persona {i}: '))
        pesos.append(peso)

viajes = 0
personasEnViaje = 0
pesoEnViaje = 0

for peso in pesos:
    if personasEnViaje < p and pesoEnViaje + peso <= w:
        personasEnViaje += 1
        pesoEnViaje += peso
    else:
        viajes += 1
        personasEnViaje = 1
        pesoEnViaje = peso

viajes += 1

print(f"La cantidad de viajes que realizará el ascensor será {viajes}.")