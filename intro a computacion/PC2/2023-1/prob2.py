prom = float(input('Introduzca su promedio general: '))

if 0 <= prom < 5:
    print('Su categoría es D')
elif 5 <= prom < 10:
    print('Su categoría es C')
elif 10 <= prom < 15:
    print('Su categoría es B')
elif 15 <= prom <= 20:
    print('Su categoría es A')
else:
    print('Promedio inválido')