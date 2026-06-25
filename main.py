from classes.magos import MagoFogo, MagoGelo, MagoPlanta
from classes.inimigos import GoblinGelo
from sistemas.combate import combate

def escolher_mago():
    print("Escolha seu mago:")
    print("1 - Mago de Fogo")
    print("2 - Mago de Gelo")
    print("3 - Mago de Planta")

    escolha = input("> ")
    nome = input("Nome do seu mago: ")

    if escolha == "1":
        return MagoFogo(nome)
    elif escolha == "2":
        return MagoGelo(nome)
    else:
        return MagoPlanta(nome)


def main():
    mago = escolher_mago()

    inimigo = GoblinGelo()

    combate(mago, inimigo)


if __name__ == "__main__":
    main()