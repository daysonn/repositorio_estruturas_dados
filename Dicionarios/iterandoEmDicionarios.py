# Declaração de dicionário 
# que traduz do inglês para português

inglesPortugues = {'one': 'um', 'two':'dois', 'three':'três', 'four':'quatro', 'five': 'cinco'}

print('Iterando com a primeira forma:\n')

for chave in inglesPortugues:
    print('A chave ', chave, 'possui valor ', inglesPortugues[chave], 'no dicionario')
    novo_valor = input(f'Defina um novo valor para a chave {chave}: ')
    inglesPortugues[chave] = novo_valor
    

    #print(f' Chave {chave} e valor {inglesPortugues[chave]}')

print(inglesPortugues)
# Usando o método .items()
# print('\nIterando com a segunda forma:\n')
# for chave, valor in inglesPortugues.items():
#     print(f'Os valores da tupla são chave={chave} e valor={valor}')

