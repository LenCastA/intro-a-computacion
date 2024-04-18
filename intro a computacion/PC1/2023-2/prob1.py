try:
    num = int(input('Introduzca el número: '))
    if num % 2 == 0:
        print('El número es par')
    else:
        print('El número es impar')
except ValueError:
    print('Introduzca números válidos')