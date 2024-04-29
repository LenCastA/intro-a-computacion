peso = float(input('Ingrese el peso (kg): '))
estatura = float(input('Ingrese la estatura (m): '))

imc = peso / (estatura ** 2)

if imc < 18.5:
    print('Bajo peso')
elif imc < 24.9:
    print('Peso saludable')
elif imc < 29.9:
    print('Sobrepeso')
else:
    print('Obesidad')