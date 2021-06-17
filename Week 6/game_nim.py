"""

Created on Wed May 26 09:01:11 2021 - BH, Brazil

@author: Davidson Prata

"""


def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m


def usuario_escolhe_jogada(n, m):
    x = int(input("Quantas peças você vai tirar? "))
    while x > m or x <= 0 or x > n:
        print("Não consegue né?! Jogada inválida! Tente de novo.")
        x = int(input("Quantas peças você vai tirar? "))
    return x


def partida():
    n = int(input("Quantas peças desta partida? "))
    m = int(input("Qual o limite de peças por jogada? "))
    while m < 1:
        print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais")
        m = int(input("Limite de peças por jogada? "))

    x = 0
    jogada = 0
    if (n % (m+1)) == 0:
        print("Você começa!")
        jogada = 1
        while n > 0:
            if jogada == 1:
                x = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", x, "peça(s).")
                n = n - x
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
            else:
                x = computador_escolhe_jogada(n, m)
                print("O computador tirou", x, "peça(s)")
                n = n - x
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1

        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1

    else:
        print("\nComputador começa!")
        jogada = 2
        while n > 0:
            if jogada == 2:
                x = computador_escolhe_jogada(n, m)
                print("O computador tirou", x, "peça(s)")
                n = n - x
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
            else:
                x = usuario_escolhe_jogada(n, m)
                print("Você tirou", x, "peça(s).")
                n = n - x
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2

        if jogada == 1:
            print("Fim do jogo! O computador ganhou!")
            return 2
        else:
            print("Fim do jogo! O você ganhou!")
            return 1


def campeonato():
    quantidade_partida = 1
    placar_computador = placar_usuario = 0

    while quantidade_partida < 4:
        print("######## Rodada", quantidade_partida, "########")
        if partida() == 1:
            placar_usuario = placar_usuario + 1
        else:
            placar_computador = placar_computador + 1
        quantidade_partida = quantidade_partida + 1
    print("######## Final do campeonato! ########")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")


def main():
    print("Olá! Seja bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input("Escolha: "))
    while escolha != 1 and escolha != 2:
        print("Escolha uma opção válida!")
        escolha = int(input("Escolha: "))
    if escolha == 1:
        print("OK! Você escolheu uma partida isolada! Vamos lá!!!")
        partida()
    else:
        if escolha == 2:
            print("OK! Você escolheu um campeonato! Vamos lá!!!")
            campeonato()


main()
