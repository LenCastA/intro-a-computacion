num = int(input('Introduzca un número entero mayor que 3: '))

suma = 0
factorial = 1
i = 1

while i <= num:
    factorial *= i
    suma += factorial
    if i != num:
        print(i, '!', end=' + ')
    else:
        print(i, '!', end=' ')
    i += 1

print('=', suma)