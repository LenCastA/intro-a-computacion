caracter = input('Introduzca un carácter: ')

vocales = ['a', 'e', 'i', 'o', 'u']

for i in vocales:
    if str(caracter) == i:
        print('Sí es una vocal')
        break
    else:
        print('No es una vocal')
        break