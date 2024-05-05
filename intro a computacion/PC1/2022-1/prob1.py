monto = float(input('Introduzca el monto que vendió durante el mes: '))

if monto > 0 and monto < 2000:
    print('Su bonificación es de 3%')
    print('Su bonificación total es de', monto * 0.03)
elif monto >= 2000 and monto < 3500:
    print('Su bonificación es de 4%')
    print('Su bonificación total es de', monto * 0.04)
elif monto >= 3500 and monto < 6000:
    print('Su bonificación es de 7%')
    print('Su bonificación total es de', monto * 0.07)
elif monto >= 6000:
    print('Su bonificación es de 9%')
    print('Su bonificación total es de', monto * 0.09)