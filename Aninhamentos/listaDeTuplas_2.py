# Lista de tuplas

# Declaração
lista_numeros = [1, 2, 3, 4, 5]
lista_letras = ['a', 'b', 'c', 'd', 'e']


print('Tipo: ', type(zip(lista_numeros, lista_letras)))

print( list(zip(lista_numeros, lista_letras)) )

#Iterando sobre o zip
for numero, letra in zip(lista_numeros, lista_letras):
    print(f'Numero: {numero} e letra: {letra}')
