codigos = {'2018': 0, '2019': 0, '2020': 0, '2021': 0, '2022': 0, '2023': 0}
escuelas = {'1': 0, '2': 0, '3': 0, '4': 0}

print('''1.Industriales
2.Sistemas
3.Telemática
4.Software''')

opcion = input('Está listo para comenzar? (s/n): ')

while opcion == 's':
    codigo = input('Ingrese el código: ')
    if codigo in codigos:
        codigos[codigo] += 1
    escuela = input('Ingrese la escuela profesional: ')
    if escuela in escuelas:
        escuelas[escuela] += 1
    opcion = input('Desea agregar un nuevo registro? (s/n): ')

print(f'''El informe final tiene los siguientes resultados:
Cantidad de alumnos por código:
2018: {codigos['2018']}
2019: {codigos['2019']}
2020: {codigos['2020']}
2021: {codigos['2021']}
2022: {codigos['2022']}
2023: {codigos['2023']}
Cantidad de alumnos por escuela:
Industriales: {escuelas['1']}
Sistemas: {escuelas['2']}
Telemática: {escuelas['3']}
Software: {escuelas['4']}''')