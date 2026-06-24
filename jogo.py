import os
import sys
import json
import queue
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from abc import ABC, abstractmethod

# ==============================================================================
# 1. MOTOR DE ENTRADA (Gerencia se o input vem da Voz ou do Teclado)
# ==============================================================================
class MotorEntrada:
    def __init__(self, modo: str, caminho_modelo="."):
        self.modo = modo  # "1" para voz, "2" para teclado
        self.modelo = None
        self.reconhecedor = None
        self.fila_audio = queue.Queue()

        if self.modo == "1":
            if not os.path.exists(os.path.join(caminho_modelo, "am")) and not os.path.exists(caminho_modelo):
                print(f"❌ Erro: Arquivos do modelo do Vosk não encontrados em '{caminho_modelo}'!")
                sys.exit(1)
            
            print("\n🔮 Sintonizando plano astral e carregando feitiços (Carregando Vosk)...")
            self.modelo = Model(caminho_modelo)
            self.reconhecedor = KaldiRecognizer(self.modelo, 16000)

    def _callback_audio(self, indata, frames, time, status):
        if status:
            print(status, file=sys.stderr)
        self.fila_audio.put(bytes(indata))

    def obter_comando(self, mensagem_prompt: str) -> str:
        """Obtém o comando do usuário via microfone ou via teclado dependendo do modo."""
        # MODO 2: TECLADO (Sem microfone)
        if self.modo == "2":
            print(f"\n⌨️  {mensagem_prompt}")
            return input("Digite seu comando: ").strip().lower()

        # MODO 1: VOZ (Microfone)
        print(f"\n🎙️  {mensagem_prompt}")
        print("[Microfone Ativo] Diga seu comando agora...")
        self.fila_audio.queue.clear()
        
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=self._callback_audio):
            while True:
                dados = self.fila_audio.get()
                if self.reconhecedor.AcceptWaveform(dados):
                    resultado = json.loads(self.reconhecedor.Result())
                    texto_reconhecido = resultado.get("text", "").strip()
                    if texto_reconhecido:
                        return texto_reconhecido

# ==============================================================================
# 2. SISTEMA DE MAGIAS (Abstração, Herança e Polimorfismo)
# ==============================================================================
class Magia(ABC):
    def __init__(self, nome: str, comando_voz: str, custo_mana: int):
        self.nome = nome
        self.comando_voz = comando_voz
        self.custo_mana = custo_mana

    @abstractmethod
    def conjurar(self, conjurador, alvo):
        pass

class MagiaAtaque(Magia):
    def __init__(self, nome: str, comando_voz: str, custo_mana: int, dano: int):
        super().__init__(nome, comando_voz, custo_mana)
        self.dano = dano

    def conjurar(self, conjurador, alvo):
        print(f"\n💥 {conjurador.nome} executou {self.nome}!")
        alvo.receber_dano(self.dano)

# ==============================================================================
# 3. SISTEMA DE PERSONAGENS (Encapsulamento e Herança)
# ==============================================================================
class Mago(ABC):
    def __init__(self, nome: str):
        self.nome = nome
        self.vida_max = 100
        self._vida = 100
        self._mana = 60
        self.__moedas = 0
        self.__pocoes_cura = 0
        self._magias = {}

    @property
    def moedas(self): return self.__moedas

    @property
    def vida(self): return self._vida

    @property
    def mana(self): return self._mana

    def adicionar_moedas(self, qtd: int):
        self.__moedas += qtd
        print(f"💰 +{qtd} moedas adicionadas à sua bolsa!")

    def gastar_moedas(self, qtd: int) -> bool:
        if self.__moedas >= qtd:
            self.__moedas -= qtd
            return True
        return False

    def comprar_pocao(self):
        self.__pocoes_cura += 1
        print(f"🧪 Poção guardada no inventário! Total: {self.__pocoes_cura}")

    def usar_pocao(self):
        if self.__pocoes_cura > 0:
            self.__pocoes_cura -= 1
            self._vida = min(self.vida_max, self._vida + 40)
            print(f"✨ Você usou uma poção de cura e recuperou 40 de vida! Vida atual: {self._vida}")
        else:
            print("❌ Você não possui poções de cura!")

    def receber_dano(self, qtd: int):
        self._vida = max(0, self._vida - qtd)
        print(f"🤕 {self.nome} sofreu {qtd} de dano! Vida restante: {self._vida}")

    def aprender_magia(self, magia: Magia):
        self._magias[magia.comando_voz] = magia

class MagoGelo(Mago):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("Lança de Gelo", "lanca de gelo", custo_mana=10, dano=25))

class MagoFogo(Mago):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("Bola de Fogo", "bola de fogo", custo_mana=15, dano=35))

class MagoAgua(Mago):
    def __init__(self, nome: str):
        super().__init__(nome)
        self.aprender_magia(MagiaAtaque("Jato de Água", "jato de agua", custo_mana=8, dano=20))

