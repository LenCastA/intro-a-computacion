def aCua():
    try:
        lado = float(input('Introduzca el valor del lado: '))
        area = lado**2
        print(f'El área del cuadrado es {area}')
    except:
        print('Introduzca valores numéricos')
        
def aCir():
    try:
        radio = float(input('Introduzca el valor del radio: '))
        area = (radio**2)*3.14
        print(f'El área del círculo es {area}')
    except:
        print('Introduzca valores numéricos')

def aRec():
    try:
        base = float(input('Introduzca el valor de la base: '))
        altura = float(input('Introduzca el valor de la altura: '))
        print(f'El área del rectángulo es {area}')
        area = base*altura
    except:
        print('Introduzca valores numéricos')
    
def aTri():
    try:
        base = float(input('Introduzca el valor de la base: '))
        altura = float(input('Introduzca el valor de la altura: '))
        area = (base*altura)/2
        print(f'El área del triángulo es {area}')
    except:
        print('Introduzca valores numéricos')

def aTrap():
    try:
        base1 = float(input('Introduzca el valor de la base 1: '))
        base2 = float(input('Introduzca el valor de la base 2: '))
        altura = float(input('Introduzca el valor de la altura: '))
        area = ((base1 + base2)/2)*altura
        print(f'El área del trapecio es {area}')
    except:
        print('Introduzca valores numéricos')

def main(op):
    if op == 1:
        aCua()
    elif op == 2:
        aCir()
    elif op == 3:
        aRec()
    elif op == 4:
        aTrap()
    elif op == 5:
        aTri()


print('''==========================================
           CÁLCULO DE SUPERFICIES
==========================================
1. Cuadrado lado*lado
2. Círculo pi*radio*radio
3. Rectángulo base*altura
4. Trapecio (base1+base2) *altura/2
5. Triángulo (base*altura) /2
==========================================''')

try:
    op = int(input('Escoja la operación a realizar: '))
    if 1<= op <=5:
        main(op)
    else:
        print('No existe opción')
except ValueError:
    print('Introduzca un valor admitido')
