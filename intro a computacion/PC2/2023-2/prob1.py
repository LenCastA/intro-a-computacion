nums = []
proh = ['0', '2', '4', '6', '8']
for num in range(100, 1000):
    lista = list(str(num))
    contienePar = False
    for i in lista:
        if i in proh:
            contienePar = True
            break
    if contienePar == False:
        nums.append(num)

suma = sum(nums)
elementos = len(nums)
print(f'La suma de los elementos es {suma} y el promedio es {round(suma/elementos, 2)}')
