from personagem import Personagem

class Guerreiro (Personagem):
    def __init__(self, nome, forca_bruta, vida = 100):
        super().__init__(nome, vida)
        self.forca_bruta = forca_bruta

    def atacar(self):
        print(f"Perfurada de lança! {self.forca_bruta}")
        return 50