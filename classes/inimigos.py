from abc import ABC
class Inimigo(ABC):
    def __init__(self, nome, vida, dano, moedas, fraqueza):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.moedas = moedas
        self.fraqueza = fraqueza

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)

    def esta_morto(self):
        return self.vida <= 0

#Região de gelo
class GoblinGelo(Inimigo):
    def __init__(self):
        super().__init__("Goblin de Gelo", 40, 10, 10, "grama")


class Yeti(Inimigo):
    def __init__(self):
        super().__init__("Yeti", 70, 15, 20, "grama")


class EspiritoArtico(Inimigo):
    def __init__(self):
        super().__init__("Espírito Ártico", 60, 12, 15, "grama")
        
#Fegião de fogo
class OrcLava(Inimigo):
    def __init__(self):
        super().__init__("Orc Lava", 60, 15, 20, "gelo")


class ElementalFogo(Inimigo):
    def __init__(self):
        super().__init__("Elemental de Fogo", 80, 18, 25, "gelo")


class DemonioMagma(Inimigo):
    def __init__(self):
        super().__init__("Demonio Magma", 90, 20, 30, "gelo")

#Região da selva
class Serpente(Inimigo):
    def __init__(self):
        super().__init__("Serpente", 50, 12, 10, "fogo")


class EspiritoFloresta(Inimigo):
    def __init__(self):
        super().__init__("Espírito da Floresta", 70, 15, 20, "fogo")


class AranhaGigante(Inimigo):
    def __init__(self):
        super().__init__("Aranha Gigante", 65, 14, 18, "fogo")

#Boss Final
class BossFinal(Inimigo):
    def __init__(self):
        super().__init__("Malakar", 200, 25, 100, "nenhuma")