class Inimigo:
    def __init__(self, nome: str, vida: int, dano: int, moedas_drop: int):
        self.nome = nome
        self.vida = vida
        self.dano = dano
        self.__moedas_drop = moedas_drop

    def receber_dano(self, qtd: int):
        self.vida = max(0, self.vida - qtd)
        print(f"🎯 {self.nome} sofreu {qtd} de dano! Vida do monstro: {self.vida}")

    def esta_morto(self) -> bool: return self.vida <= 0
    def soltar_drop(self) -> int: return self.__moedas_drop

class Loja:
    def __init__(self):
        self.preco_pocao = 15

    def interagir(self, mago: Mago, comando: str):
        if "comprar" in comando or "pocao" in comando:
            if mago.gastar_moedas(self.preco_pocao):
                mago.comprar_pocao()
            else:
                print("❌ Ouro insuficiente! A poção custa 15 moedas.")

# ==============================================================================
# 4. LOOP PRINCIPAL DO JOGO (Execução)
# ==============================================================================
if __name__ == "__main__":
    print("========================================")
    print("      🧙‍♂️ BEM-VINDO AO MAGO DE VOZ 🧙‍♂️    ")
    print("========================================")
    
    print("\nComo deseja controlar as suas magias?")
    print("[ 1 ] Usar Microfone (Falar comandos)")
    print("[ 2 ] Usar Teclado (Digitar comandos)")
    
    modo_escolhido = ""
    while modo_escolhido not in ["1", "2"]:
        modo_escolhido = input("Escolha o modo (1 ou 2): ").strip()
    
    # Passamos "." assumindo que o código está rodando direto de dentro da pasta do modelo
    motor = MotorEntrada(modo=modo_escolhido, caminho_modelo=".")
    
    # Seleção de Região
    jogador = None
    while jogador is None:
        fala = motor.obter_comando("Escolha sua Região de Origem (diga ou digite: 'gelo', 'deserto' ou 'praia')")
        print(f"📝 Comando interpretado: '{fala}'")
        
        if "gelo" in fala:
            jogador = MagoGelo("Merlin de Gelo")
            print("🏔️ Classe definida: Mago do Gelo! Magia inicial: 'lanca de gelo'")
        elif "deserto" in fala:
            jogador = MagoFogo("Merlin de Fogo")
            print("🌵 Classe definida: Mago do Fogo! Magia inicial: 'bola de fogo'")
        elif "praia" in fala:
            jogador = MagoAgua("Merlin da Água")
            print("🏖️ Classe definida: Mago da Água! Magia inicial: 'jato de agua'")
        else:
            print("❓ Comando inválido. Tente novamente.")

    # --- FASE 1: COMBATE ---
    orc = Inimigo("Orc da Caverna", vida=60, dano=15, moedas_drop=30)
    print(f"\n👹 Um {orc.nome} bloqueia seu caminho!")
    
    while not orc.esta_morto() and jogador.vida > 0:
        print(f"\n[SUA VEZ] Vida: {jogador.vida} | Mana: {jogador.mana}")
        fala = motor.obter_comando("Diga ou digite sua magia de ataque ou 'usar pocao'")
        print(f"📝 Comando interpretado: '{fala}'")
        
        if fala == "usar pocao":
            jogador.usar_pocao()
        elif fala in jogador._magias:
            magia = jogador._magias[fala]
            if jogador.mana >= magia.custo_mana:
                jogador._mana -= magia.custo_mana
                magia.conjurar(jogador, orc)
            else:
                print("❌ Sem mana suficiente!")
        else:
            print(f"💨 O feitiço falhou! O comando '{fala}' não gerou energia mágica.")
        
        if not orc.esta_morto():
            print(f"\n[TURNO DO INIMIGO] O {orc.nome} te ataca!")
            jogador.receber_dano(orc.dano)
            
    if jogador.vida <= 0:
        print("\n💀 Você foi derrotado! Fim de jogo.")
        sys.exit()
        
    print(f"\n🎉 Você derrotou o {orc.nome}!")
    jogador.adicionar_moedas(orc.soltar_drop())

    # --- FASE 2: A LOJINHA ---
    lojinha = Loja()
    print(f"\n========================================")
    print(f"🛒 Você entrou na Loja! Moedas: {jogador.moedas}")
    print("========================================")
    
    while True:
        fala = motor.obter_comando("Diga ou digite 'comprar pocao' ou 'sair'")
        print(f"📝 Comando interpretado: '{fala}'")
        
        if "sair" in fala:
            print("👋 Você saiu da loja!")
            break
        elif "comprar" in fala or "pocao" in fala:
            lojinha.interagir(jogador, "comprar pocao")
            print(f"Carteira atual: {jogador.moedas} moedas.")
        else:
            print("❓ O mercador não entendeu o comando.")

    print("\n👑 Fim da demonstração do jogo!")
