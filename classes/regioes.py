import random
from classes.inimigos import *


class Regiao:
    def __init__(self, nome_da_regiao, inimigos, boss):
        self.nome_da_regiao = nome_da_regiao
        self.inimigos = inimigos
        self.boss = boss

    def gerar_inimigos(self):
        return random.sample(self.inimigos, 3)

#TALVEZ POSSA SER UM ARQUIVO CSV
def criar_regioes():
    regioes = [Regiao("Atlântida", [Sereia(), Hidra(), Kraken()], Leviata()), Regiao("Vulcão", [OrcLava(), ElementalFogo(), DemonioMagma()], Dragao_de_fogo()), Regiao("Selva", [Serpente(), EspiritoFloresta(), AranhaGigante()], Golem_enferrujado())]