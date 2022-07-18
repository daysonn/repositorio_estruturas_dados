
# Usando tuplas como chaves de dicionarios
# Dicionário de telefones: chaves como nome e sobrenome

nomes_e_telefones = {
    ('Ana', 'Santos'): '555-5550',
    ('Dayson', 'Nascimento'): '555-5551',
    ('Paula Melo'): '555-5552'
}

#Iterando sobre o dicionário
for nome, sobrenome in nomes_e_telefones:
    # print(nome, sobrenome, nomes_e_telefones[(nome, sobrenome)])
    if sobrenome == 'Santos':
        print(f'O contato {nome} de sobrenome {sobrenome} telefone: {nomes_e_telefones[(nome, sobrenome)]}')

