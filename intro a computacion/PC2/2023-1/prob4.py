RAZSO = 'Internacional S.A.C.'
RUC = '34545678911'
LUGAR = 'Ciudad de Lima'
CARGO = 'Administrador'
ADPEN = 'AFP Integra'

def boleta():
    return print(f'''=================BOLETA DE PAGO===================
Periodo: Abril 2023
Datos del Empleador:
 – Razón Social: {RAZSO}
 – RUC: {RUC}
 – Lugar: {LUGAR}
Datos del Empleado:
 – Código: {code}
 – DNI: {dni}
 – Apellidos y Nombres: {lastName + ' ' + name}
 – Cargo: {CARGO}
 – Administrador de pensión: {ADPEN}
DETALLE DE LA REMUNERACIÓN
Ingresos:
 – Remuneración básica (bruta): S/ {sueldoB}
 – Bonificación al cargo: S/ {bono}
 – Total ingresos: S/ {totalI}
Descuentos y retenciones:
 – AFP Integra: S/ {round(afp, 2)}
 – IR 5ta categoría: S/ {round(impuesto, 2)}
 – Faltas y Tradanzas: S/ {round(descuento, 2)}
 – Total descuentos: S/ {round(totalD, 3)}
Aportes del empleador
 – ESSALUD: S/ {essalud}
 – Total aportes: S/ {essalud}
Neto a pagar = S/ {round(totalI - totalD, 3)}''')


name = input('Introduce tus nombres: ')
lastName = input('Introduce tus apellidos: ')
dni = input('Introduce tu DNI (8 dígitos): ')

if len(dni) == 8:
    code = input('Introduce tu código (5 dígitos): ')
    if len(code) == 5:
        try:
            sueldoB = int(input('Introduce su sueldo: '))
            bono = 1000
            totalI = bono + sueldoB
            afp = (sueldoB*0.1) + (sueldoB*0.0155) + (sueldoB*0.0174)
            impuesto = 0.08*sueldoB
            descuento = sueldoB/30
            totalD = afp + impuesto + descuento
            essalud = 0.09*totalI
            boleta()
        except ValueError:
            print('Introduzca su sueldo real')
    else:
        print('Introduzca un código válido')
else:
    print('Introduzca un DNI válido')