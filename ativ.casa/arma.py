from item import Item

class Arma (Item):
    def __init__(self, nome, peso, preco, dano_de_ataque):
        
            super().__unit__(nome, peso, preco)

        self.dano_de_ataque = dano_de_ataque

    def usar(self):
        print(f"Você bebe {self.nome} e recupera {self.dano_de_ataque}")