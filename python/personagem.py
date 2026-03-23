class Personagem:

    def __init__(self, nome, vida = 100):
        self.nome = nome
        self.vida = vida

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano! Vida: {self.vida}")

    def atacar(): 
        print("ataque Generico!")
        print("10 de Dano")