
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf
    

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def get_titular(self):
        return self.titular.get_nome()

    def get_cpf_do_titular(self):
        return self.titular.get_cpf()

    def get_dados_titular(self):
        return self.get_titular(), self.get_cpf_do_titular()

primeiro_cliente = Cliente("Hermano", "Braga", 111111111)
primeira_conta = Conta("1111-5", primeiro_cliente, 0, 500)

print(primeira_conta.get_titular())



