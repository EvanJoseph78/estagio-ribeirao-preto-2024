string = 'Evandro Mariano'
lista = []

for caracter in string:
    lista.insert(0, caracter)

stringInvertida = ''.join(lista)
print(stringInvertida)
