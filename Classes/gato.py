
class Gato():
    nome = ''
    cor = ''
    idade = 0
    raca = ''
    sexo = ''

    def inserirItens(self, nome_entrada, cor_entrada, idade_entrada, raca_entrada, sexo_entrada):

        self.nome = nome_entrada
        self.cor = cor_entrada
        self.idade = idade_entrada
        self.raca = raca_entrada
        self.sexo = sexo_entrada

    def miar(self):
        return(f"O gato {self.nome} miou")

    def comer(self):
        return(f"O gato {self.nome} comeu")

    def exibirDados(self):
        print(f'O gato tem nome {self.nome}, idade {self.idade} e é da cor {self.cor}')


nome = input('Digite o nome do gato: ')
cor = input('Digite a cor do gato: ')
raca = input('Digite a raça: ')
idade = int(input('Digite a idade: '))
sexo = input('Digite o sexo do gato: ')

primeiro_gatinho = Gato()
primeiro_gatinho.inserirItens(nome, cor, idade, raca, sexo)

entrada = ""
while entrada != 'sair':
    entrada = input('Digite a ação que o gato deve executar (comer, miar ou sair): ')

    if entrada == 'comer':
        acao = primeiro_gatinho.comer()
        print(acao)
    elif entrada == 'miar':
        acao = primeiro_gatinho.miar()
        print(acao)

