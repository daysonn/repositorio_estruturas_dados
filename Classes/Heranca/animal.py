
class Animal:
    def __init__(self, especie):
        self.especie = especie

    def locomover(self):
        print("Animal se locomoveu")

class Mamifero(Animal):
    def __init__(self, especie, temPatas):
        Animal.__init__(self,especie)
        self.patas = temPatas

    def locomover(self):
        if self.patas:
            print("Mamífero andou")
        else:
            print("Mamífero se locomoveu")

class Peixe(Animal):
    def __init__(self, especie, temEscamas):
        Animal.__init__(self,especie)
        self.escamas = temEscamas

    def locomover(self):
        print("Peixe nadou")

primeiro_mamifero = Mamifero("Felis catus", True)
primeiro_peixe = Peixe("Salminus brasiliensis", True)

primeiro_mamifero.locomover()
primeiro_peixe.locomover()