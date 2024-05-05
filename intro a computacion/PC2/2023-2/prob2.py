n = int(input('Introduce un número entero: '))
suma = 1
factorial = 1
i = 1

while i <= n:
    factorial *= i
    if i % 2 == 0:
        suma -= 1 / factorial
    else:
        suma += 1 / factorial
    i += 1

print(f'La suma de las inversas de los factoriales es: {suma}')