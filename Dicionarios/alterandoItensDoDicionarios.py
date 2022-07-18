# Declaração de dicionário 
# que traduz do inglês para português

inglesPortugues = {'one': 'um', 'two':'dois', 'three':'três', 'four':'quatro', 'five': 'cinco'}

# Usando atribuição
inglesPortugues['one'] = 'uno'

# Usando método update
chave = input('chave')
valor = input('valor')
inglesPortugues.update({chave: valor})
# inglesPortugues.update({1: 'dos'})

print(inglesPortugues)

# E se eu tentar update em uma chave que não existe?
# inglesPortugues.update({'six': 'seis'})
# print(inglesPortugues)
