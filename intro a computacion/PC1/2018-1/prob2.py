num = int(input('Ingrese un número entero mayor a 50: '))

monedasDeCinco = 0
monedasDeDos = 0
monedasDeUno = 0

if num > 50:
    monedasDeCinco = num // 5
    num %= 5
    monedasDeDos = num // 2
    num %= 2
    monedasDeUno = num
    print('Monedas de 5 soles:', monedasDeCinco)
    print('Monedas de 2 soles:', monedasDeDos)
    print('Monedas de 1 sol:', monedasDeUno)