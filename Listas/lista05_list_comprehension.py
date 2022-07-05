
lista_frutas_sem_letra_a = []
lista_frutas = ['maçã', 'banana', 'melancia', 'mamão', 'kiwi', 'coco', 'pêssego', 'figo']

for nome_fruta in lista_frutas:
    if 'a' not in nome_fruta:
        lista_frutas_sem_letra_a.append(nome_fruta)

lista_frutas_sem_letra_a = [nome_fruta.upper() for nome_fruta in lista_frutas if 'a' not in nome_fruta]

print('Tamanho da lista: ',  len (  [fruta.upper() for fruta in lista_frutas]  )    )

# print(lista_frutas_sem_letra_a)