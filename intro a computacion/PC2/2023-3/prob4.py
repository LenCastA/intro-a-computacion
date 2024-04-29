import math

print('Se tiene la ecuación cuadrática ax^2 + bx + c = 0')
a = float(input('Ingrese a: '))
b = float(input('Ingrese b: '))
c = float(input('Ingrese c: '))

discriminante = (b ** 2) - (4 * a * c)

if discriminante > 0:
    sol1 = (-b + (math.sqrt(discriminante))) / (2 * a)
    sol2 = (-b - (math.sqrt(discriminante))) / (2 * a)  
    print(f'Las soluciones son reales y son: {round(sol1, 3)} y {round(sol2, 3)}')
elif discriminante == 0:
    sol1 = (-b + (math.sqrt(discriminante))) / (2 * a)
    print(f'Existe una solución única y real: {round(sol1, 3)}')
else:
    parteReal = -b / (2 * a)
    parteImaginaria = (1*math.sqrt(abs(discriminante))) / (2 * a)
    print(f'Las soluciones son complejas y son: {round(parteReal, 3)} + {round(parteImaginaria, 3)}i y {round(parteReal, 3)} - {round(parteImaginaria, 3)}i')