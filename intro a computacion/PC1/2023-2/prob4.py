num = int(input('Introduce un número: '))

if num > 1000:
    sep = list(str(num))
    sep = list(map(int, sep))
    minimo = min(sep)
    while minimo in sep:
        sep.remove(minimo)
    sep = list(map(str, sep))
    newNum = int(''.join(sep))
    print(f'El número sin el dígito menor es: {newNum}')
else:
    print('El número tiene que ser mayor a 1000')