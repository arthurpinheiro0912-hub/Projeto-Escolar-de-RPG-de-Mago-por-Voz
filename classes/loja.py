class Loja:
    def __init__(self):
        self._preco_pocao = 15

    def interagir(self, jogador):
        escolha = input("Comprar poção? (s/n): ").lower()

        if escolha == "s":
            if jogador.gastar_moedas(self._preco_pocao):
                jogador.adicionar_pocoes(1)
                print("Poção comprada!")
            else:
                print("Ouro insuficiente")