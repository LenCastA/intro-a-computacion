abc = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h',
    9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
    16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v',
    23: 'w', 24: 'x', 25: 'y', 26: 'z'
}

def obtenerClave(diccionario, valor):
    for clave, val in diccionario.items():
        if val == valor:
            return clave

def encrypt():
    wordList = []
    word = input('Introduzca la palabra u oración: ')
    word = word.lower()
    
    lista = list(word)
    for i in lista:
        try:
            clave = obtenerClave(abc, i)
            clave = clave - 3
            if clave < 1:
                clave = clave + 26
            wordList.append(abc.get(clave))
        except:
            wordList.append(' ')
        
    newWord = ''.join(wordList)
    return print(newWord)
    
def desencrypt():
    wordList = []
    word = input('Introduzca la palabra u oración: ')
    word = word.lower()
    lista = list(word)
    for i in lista:
        try:
            clave = obtenerClave(abc, i)
            clave = clave + 3
            if clave > 26:
                clave = clave - 26
            wordList.append(abc.get(clave))
        except:
            wordList.append(' ')
    
    newWord = ''.join(wordList)
    return print(newWord)
    
def main():
    print('''==========MENU==========
    1. Desencriptar
    2. Encriptar''')
    opcion = int(input('Introduzca una opción: '))
    if opcion == 1:
        desencrypt()
    elif opcion == 2:
        encrypt()
    else:
        print('Introduzca un valor correcto')
        
main()