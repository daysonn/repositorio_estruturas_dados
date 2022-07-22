
class Carro():
    #Posso colocar valores padrão?
    cor = "preto"
    chassi = ''
    blindagem = False
    motor = ''
    ano = 00 
    sensor = False

    def __init__(self, rodas, capacidadeTanque, modelo, nroPortas):
        self.rodas = rodas
        self.qtdLitrosTanque = capacidadeTanque
        self.modelo = modelo
        self.portas = nroPortas

    def setCor(self, novaCor):
        lista_cores_disponiveis = ['amarelo', 'branco', 'azul']

        if novaCor not in lista_cores_disponiveis:
            print('Esta cor não está disponível')
        else:
            self.cor = novaCor
            print(" Nova cor atribuída ao carro.")

    def getCort(self):
        return self.cor

# E na hora de instanciar a classe...
rodas = input("Digite a qtd de rodas: ")
primeiro_carro = Carro(rodas, 30, 'Ford', 4)
novaCor = input('Digite a nova cor do carro')
primeiro_carro.setCor(novaCor)