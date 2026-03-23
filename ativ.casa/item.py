class Item:
    def __init__(self, nome, peso, preco):
        self.nome = nome
        self.peso = peso
        self.preco = preco

    def usar(self):
        print(f"Você segura o item {self.nome}")
