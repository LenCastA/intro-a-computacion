def obtenerClave(diccionario, valor):
    for clave, val in diccionario.items():
        if val == valor:
            return clave
        
texto = input('Introduce el texto: ')

texto = texto.replace(' ', '')
texto = texto.lower()
list = list(set(texto))

contadores = []
dicc = {}

for i in list:
    contador = 0
    for j in texto:
        if i == j:
            contador += 1
    contadores.append(contador)        
    key, value = i, contador
    dicc[key] = value

maximo = max(contadores)
letra = obtenerClave(dicc, maximo)

print(f'La letra {letra} aparece {maximo} veces')
