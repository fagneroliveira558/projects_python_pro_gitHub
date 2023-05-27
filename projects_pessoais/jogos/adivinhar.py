

def jogo_de_adivinhar():
    print('-'*30)
    print('Seja muitíssimo bem-vindo(a) ao jogo de adivinhação!!! ')
    print('-'*30)

    meu_numero_secreto = 1024
    total_de_tentativas = 4

    print('-'*30)
    print('Atenção!!! Neste jogo, você tem um total de 4 tentativas... não se esqueça... ')
    print('-'*30)

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        shute = int(input("Adivinhe meu número secreto??? "))
        print('Você digitou o número: ', shute)

        acertou = meu_numero_secreto == shute
        maior = shute > meu_numero_secreto
        menor = shute < meu_numero_secreto

        if (acertou):
            print('Wal!!! Você é de mais!!! Super acertou meu número secreto... Sensacional! ')
            break
        elif (maior):
            print('Puts!!! Você jogou um número maior do que o meu secreto... Você errou. ')
        elif (menor):
            print('Puts!!! maninho, você errou... Você jogou um número menor do que o meu secreto. ')

        print('Fim do jogo... ')