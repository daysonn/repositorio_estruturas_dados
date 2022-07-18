# Declaração de dicionário 
# que traduz do inglês para português

inglesPortugues = {'one': 'um', 'two':'dois', 'three':'três', 'four':'quatro', 'five': 'cinco'}

# Remover a partir de uma chave
valor = inglesPortugues.pop('one')
del inglesPortugues['two']

print('Valor: ', valor)
print('\nDicionário após deletar as chaves: ')
print(inglesPortugues)

# Remover último item inserido
inglesPortugues['one'] = 'um'
print('\nDicionário após deletar último item: ')
inglesPortugues.popitem()
print(inglesPortugues)

# Esvaziando o dicionário
inglesPortugues.clear()
print('\nDicionário após esvaziamento: ')
print(inglesPortugues)