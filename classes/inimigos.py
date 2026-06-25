from abc import ABC
from classes.magias import MagiaAtaque
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
        super().__init__("Hidra", 70, 15, 15, "grama")


class Kraken(Inimigo):
    def __init__(self):
        super().__init__("Kraken", 60, 20, 20, "grama")

class Leviata(Inimigo):
    def __init__(self):
        super().__init__("Leviata", 100, 30, 90, "grama")

    def drop_magia(self):
        return MagiaAtaque("Tsunami", 25, "agua", 45)
        
        
#Região de fogo
class OrcLava(Inimigo):
    def __init__(self):
        super().__init__("Orc Lava", 60, 20, 35, "agua")


class ElementalFogo(Inimigo):
    def __init__(self):
        super().__init__("Elemental de Fogo", 80, 25, 45, "agua")


class DemonioMagma(Inimigo):
    def __init__(self):
        super().__init__("Demonio Magma", 100, 30, 50, "agua")

class Dragao_de_fogo(Inimigo):
    def __init__(self):
        super().__init__("Dragão de Fogo", 150, 40, 130, "agua")
    
    def drop_magia(self):
        return MagiaAtaque("Fogo Abrasador", 30, "fogo", 50)

#Região da selva
class Serpente(Inimigo):
    def __init__(self):
        super().__init__("Serpente", 50, 15, 25, "fogo")


class EspiritoFloresta(Inimigo):
    def __init__(self):
        super().__init__("Espírito da Floresta", 65, 23, 30, "fogo")


class AranhaGigante(Inimigo):
    def __init__(self):
        super().__init__("Aranha Gigante", 70, 28, 40, "fogo")

class Golem_enferrujado(Inimigo):
    def __init__(self):
        super().__init__("Golem Enferrujado", 120, 40, 110, "fogo")
    
    def drop_magia(self):
        return MagiaAtaque("Escudo de Metal", 20, "terra", 35)


#Boss Final
class BossFinal(Inimigo):
    def __init__(self):
        super().__init__("Malakar", 200, 25, 100, "nenhuma")
    
    def drop_magia(self):
        return MagiaAtaque("Fogo Primordial", 40, "fogo", 60)