from random import choice

def jogar_jogo_da_forca():
    frutas = ['banana', 'jabuticaba', 'laranja', 'uva', 'manga', 'melancia', 'tomate', 'abacate', 'goiaba', 'siriguela', 'carambola', 'mexerica', 'graviola']

    palavra_secreta = choice(frutas)
    print('-'*30)
    print('Olá! Você escolheu o jogo da forca!! ')
    print('E aí! Preparado??? \n\tVamos lá... ')
    print('-'*30)

    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    chances = 6
    tentativas = []
    while True:
        print(tentativas)
        #chances -= 1
        print('Chances: ', chances)

        for letra in palavra_secreta:
            if letra in tentativas:
                print(letra, end=' ')
            else:
                print('_', end = ' ')


        palpite = input('\nÉ agora! Escolha uma letra, ou "SAIR" para sair do programa...  ').lower()
        if palpite == 'sair':
            break
        elif palpite not in alfabeto or palpite == '':
            print('Puts maninho... Você não informou uma letra!!! Assim, não da em? ')
            continue
        elif palpite in tentativas:
            print("Você é desmemoriado ou o quê!? Você já tentou essa letra. Tente outra!")
            continue
        tentativas.append(palpite)
        if palpite in palavra_secreta:
            print("Wal!!! ACERTÔ, MIZERAVI!")
        else:
            chances -= 1
            print("Puts!!! Maninho, errou feio, errou rude!")
            print(chances)
        if chances == 0:
            print('Puts!!! Perdeu pivete... Foi enforcado... \n\tQue peninha.... \n\t\tQuem sabe na próxima, né???? ')
            break
        elif set(palavra_secreta).issubset(set(tentativas)):
            print('Wal... Você super acertou meu caro!!!! \n\tShow de bola! \n\t\tMandou muito bem... \n\t\t\tContinue assim... \n\t\t\t\tA palavra secreta, éra: ', palavra_secreta)
            break

if __name__ == '__main__':
    jogar_jogo_da_forca()
