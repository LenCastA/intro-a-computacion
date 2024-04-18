cursos = ['Matemática', 'Física', 'Química', 'Estadística', 'Programación']

mate = float(input('Ingrese el promedio de Matemática: '))
fisi = float(input('Ingrese el promedio de Física: '))
qui = float(input('Ingrese el promedio de Química: '))
est = float(input('Ingrese el promedio de Estadística: '))
prog = float(input('Ingrese el promedio de Programación: '))

prom = [mate, fisi, qui, est, prog]

minimo = min(prom)
maximo = max(prom)

dic = {
    mate:'Matemática',
    fisi:'Física',
    qui:'Química',
    est:'Estadística',
    prog:'Programación'}

if mate >= 12:
    cursos.remove('Matemática')
if fisi >= 12:
    cursos.remove('Física')
if qui >= 12:
    cursos.remove('Química')
if est >= 12:
    cursos.remove('Estadística')
if prog >= 12:
    cursos.remove('Programación')

print('Usted debe llevar los siguientes cursos:')
for curso in cursos:
    print(f'- {curso}')

print(f'Además su mejor promedio fue en {dic[maximo]} y su menor promedio fue en {dic[minimo]}')