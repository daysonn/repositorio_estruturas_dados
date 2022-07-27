'''
### Questionário ###
- Participante
- Data
- Idade
- Genero
- Localização
- Perguntas
- Respostas
- Opções de respostas
'''

# 1 - O Entrevistador cadastra as perguntas
# 2 - O entrevistador decide quantas pessoas ele vai entrevistar naquele dia
# 3 - O entrevistado responde as perguntas cadastradas

class Questionario:
    
    def __init__(self, participante, idade, genero, localizacao, dicionario_perguntas):
        self.participante = participante
        self.idade = idade
        self.genero = genero
        self.localizacao = localizacao
        self.dicionario_perguntas_respostas = dict(dicionario_perguntas)

    def cadastrarRespostas(self):
        for pergunta in self.dicionario_perguntas_respostas:
            resposta = input(pergunta + '\n')
            self.dicionario_perguntas_respostas[pergunta] = resposta

    def exibirTodasRespostas(self):
        for pergunta in self.dicionario_perguntas_respostas:
            print(pergunta + ' ' + self.dicionario_perguntas_respostas[pergunta])
        
# Opção 02: criar um dicionario somente com as perguntas como chaves e copia-los para a classe questionario
dicionario_perguntas = {}
fila = []

# 1 - O Entrevistador cadastra as perguntas:
resposta_entrevistador = input("Deseja digitar uma nova pergunta? [Sim ou Não] ")
while(resposta_entrevistador != 'Não'):
    pergunta_cadastrada = input("Favor digitar a pergunta: ")
    dicionario_perguntas[pergunta_cadastrada] = ''
    resposta_entrevistador = input("Deseja digitar uma nova pergunta? [Sim ou Não]")

# 2 - O entrevistador decide quantas pessoas vai entrevistar naquele dia
qtd_entrevistados = int(input("Digite a meta de entrevistados para o dia: "))
data_entrevista = input("Digite a data da entrevista: ")

# 3 - O entrevistado responde as perguntas cadastradas
for i in range(qtd_entrevistados):
    nome_participante = input("Digite o nome do participante: ")
    idade = input("Digite a idade do participante: ")
    genero = input("Digite o genero do participante: ")
    localizacao = input("Digite a localização do participante: ")

    resposta = Questionario(nome_participante, idade, genero, localizacao, dicionario_perguntas)
    resposta.cadastrarRespostas()

    fila.append(resposta)

for cada_entrevistado in fila:
    print(f"O participante: {cada_entrevistado.participante} teve as seguintes respostas:\n")
    cada_entrevistado.exibirTodasRespostas()

'''
No processo paralelo:
def funcaoRecebeFila(fila):
    if fila::
        resposta = fila.pop(0)
        return fresposta
'''