try:
    x = float(input('Introduzca el valor de x: '))
    y = float(input('Introduzca el valor de y: '))
    if y != 1:
        if x >= 0:
            resultado = (x**(1/2))/((y**2)-1)
            print(f'f(x,y) = {round(resultado, 3)}')
        else:
            print('El valor de x no puede ser negativo')
    else:
        print('El valor de y no puede ser 1 porque el denominador no puede ser 0')
except:
    print('Introduzca valores numéricos')