meses = {
    1:'Enero',
    2:'Febrero',
    3:'Marzo',
    4:'Abril',
    5:'Mayo',
    6:'Junio',
    7:'Julio',
    8:'Agosto',
    9:'Septiembre',
    10:'Octubre',
    11:'Noviembre',
    12:'Diciembre',
}

try:
    mes = int(input('Introduzca el número del mes: '))
    print(f'El mes es {meses[mes]}')
except ValueError:
    print('Por favor, introduzca un número entero.')
except KeyError:
    print('No es un número de mes válido.')