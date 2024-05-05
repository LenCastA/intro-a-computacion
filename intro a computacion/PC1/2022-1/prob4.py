def esPerfecto(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma == n

for n in range(1, 1001):
    if esPerfecto(n) == True:
        print(n)