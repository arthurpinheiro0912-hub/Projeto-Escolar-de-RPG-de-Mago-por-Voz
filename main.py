from classes.magos import MagoFogo, MagoAgua, MagoPlanta
from classes.inimigos import Sereia, Hidra, Kraken, Leviata, OrcLava, ElementalFogo, DemonioMagma, Dragao_de_fogo, Serpente, EspiritoFloresta, AranhaGigante, Golem_enferrujado, BossFinal
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


def escolher_regiao():
    print("\n=== ESCOLHA SUA REGIÃO ===")
    print("1 - Região da Água")
    print("2 - Região do Fogo")
    print("3 - Região da Selva")
    
    escolha = input("> ")
    return escolha


def minichefes_regiao(regiao):
    """Retorna lista de mini-chefes da região"""
    minichefes = {
        "1": [Sereia(), Hidra(), Kraken()],
        "2": [OrcLava(), ElementalFogo(), DemonioMagma()],
        "3": [Serpente(), EspiritoFloresta(), AranhaGigante()]
    }
    return minichefes.get(regiao, [])


def boss_regiao(regiao):
    """Retorna o boss da região"""
    bosses = {
        "1": Leviata(),
        "2": Dragao_de_fogo(),
        "3": Golem_enferrujado()
    }
    return bosses.get(regiao)


def main():
    mago = escolher_mago()
    
    regioes_feitas = []
    regiao_nomes = {"1": "Água", "2": "Fogo", "3": "Selva"}
    
    while len(regioes_feitas) < 3:
        # Escolher região
        regiao = escolher_regiao()
        
        if regiao in regioes_feitas:
            print("Você já completou essa região!")
            continue
        
        print(f"\n Você entrou na Região de {regiao_nomes.get(regiao, 'Desconhecida')}!\n")
        
        # Combate com mini-chefes
        minichefes = minichefes_regiao(regiao)
        venceu = True
        
        for minichefe in minichefes:
            if not combate(mago, minichefe):
                print(f"\n Você foi derrotado!")
                return
            print(f"\n {minichefe.nome} foi derrotado!")
        
        # Combate com o boss
        print(f"\n O BOSS APARECEU!")
        boss = boss_regiao(regiao)

        if combate(mago, boss):
            print(f"\n Boss derrotado: {boss.nome}!")
            regioes_feitas.append(regiao)
            print(f"Regiões conquistadas: {len(regioes_feitas)}/3")

        else:
            print(f"\n Você Perdeu!")
            return
    
    print("\n VOCÊ VENCEU O JOGO! ")


if __name__ == "__main__":
    main()