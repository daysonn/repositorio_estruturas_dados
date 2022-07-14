
# Declaração de dicionários
# Primeira forma
portuguesIngles = dict()
portuguesIngles['um'] = 'one'
portuguesIngles['dois'] = 'two'
portuguesIngles['tres'] = 'three'

# Segunda forma
inglesPortugues = { 'one': 'um', 'two':'dois', 'three':'tres' }

print(portuguesIngles)
print(inglesPortugues)

# Operadores com os dicionários
print('Tamanho do dicionário portugues-ingles:', len(portuguesIngles))
print('Tamanho do dicionário ingles-portugues:', len(inglesPortugues))

#Checando se as duas opções são chaves válidas no dicionário
if 'one' in inglesPortugues:
    print(f'One é uma chave válida e possui valor ', inglesPortugues['one'])

if 'um' in inglesPortugues:
    print('Um é uma chave válida e possui valor', inglesPortugues['one'] )
else:
    print('Chave inválida!')