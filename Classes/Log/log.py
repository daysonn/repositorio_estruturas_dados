class Categoria:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

class Evento:
    def __init__(self, titulo, data, categoria):
        self.titulo = titulo
        self.data = data
        self.categoria = categoria

def checarSeEventoExiste(evento, lista_de_eventos):
    for objeto in lista_de_eventos:
        if evento == objeto.titulo:
            return True
    return False


lista_categorias = ['Jornada Corporativa', 'Meetups', 'SER', 'Apresentação de módulo', 'Campeonato de Jogos']
lista_eventos = []

jornadaCorporativa = Categoria('Jornada Corporativa', 'Categoria que define Jornada corporativa ocorrida na Resilia')
meetUP = Categoria('Meetup', 'Descrição meetup')
ser = Categoria('SER', 'Semana de Empregabilidade da Resilia')
ppt = Categoria('Apresentação', 'Apresentação de módulo')
jogo = Categoria('Campeonato de Jogos', 'Breve descrição')

while True:
    eventonovo = input("Deseja inserir um evento novo? [Sim ou Não] ")
    if (eventonovo == 'Sim'):
        # Print do que há de opções na lista de categorias
        for i,j in enumerate(lista_categorias,start=1):
            print(f'{i}: {j}')

        escolha_categoria = int(input("Escolha uma categoria acima digitando seu índice:\n"))
        tituloEvento = input("Qual novo título de evento deseja registrar? ")
        data = input("Digite a data do evento: ")

        if escolha_categoria == 1:
            categoria = jornadaCorporativa
        elif escolha_categoria == 2:
            categoria = meetUP
        elif escolha_categoria == 3:
            categoria = ser
        elif escolha_categoria == 4:
            categoria = ppt
        else:
            categoria = jogo
        
        if not checarSeEventoExiste(tituloEvento, lista_eventos):
            novoEvento = Evento(tituloEvento, data, categoria)
            lista_eventos.append(novoEvento)
    else:
        break

arquivo = open('novo-arquivo.txt', 'a', encoding='utf-8')
for evento in lista_eventos:
    arquivo.write(f'{evento.titulo}, {evento.data}, {evento.categoria.titulo}\n')
arquivo.close() 

