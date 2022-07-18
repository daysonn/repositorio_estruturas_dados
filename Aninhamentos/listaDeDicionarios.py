
# Declaração de dicionarios

carro01 = {'cor': 'preto', 'motor': 2.0, 'ano':2012}
carro02 = {'cor': 'branco', 'motor': 1.0, 'ano':2013}
carro03 = {'cor': 'prata', 'motor': 2.4, 'ano':2014}
carro04 = {'cor': 'vermelho', 'motor': 1.6, 'ano':2015}

lista_de_dicionarios_de_carros = [carro01, carro02, carro03, carro04]

# Iterando sobre a lista de carros
# for carro in lista_de_dicionarios_de_carros:
#     print(carro)

entrada_do_usuario = input('Defina a cor do carro: ')
for carro in lista_de_dicionarios_de_carros:

    for caracteristica in carro:
        if carro[caracteristica] == entrada_do_usuario:
            print(carro)