class Funcionario: 
    def __init__(self, nome, cpf, salario): 
        self._nome = nome 
        self._cpf = cpf 
        self._salario = salario

class Gerente(Funcionario): 

    def __init__(self, senha, qtd_funcionarios): 
        self._senha = senha 
        self._qtd_funcionarios = qtd_funcionarios 

    def autentica(self, senha): 
        if self._senha == senha: 
            print("acesso permitido") 
            return True 
        else: 
            print("acesso negado")
            return False

    def getNome(self):
        return self._nome


nome = "Hermano"
cpf = '000'
salario = 10
senha = '12345'
qtd_funcionarios = 5
