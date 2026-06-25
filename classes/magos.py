from abc import ABC
from classes.magias import MagiaAtaque

class Mago(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.__vida_max = 200
        self._vida = 200
        self._mana = 300
        self._magias = {}
        self._pocoes = 2
        self._moedas = 0

    @property
    def vida(self):
        return self._vida

    @property
    def mana(self):
        return self._mana

    @property
    def magias(self):
        return self._magias
    
    @property
    def pocoes(self):
        return self._pocoes

    @property
    def moedas(self):
        return self._moedas

    def gastar_mana(self, quantidade):
        if self._mana >= quantidade:
            self._mana -= quantidade
            return True
        return False

    def receber_dano(self, dano):
        self._vida = max(0, self._vida - dano)
        print(f"Dano recebido: {dano}")

    def usar_pocao(self):
        if self._pocoes > 0:
            self._pocoes -= 1
            self._vida = min(self.__vida_max, self._vida + 40)
            print("Vida regenerada")
        else:
            print("Não possui poções")

    def adicionar_moedas(self, quantidade):
        self._moedas += quantidade

    def gastar_moedas(self, quantidade):
        if self._moedas >= quantidade:
            self._moedas -= quantidade
            return True
        return False

    def adicionar_pocoes(self, quantidade):
        self._pocoes += quantidade

    def aprender_magia(self, magia):
        self._magias[magia.nome_magia.lower()] = magia

class MagoFogo(Mago):
    def __init__(self, nome):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("bola de fogo", 15, "fogo", 35))

class MagoAgua(Mago):
    def __init__(self, nome):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("Jato de Água", 10, "agua", 25))

class MagoPlanta(Mago):
    def __init__(self, nome):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("espinhos", 8, "grama", 20))