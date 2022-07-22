class Historico:
    def __init__(self, data):
        self.data_abertura = data
        self.transacoes = []
    
    def inserirTransacao(self, transacao):
        self.transacoes.append(transacao)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, cliente):
        self.titular = cliente
        self.historico = Historico(datetime.now())
        self.saldo = 0

    def inserirDinheiro(self, quantia):
        self.saldo += quantia
        self.historico.inserirTransacao(f"{quantia} inserida na conta. Novo saldo {self.saldo}")


primeiro_cliente = Cliente("Hermano", "Braga", 11111)
primeira_conta = Conta(primeiro_cliente)
primeira_conta.inserirDinheiro(100)




