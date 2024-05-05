def numPorDos(num):
    return num * 2

def numMasDiez(num):
    return num + 10

def numPorTres(num):
    return num * 3

def numCero(num):
    return 0

dic = {
    '1': numPorDos,
    '2': numMasDiez,
    '3': numPorTres,
}

try:
    num = int(input('Ingrese un número: '))
    newNum = str(num)
    print(dic.get(newNum[-1], numCero)(num))
except ValueError:
    print('Debe ingresar un número entero')