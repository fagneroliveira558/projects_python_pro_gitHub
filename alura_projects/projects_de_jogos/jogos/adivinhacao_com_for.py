import random

def jogar_jogo_de_adivinhacao():
    print('*'*30)
    print('Sejam bem-vindos(as) ao nosso jogo de adivinhação... ')
    print('*'*30)

    numero_secreto = random.randrange(1, 100)
    total_de_tentativas = 0
    pontos = 1000
    print('Qual o nível de dificuldade você deseja? ')

    print('Preste atenção nas opções abaixo: \n\tDigite (1) e, escolha fácil... \n\tDigite (2) e, escolha médio... \n\tDigite (3) e, escolha difícil. \n\t\tLhe desejo boa sorte maninho...  ')

    nivel_de_jogada = int(input('Defina em qual nível deseja jogar: '))

    if (nivel_de_jogada == 1):
        total_de_tentativas = 20
    elif (nivel_de_jogada == 2):
        total_de_tentativas = 10
    elif (nivel_de_jogada == 3):
        total_de_tentativas = 5
    else:
        print('Ops... O maninho, não exixte esta opção... \n\tNão prestou atenção nas instruções do jogo. \n\t\tLeia novamente com atenção! ')


    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {} '.format(rodada, total_de_tentativas))
        chute_texto = input('E aí maninho... Que número você joga??? \n\t\tDica... Digite apenas números entre (1 ou 100) ')
        print('Você jogou o número: ', chute_texto)
        chute = int(chute_texto)

        if (chute < 1 or chute > 100):
            print('Puts maninho... Não prestou atenção!!! Digite apenas números entre (1 e 100) \n\t\tTome cuidado da próxima... ')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print('Wal... Você acertou meu querido!!! Sensacional!!! \n\t\tVocê é de mais!! \n\t\t\tVocê fez {} pontos! \n\t\t\t\tMeu número secreto, é: {} '.format(pontos, numero_secreto))
            break
        else:
            if (maior):
                print('Puts... Errou maninho!!! Você jogou um número maior que o meu secreto... ')
            elif (menor):
                print('Puts... Maninho, você errou!!! Jogou um número menor que o meu secreto... \n\t\tTente de novo! ')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
    print('Fim do jogo!!!')


if (__name__ == '__main__'):
    jogar_jogo_de_adivinhacao()