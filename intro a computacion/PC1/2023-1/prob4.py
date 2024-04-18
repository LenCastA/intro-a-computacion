RAZSO = 'Mundo Negocios S.R.L.'
RUC = 22245678911
LUGAR = 'Ciudad de Lima'
CARGO = 'Administrador'

def boleta():
    return print(f'''=================BOLETA DE PAGO===================
Periodo: Marzo 2023
Datos del Empleador:
 – Razón Social: {RAZSO}
 – RUC: {RUC}
 – Lugar: {LUGAR}
Datos del Empleado:
 – Código: {code}
 – DNI: {dni}
 – Nombres y Apellidos: {name + ' ' + lastName}
 – Cargo: {CARGO}
 – Administrador de pensión
DETALLE DE LA REMUNERACIÓN
Ingresos:
 – Remuneración básica: {sueldoB} soles
 – Asignación familiar: {asFam} soles
 – Bonificación al cargo: {bono} soles
 – Total ingresos: {totalI}
Descuentos y retenciones:
 – ONP: {round(onp, 2)}
 – Total descuentos: {round(onp, 2)}
Aportes del empleador
 – ESSALUD: {essalud}
 – Total aportes: {essalud}
Neto a pagar = {totalI-onp}''')


name = input('Introduce tus nombres: ')
lastName = input('Introduce tus apellidos: ')
dni = input('Introduce tu DNI (8 dígitos): ')

if len(dni) == 8:
    code = input('Introduce tu código (5 dígitos): ')
    if len(code) == 5:
        try:
            sueldoB = int(input('Introduce su sueldo: '))
            bono = 800
            asFam = 2*(sueldoB*0.1)
            totalI = sueldoB + bono + asFam
            onp = totalI*0.13
            essalud = 0.09*totalI
            boleta()
        except ValueError:
            print('Introduzca su sueldo real')
    else:
        print('Introduzca un código válido')
else:
    print('Introduzca un DNI válido')