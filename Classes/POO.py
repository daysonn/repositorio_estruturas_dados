
class Lista():
    salvar = []
    tamanho = 0

    def inserirItens(self, quantidade):
        
        for i in range(quantidade):
            entrada = input(f"Insira o item {i+1} na lista: ")
            self.salvar.append(entrada)
            self.tamanho += 1

    def exibirItens(self):

        print("\nExibindo os itens: ")
        for i in range(self.tamanho):
            print(self.salvar[i])
        print('\n')


compras = Lista()

quantidade = int( input("Por favor, digite a quantidade de itens a serem inseridos na lista: ") ) 

compras.inserirItens(quantidade)
compras.exibirItens()

print("Tamanho total da lista: ", compras.tamanho)