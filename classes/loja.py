class Loja:
    def __init__(self):
        self.preco_pocao = 15

    def interagir(self, jogador):
        escolha = input("Comprar poção? (s/n): ").lower()

        if escolha == "s":
            if jogador.gastar_moedas(self.preco_pocao):
                jogador._pocoes += 1
                print("Poção comprada!")
            else:
                print("Ouro insuficiente")