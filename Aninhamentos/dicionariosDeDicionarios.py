# Declaração de um dicionario de dicionarios

carro01 = {'cor': 'preto', 'motor': 2.0, 'ano':2012}
carro02 = {'cor': 'branco', 'motor': 1.0, 'ano':2013}
carro03 = {'cor': 'prata', 'motor': 2.4, 'ano':2014}
carro04 = {'cor': 'vermelho', 'motor': 1.6, 'ano':2015}

dicionario_carros = {
    'Gol': carro01,
    'Corsa': carro02,
    'Hilux': carro03,
    'Fiesta': carro04
}

# Iterando sobre o dicionário de dicionários
# for chave in dicionario_carros:
#     print(dicionario_carros[chave])

print('\n #################################### \n')
for primeira_chave in dicionario_carros:
    print(f'Carro {primeira_chave}: ')
    for segunda_chave in dicionario_carros[primeira_chave]:

        # print(dicionario_carros[primeira_chave][segunda_chave])
        print(f'- {segunda_chave} do carro é {dicionario_carros[primeira_chave][segunda_chave]}')
    print('\n')