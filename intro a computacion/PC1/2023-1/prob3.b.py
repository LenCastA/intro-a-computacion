import math as m

def function(x, y):
    if x >= 0:
        num = m.sqrt(x)
        if y != 1 and y != -1:
            dom = m.pow(y, 2) - 1
            rpta = fraction(num, dom)
            return round(rpta, 3)
        else:
            print('El valor de y no puede ser ±1')
    else:
        print('El valor de x no puede ser negativo')

def fraction(num, dom):
    return(num / dom)

def main():
    try:
        x = float(input('Introduzca el valor de x: '))
        y = float(input('Introduzca el valor de y: '))
        result = function(x, y)
        if result is not None:
            print(result)
    except ValueError:
        print('Por favor, ingrese valores numéricos válidos')
        main()

main()