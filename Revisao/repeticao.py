


def criar_lista_de_lista(tamanho_lista = 50):

    lista_de_lista_numeros = []
    for i in range(tamanho_lista):
        lista_numeros = []
        for j in range(100):
            lista_numeros.append(j)

        lista_de_lista_numeros.append(lista_numeros)
        print(f"{i}: lista com {len(lista_numeros)} números criada")
    
    return lista_de_lista_numeros

lista_listas = criar_lista_de_lista(100)
print(f"Tamanho da lista de listas: {len(lista_listas)}")

