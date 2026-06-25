from abc import ABC, abstractmethod

class Magia(ABC):
    def __init__(self, nome_magia, custo_mana, tipo_de_magia):
        self.nome_magia = nome_magia
        self.custo_mana = custo_mana
        self.tipo_de_magia = tipo_de_magia

    @abstractmethod
    def atacar(self, conjurador):
        pass


class MagiaAtaque(Magia):
    def __init__(self, nome, custo_mana, tipo_de_magia, dano):
        super().__init__(nome, custo_mana, tipo_de_magia)
        self.dano = dano

    def atacar(self, conjurador, alvo):
        if self.tipo_de_magia == alvo.fraqueza:
            dano_final = self.dano + 5
            print(f"{conjurador.nome} usou {self.nome_magia}, que é crítica, dando 5 de dano extra")
            alvo.receber_dano(dano_final) 
        else:
            print(f"{conjurador.nome} usou {self.nome_magia}")
            alvo.receber_dano(self.dano)