from abc import ABC
from classes.magias import MagiaAtaque

class Mago(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.vida_max = 100
        self._vida = 100
        self._mana = 60
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

    def levar_dano(self, dano):
        self._vida = max(0, self._vida - dano)
        print(f"Dano recebido: {dano}")

    def usar_pocao(self):
        if self._pocoes > 0:
            self._pocoes -= 1
            self._vida = min(self.vida_max, self._vida + 40)
            print("Vida regenerada")
        else:
            print("Não possui poções")

    def adicionar_moedas(self, quantidade):
        self._moedas += quantidade

    def gastar_moedas(self, qtd):
        if self._moedas >= qtd:
            self._moedas -= qtd
            return True
        return False

    def aprender_magia(self, magia):
        self._magias[magia.nome.lower()] = magia

class MagoFogo(Mago):
    def __init__(self, nome):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("bola de fogo", 15, 35))

class MagoGelo(Mago):
    def __init__(self, nome):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("lança de gelo", 10, 25))

class MagoPlanta(Mago):
    def __init__(self, nome):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("espinhos", 8, 20))