from personagem import Personagem

class Chefe (Personagem):
    def receber_dano(self,dano):
        dano_real = dano/ 2
        super().receber_dano(dano_real)