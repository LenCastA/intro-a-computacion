proLunes = int(input('Introduzca la producción del lunes: '))
proMartes = int(input('Introduzca la producción del martes: '))
proMiercoles = int(input('Introduzca la producción del miércoles: '))
proJueves = int(input('Introduzca la producción del jueves: '))
proViernes = int(input('Introduzca la producción del viernes: '))

promedio = (proLunes + proMartes + proMiercoles + proJueves + proViernes) / 5

if promedio > 100:
    print('Sí recibirá incentivos')
else:
    print('No recibirá incentivos')