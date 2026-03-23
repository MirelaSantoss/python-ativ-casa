from item import Item

class Porcao (Item):
    def __init__(self, nome, peso, preco, pontos_de_cura): 

        super().__unit__(nome, peso, preco)

        self.pontos_de_cura = pontos_de_cura

    def usar(self):
        print(f"Você bebe {self.nome} e recupera {self.pontos_de_cura}")

