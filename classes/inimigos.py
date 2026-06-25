class Inimigo:
    def __init__(self, nome, vida, dano, moedas):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.moedas = moedas

    def receber_dano(self, qtd):
        self.vida = max(0, self.vida - qtd)

    def esta_morto(self):
        return self.vida <= 0


class BossFinal(Inimigo):
    def __init__(self):
        super().__init__("Malakar", 200, 25, 100)