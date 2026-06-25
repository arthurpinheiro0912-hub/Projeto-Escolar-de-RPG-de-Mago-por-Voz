import time
from classes.loja import Loja
def exibir_status(mago, inimigo):
    print("\n========================")
    print(f"{mago.nome} | Vida: {mago.vida} | Mana: {mago.mana} | Poções: {mago.pocoes}")
    print(f"{inimigo.nome} | Vida: {inimigo.vida}")
    print("========================\n")


def turno_jogador(mago, inimigo):
    print("Escolha sua ação:")
    print("1 - Usar magia")
    print("2 - Usar poção")
    print("3 - Loja")

    escolha = input("> ")

    if escolha == "1":
        if not mago.magias:
            print("Você não possui magias!")
            return

        print("\nMagias disponíveis:")
        for i, magia in enumerate(mago.magias.values(), start=1):
            print(f"{i} - {magia.nome_magia} (Mana: {magia.custo_mana})")

        try:
            opcao = int(input("> ")) - 1
            magia = list(mago.magias.values())[opcao]

            if mago.gastar_mana(magia.custo_mana):
                magia.atacar(mago, inimigo)
            else:
                print("Mana insuficiente!")

        except (ValueError, IndexError):
            print("Escolha inválida!")

    elif escolha == "2":
        mago.usar_pocao()

    elif escolha == "3":
        loja = Loja()
        loja.interagir(mago)




def turno_inimigo(mago, inimigo):
    if inimigo.esta_morto():
        return

    print(f"\n{inimigo.nome} ataca!")
    mago.receber_dano(inimigo.dano)


def combate(mago, inimigo):
    print(f"\n🔥 Um {inimigo.nome} apareceu!\n")

    while True:
        exibir_status(mago, inimigo)

        # Turno do jogador
        turno_jogador(mago, inimigo)

        if inimigo.esta_morto():
            print(f"\n✅ Você derrotou {inimigo.nome}!")
            mago.adicionar_moedas(inimigo.moedas)
            print(f"Você ganhou {inimigo.moedas} moedas!")
            
            # Verificar se o inimigo dropará uma magia
            if hasattr(inimigo, 'drop_magia'):
                magia = inimigo.drop_magia()
                if magia:
                    print(f"\n⭐ {inimigo.nome} dropou uma magia: {magia.nome_magia}!")
                    mago.aprender_magia(magia)
            break

        time.sleep(1)

        # Turno do inimigo
        turno_inimigo(mago, inimigo)

        if mago.vida <= 0:
            print("\n💀 Você foi derrotado!")
            return False

        time.sleep(1)

    return True