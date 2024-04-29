importe = float(input('Ingrese el importe total de compra: '))

if importe > 0 and importe < 50:
    pagoFinal = importe
    print(f'El monto final a pagar es {pagoFinal}')
elif importe >= 50 and importe < 100:
    pagoFinal = importe - (importe * 0.05)
    print(f'El monto final a pagar es {pagoFinal}')
elif importe >= 100 and importe < 200:
    pagoFinal = importe - (importe * 0.1)
    print(f'El monto final a pagar es {pagoFinal}')
elif importe >= 200 and importe < 300:
    pagoFinal = importe - (importe * 0.15)
    print(f'El monto final a pagar es {pagoFinal}')
elif importe >= 300:
    pagoFinal = importe - (importe * 0.2)
    print(f'El monto final a pagar es {pagoFinal}')
else:
    print('Ingrese un importe válido')