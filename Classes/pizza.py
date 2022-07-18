
class Pizza():
    borda = ''
    tipo_massa = ''
    sabor = ''
    tamanho = ''

    def prepararMassa(self):
        print("Massa batida e assada")

    def incluirIngredientes(self):
        print("Ingredientes inclusos")

    def adicionarBorda(self):
        if self.borda == True:
            print("Borda adicionada")
        else:
            print("Foi sem borda")

    def prepararPizza(self):

        self.prepararMassa()
        self.adicionarBorda()
        self.incluirIngredientes()
        print(f"Pizza de {self.sabor} pronta!")

    def exibirSabor(self):
        print(f'A pizza tem sabor {self.sabor}')

  
qtd = int(input('Digite a qtd de pizzas: '))
lista_pizzas = []
for i in range(qtd):
    primeira_pizza = Pizza()
    primeira_pizza.sabor = input('Digite o sabor da pizza: ')
    primeira_pizza.borda = False
    primeira_pizza.prepararPizza()

    lista_pizzas.append(primeira_pizza)

for pizza in lista_pizzas:
    pizza.exibirSabor()

