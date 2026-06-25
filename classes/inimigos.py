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

#Região de agua
class Sereia(Inimigo):
    def __init__(self):
        super().__init__("Sereia", 40, 10, 10, "grama")


class Hidra(Inimigo):
    def __init__(self):
        super().__init__("Hidra", 70, 15, 20, "grama")


class Kraken(Inimigo):
    def __init__(self):
        super().__init__("Kraken", 60, 12, 15, "grama")
        
#Região de fogo
class OrcLava(Inimigo):
    def __init__(self):
        super().__init__("Orc Lava", 60, 15, 20, "agua")


class ElementalFogo(Inimigo):
    def __init__(self):
        super().__init__("Elemental de Fogo", 80, 18, 25, "agua")


class DemonioMagma(Inimigo):
    def __init__(self):
        super().__init__("Demonio Magma", 90, 20, 30, "agua")

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