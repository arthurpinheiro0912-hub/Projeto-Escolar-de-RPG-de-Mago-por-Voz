from classes.magos import MagoFogo, MagoAgua, MagoPlanta
from classes.inimigos import Sereia
from sistemas.combate import combate

def escolher_mago():
    nome = input("Nome do seu mago: ")
    print("Escolha seu mago:")
    print("1 - Mago de Fogo")
    print("2 - Mago de Agua")
    print("3 - Mago de Planta")

    escolha = input("> ")

    if escolha == "1":
        return MagoFogo(nome)
    elif escolha == "2":
        return MagoAgua(nome)
    else:
        return MagoPlanta(nome)


def main():
    mago = escolher_mago()

    inimigo = Sereia()

    combate(mago, inimigo)


if __name__ == "__main__":
    main()