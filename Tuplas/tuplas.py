
from re import X


sequencial = [i for i in range(100)]

a = (1, 2, 3)

sequencial_tupla = tuple(sequencial)
letras = tuple('abc')

# print('Tipo de sequencial: ', type(sequencial))
# print('Tipo de c: ', type(c))

# sequencial_tupla[0] = 'a'
# print(letras[0])

tupla_com_um_elemento = ('a', )
# print( type( tupla_com_um_elemento) )

tupla_a = (0, 100, 2)
tupla_b = (0, 3, 4)

#Comparação entre tuplas

print(tupla_a < tupla_b)

# Atribuição de tuplas

x=10
y=20

x, y = y, x

print(x, y)


# Métodos das tuplas
tupla = ('a', 'a', 'a', 'b', 'b', 'b', 'c')

print('Verificando os índices de cada elemento: ')
print(tupla.index('a'))
print(tupla.index('b'))
print(tupla.index('c'))

print('Verificando as quantidades de cada elemento: ')
print(tupla.count('a'))
print(tupla.count('b'))
print(tupla.count('c'))
