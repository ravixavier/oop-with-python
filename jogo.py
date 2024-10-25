# Personagem: classe mae
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario

import random
import math

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def ataque_normal(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_dano(dano)
        print(f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!')


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        self.__pontos_de_sangue = math.ceil(self.get_nivel() / 2)

    def get_habilidade(self):
        return self.__habilidade

    def get_pontos_de_sangue(self):
        return self.__pontos_de_sangue

    def gastar_ponto_de_sangue(self):
        self.__pontos_de_sangue -= 1
        if self.__pontos_de_sangue < 0:
            self.__pontos_de_sangue = 0

    def exibir_detalhes(self):
        return (f'{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\nPontos de Sangue:'
                f' {self.get_pontos_de_sangue()}\n')


    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 4, self.get_nivel() * 6)
        alvo.receber_dano(dano)
        print(f'{self.get_nome()} usou o ataque especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!')


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f'{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n'


class Jogo:
    """" classe orquestradora do jogo """
    def __init__(self):
        self.heroi = Heroi('Heroi', 130, 6, 'Potencia')
        self.inimigo = Inimigo("Lobisomem", 150, 7, 'Sobrenatural')

    def iniciar_batalha(self):
        print('Iniciando batalha:')
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print('\nTurno dos personagens:\n')
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input('Precione Enter para atacar.')
            escolha = input('Escolha (1 - Ataque Normal, 2 - Ataque Especial): ')

            if escolha == '1':
                self.heroi.ataque_normal(self.inimigo)
            elif escolha == '2':
                if self.heroi.get_pontos_de_sangue() > 0:
                    self.heroi.ataque_especial(self.inimigo)
                    self.heroi.gastar_ponto_de_sangue()
                else:
                    print('O heroi não pode mais utilizar esse poder.')
                    print('O heroi irá atacar normalmente')
                    self.heroi.ataque_normal(self.inimigo)
            else:
                print('Escolha invalida. Escolha novamente.')

            if self.inimigo.get_vida() > 0:
                # Inimigo ataca o heroi
                self.inimigo.ataque_normal(self.heroi)


        if self.heroi.get_vida() > 0 :
            print('\nParabéns! Você venceu a batalha!')
        else:
            print('\nVocê foi derrotado!')

# Criar instancia do jogo e inicar a batalha
jogo = Jogo()
jogo.iniciar_batalha()