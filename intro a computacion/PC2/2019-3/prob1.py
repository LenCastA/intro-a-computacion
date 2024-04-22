def main(num):
    parte1 = 0
    parte2 = 0
    parte3 = 0
    if num % 2 != 0:
        for i in range(1, num + 1):
            exp4 = i ** 4
            parte1 += exp4
        for i in range(1, num + 1):
            exp3 = 6 * (i ** 3)
            parte2 += exp3
        for i in range(1, num + 1):
            exp0 = 5
            parte3 += exp0
        print(f'La suma es: {parte1 + parte2 + parte3}')
        
    else:
        for i in range(1, num + 1):
            exp5 = i ** 5
            parte1 += exp5
        for i in range(1, num + 1):
            exp3 = (3 / 20) * (i ** 3)
            parte2 += exp3
        for i in range(1, num + 1):
            exp0 = 5
            parte3 += exp0
            
        print(f'La suma es: {parte1 + parte2 + parte3}')


try:
    num = int(input('Introduzca un número: '))
    main(num)
except:
    print('Introduzca un valor numérico')