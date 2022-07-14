
# Declaração de dicionário com listas

numerosParaListadePalavras = dict()
numerosParaListadePalavras[1] = ['one', 'uno', 'um']
numerosParaListadePalavras[2] = ['two', 'dos', 'dois']
numerosParaListadePalavras[3] = ['three', 'tres', 'tres']

#lista_de_1 = numerosParaListadePalavras[1]
numerosParaListadePalavras[1].append('une')
numerosParaListadePalavras[1].append('ichi')

numerosParaListadePalavras[4] = ['four', 'cuatro', 'quatro']

del numerosParaListadePalavras[3]

print(numerosParaListadePalavras)
