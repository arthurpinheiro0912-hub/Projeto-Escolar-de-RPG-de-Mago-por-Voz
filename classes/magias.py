from abc import ABC, abstractmethod


class Magia(ABC):
    def __init__(self, nome, custo_mana):
        self.nome = nome
        self.custo_mana = custo_mana

    @abstractmethod
    def conjurar(self, conjurador, alvo):
        pass


class MagiaAtaque(Magia):
    def __init__(self, nome, custo_mana, dano):
        super().__init__(nome, custo_mana)
        self.dano = dano

    def conjurar(self, conjurador, alvo):
        print(f"{conjurador.nome} usou {self.nome}")
        alvo.receber_dano(self.dano)