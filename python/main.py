from dragao import Dragao
from guerreiro import Guerreiro
from chefe import Chefe
from inimigo import Inimigo
from mago import Mago

guerreiro_principal = Guerreiro("Guerreiro", 30, 200)
print(f"O nome do guerreiro principal é {guerreiro_principal.nome}")

guerreiro_principal.vida = 150

print(f"vida do Guerreiro principal: {guerreiro_principal.vida}")

guerreiro_principal.receber_dano(32)

mago_principal = Mago("Mago")
orc = Inimigo("Orc")

orc.receber_dano(mago_principal.atacar())
orc.receber_dano(guerreiro_principal.atacar())

obelisco = Chefe("Obelisco")
obelisco.receber_dano(guerreiro_principal.atacar())

obelisco.receber_dano(mago_principal.atacar())

banguela = Dragao("Banguela", 500)

banguela.voar()

mago_principal.receber_dano(banguela.atacar())

print(Dragao.mro())
