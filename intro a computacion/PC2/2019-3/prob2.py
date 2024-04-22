try:
    cantidad = int(input('Cuántos números quiere evaluar?: '))
    flag = 0
    for i in range(1, cantidad+1):
        num = int(input(f'Introduzca el número {i}: '))
        for j in range(1, num):
            if j * (j + 1) == num:
                flag += 1
                break

    print(f"La cantidad de números que cumplen la condición es: {flag}")
except ValueError:
    print('Introduzca un número natural')