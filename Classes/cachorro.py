
class Cachorro():
    nome = ""
    cor = ""
    raca = ""
    idade = 0
    data_nascimento = ""

    def inserirDados(self, nome_entrada, cor_entrada, raca_entrada, idade_entrada, nascimento_entrada):

        self.nome = nome_entrada
        self.cor = cor_entrada
        self.raca = raca_entrada
        self.idade = idade_entrada
        self.data_nascimento = nascimento_entrada

    def latir(self):
        print("O cachorro latiu")

    def comer(self):
        print("O cachorro comeu!")

    def exibirDados(self):
        print(f'O cachorro tem nome {self.nome}, idade: {self.idade} e é da cor {self.cor}')

# Instanciar a classe
golden_retriever = Cachorro()

qtd = int(input("Digite quantos cachorros vc quer incluir: "))
lista_de_cachorros = []

nome = input('Digite o nome do cachorro: ')
cor = input('Digite a cor do cachorro')
raca = input('Digite a raça: ')
idade = int(input('Digite a idade: '))
nascimento = input('Digite o dia de nascimento: ')

golden_retriever.inserirDados(nome, cor, raca, idade, nascimento)

entrada = ""
while entrada != 'sair':
    entrada = input('Digite a ação que o cachorro deve executar: ')

    if entrada == 'comer':
        golden_retriever.comer()
    elif entrada == 'latir':
        golden_retriever.latir()

golden_retriever.exibirDados()