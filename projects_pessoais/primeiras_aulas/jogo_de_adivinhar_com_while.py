print('-'*30)
print('Seja muito bem-vindo(a) ao jogo de adivinhação!!! ')
print('-'*30)


meu_numero_secreto = 512
rodada = 1
total_de_tentativas = 4

while (rodada <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    shute = int(input('Adivinhe meu número secreto: Duvído! '))
    print('Você digitou o número: ', shute)

    acertou = shute == meu_numero_secreto
    maior = shute > meu_numero_secreto
    menor = shute < meu_numero_secreto

    if (acertou):
        print('Wal!!! Você é de mais!!! Super acertou meu número secreto... Sensacional! ')
        break
    elif (maior):
        print('Puts!!! Você jogou um número maior do que o meu secreto... Você errou. ')
    elif (menor):
        print('Puts!!! maninho, você errou... Você jogou um número menor do que o meu secreto. ')
    rodada += 1

    #total_de_tentativas -= 1
print('Fim do jogo... ')
