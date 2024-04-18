precios = []

for i in range(1,11):
    precioPro = float(input(f'Ingrese el precio del producto {i}: '))
    precios.append(precioPro)

suma = sum(precios)
promedio = suma/10
maximo = max(precios)
minimo = min(precios)
precios.remove(maximo)
maximo1 = max(precios)

print(f'La suma de los precios es {suma} y el promedio es {round(promedio, 2)}. Además el precio más caro fue {maximo} y el segundo precio más caro fue {maximo1} y el precio más barato fue {minimo}')