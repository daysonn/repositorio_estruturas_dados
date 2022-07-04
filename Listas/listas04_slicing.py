

lista_famosos = ['Beyonce', 'Brad', 'Leonardo', 'Natalie', 'Madonna']

print(lista_famosos[1:])

lista_copia = lista_famosos[:]
lista_copia = lista_famosos.copy()

lista_copia.remove('Brad')

print('Original: ', lista_famosos)
print('Cópia: ', lista_copia)