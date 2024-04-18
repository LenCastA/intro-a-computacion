lista = []

for i in range(1,4):
    num = float(input(f'Introduce el número {i}: '))
    lista.append(num)

maximo = max(lista)
lista.remove(maximo)
maximo1 = max(lista)
lista.remove(maximo1)
maximo2 = max(lista)

print(f'Los números ordenado de mayor a menor son: {maximo}, {maximo1}, {maximo2}')

