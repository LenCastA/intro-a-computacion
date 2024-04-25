num = int(input('Introduce el número: '))
lista = []
for i in range(1, num + 1):
    if num % i == 0:
        lista.append(i)

print(f'Los divisores del número son: {lista}')