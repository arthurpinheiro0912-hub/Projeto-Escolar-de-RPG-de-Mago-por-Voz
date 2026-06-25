import random
from classes.inimigos import Inimigo


class Regiao:
    def __init__(self, nome, inimigos):
        self.nome = nome
        self.inimigos = inimigos

    def gerar_inimigos(self):
        return random.sample(self.inimigos, 3)

#TALVEZ POSSA SER UM ARQUIVO CSV
def criar_regioes():
    return [
        Regiao("Montanhas Congeladas", [
            Inimigo("Goblin de Gelo", 40, 10, 10),
            Inimigo("Yeti", 70, 15, 20),
            Inimigo("Espírito Ártico", 60, 12, 15),
        ]),

        Regiao("Vulcão", [
            Inimigo("Orc Lava", 60, 15, 20),
            Inimigo("Elemental de Fogo", 80, 18, 25),
            Inimigo("Demonio Magma", 90, 20, 30),
        ]),

        Regiao("Selva", [
            Inimigo("Serpente", 50, 12, 10),
            Inimigo("Espírito da Floresta", 70, 15, 20),
            Inimigo("Aranha Gigante", 65, 14, 18),
        ])
    ]