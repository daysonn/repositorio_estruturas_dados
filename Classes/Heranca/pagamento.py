'''
######  Passo a passo feito em sala ######
    1- Criar a classe Funcionario
    2- Criar as classes FuncionarioCLT e FuncionarioPJ que herdam de Funcionario, usando métodos polimorfos de calcular salário
    3- Criar o método de definir a senioridade do cargo para termos um fator que multiplica o salário base
    4- Criar a classe Pessoa que vai ser agregada à classe Funcionário
'''

class Pessoa:
    def __init__(self, nome, cpf) -> None:
        self.nome = nome
        self._cpf = cpf

class Funcionario:
    def __init__(self, pessoa, salarioBase):
        self.pessoa = pessoa
        self._salarioBase = salarioBase

    def calcularSalario(self):
        return self._salarioBase

class FuncionarioCLT(Funcionario):
    def __init__(self, pessoa, salarioBase, mesesEmpresa):
        Funcionario.__init__(self, pessoa, salarioBase)
        self.mesesEmpresa = mesesEmpresa

    def calcularSalario(self):
        self._salario = self._salarioBase*(self.mesesEmpresa/100)
        return self._salario

class FuncionarioPJ(Funcionario):
    def __init__(self, pessoa, salarioBase, anosExperiencia):
        Funcionario.__init__(self, pessoa, salarioBase)
        self.anosExperiencia = anosExperiencia
        self.__definirSenioridadeCargo()

    def __definirSenioridadeCargo(self):
        if self.anosExperiencia < 3:
            self.senioridade = 'Junior'
            self._fator = 1
        elif self.anosExperiencia > 3 and self.anosExperiencia < 5:
            self.senioridade = 'Pleno'
            self._fator = 2
        else:
            self.senioridade = 'Senior'
            self._fator = 3

    def setAnosExeperiencia(self, anosExperiencia):
        self.anosExperiencia = anosExperiencia
        self.__definirSenioridadeCargo()

    def calcularSalario(self):

        self._salario = self._salarioBase*self._fator
        return self._salario



pessoa01 = Pessoa("Hermano Braga", 1111111)

primeiro_funcionario_clt = FuncionarioCLT(pessoa01, 1000, 10)
print("CLT: ", primeiro_funcionario_clt.calcularSalario())

primeiro_pj = FuncionarioPJ("Braga Hermano Tangerina", 1000, 6)
print("PJ: ", primeiro_pj.calcularSalario())