
# Declaração da classe lâmpada
class Lampada():
    cor = "Amarela"
    acesa = False

    # Método para acender a classe lâmpada
    def acender(self):
        if not self.acesa:
            self.acesa = True
            print("Lâmpada acesa")
        else:
            print("Esta lâmpada já está acesa")

    # Método para apagar a lâmpada...
    def apagar(self):

        if self.acesa: # Se a lampada estiver acesa
            self.acesa = False
            print("Lâmpada apagada")
        else:
            print("Esta lâmpada já está apagada")