ventas = []
print('-------Ventas de Enero-------')
for i in range(1,32):
    venta = float(input(f'Ingrese el monto de la venta del día {i}: '))
    ventas.append(venta)

print('-------Ventas de Febrero-------')
for i in range(1,31):
    venta = float(input(f'Ingrese el monto de la venta del día {i}: '))
    ventas.append(venta)
    
ventaMax = max(ventas)
ventaMin = min(ventas)

print(f'La venta máxima fue de {ventaMax} y la venta mínima fue de {ventaMin}')