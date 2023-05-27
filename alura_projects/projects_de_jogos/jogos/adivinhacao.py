import random

print('*' * 40)
print('Olá!!! Tudo bem com você? \n\t\tSejam muito bem-vindos(as) ao nosso jogo de adivinhação dinâmico... \n\t\tVamos lá??? ')
print('*' * 40)

# numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
rodada = 1
pontos = 1000
print('Qual o nível de dificuldade você deseja ter no jogo? ')
print('(1) Fácil (2) Médio (3) Difícil ')

nivel_de_jogada = int(input('Defina qual nível deseja: '))

nivel_facil = nivel_de_jogada == 1
nivel_medio = nivel_de_jogada == 2
nivel_dificil = nivel_de_jogada == 3

if (nivel_facil):
    total_de_tentativas = 20
elif (nivel_medio):
    total_de_tentativas = 10
elif (nivel_dificil):
    total_de_tentativas = 5
else:
    print('Ops... Você não informou uma opção válida... ')

while (rodada_atual <= total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada_atual, total_de_tentativas))
    #numero_secreto = 42
    chute_texto = input('Adivinhe meu número secreto?? \n\t\tDica... Está entre (1 e 100) ')
    print('Seu número digitado, é: ', chute_texto)
    chute = int(chute_texto)

    if (chute < 0 or chute > 100):
        print('Ops... Maninho, não prestou atenção!!!! Meu número secreto, está entre (1 e 100) ')
        continue



    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Wal!!! Você super acertou... Sensacional... \n\t\tSua pontuação, é: {} '.format(pontos))
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos
        if (maior):
            print('Puts... Você errou... Você jogou um número maior do que o meu secreto. ')
            if (rodada == total_de_tentativas):
                print('O número secreto, era: {}. Você fez: {} '.format(
                    numero_secreto, pontos
                ))

        elif (menor):
            print('Puts... Você errou! jogou um número menor do que o meu secreto... ')
            if (rodada == total_de_tentativas):
                print('O número secreto, era: {}. Você fez {} '.format(
                    numero_secreto, pontos
                ))



    rodada_atual += 1

print('Fim do jogo...')