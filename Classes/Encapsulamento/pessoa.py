
class Casa:
    def __init__(self, endereco, proprietario):
        self.endereco = endereco
        self.titular = proprietario

class Pessoa:
    def __init__(self, nome, cpf, casa):
        self._cpf = cpf
        self._nome = nome
        self.casa = casa

    def setNome(self, novoNome):
        self._nome = novoNome

    def getNome(self):
        return self._nome

class Servico:
    def __init__(self, valor, data_inicio, nome, cpf, casa):
        self.valor = valor
        self.titular = Pessoa(nome, cpf, casa)
        self.data = data_inicio
        
    def alterarTitulardoServico(self, nomeNovo):
        self.titular.alterarNome(nomeNovo)

    def resgatarDadosServico(self):
        return f"O cliente {self.titular.getNome()} tem um servico no valor de R${self.valor} no endereco {self.titular.casa.endereco}."


print("[1] Cadastrar um servico \n[2] Alterar o nome de um cliente em um serviço \n [0] Para sair do sistema")

entrada_usuario = input("Digite uma das opções acima: ")

while entrada_usuario != "0":

    if entrada_usuario == "1":
        print("Vamos iniciar pelos dados da residencia do cliente")

        endereco = input("Digite o endereco: ")
        nome_titular_endereco = input("Nome do titular do endereço informado: ")
        casa = Casa(endereco, nome_titular_endereco)

        print("Vamos agora para os dados do cliente")
        nome = input("Digite o nome: ")
        cpf = input("Digite o cpf: ")
        valor = input("Digite o valor do serviço: ")
        data = input("Digite a data atual: ")

        servico = Servico(valor, data, nome, cpf, casa)
        print(servico.resgatarDadosServico())








