import random
from classes.inimigos import *


class Regiao:
    def __init__(self, nome_da_regiao, inimigos):
        self.nome_da_regiao = nome_da_regiao
        self.inimigos = inimigos

    def gerar_inimigos(self):
        return random.sample(self.inimigos, 3)

#TALVEZ POSSA SER UM ARQUIVO CSV
def criar_regioes():
    regioes = [Regiao("Atlântida", [Sereia(), Hidra(), Kraken()]), Regiao("Vulcão", [OrcLava(), ElementalFogo(), DemonioMagma()]), Regiao("Selva", [Serpente(), EspiritoFloresta(), AranhaGigante()])
]