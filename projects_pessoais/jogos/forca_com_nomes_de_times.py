from random import choice


def jogar_forca_com_nomes_times():
    mensagem_de_boas_vindas()
    nomes_de_times = ['palmeiras', 'santos', 'tricolor', 'corinthians', 'flamengo', 'vasco', 'bangu', 'fluminense',
                      'portuguesa', 'guarani', 'barueri', '', 'barcelona', 'realmadri', 'gremio', 'cru', 'cruzeiro',
                      'curitiba', 'bahia', 'goias']
    palavra_secreta = choice(nomes_de_times)
    letras_do_alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    chances = 6
    tentativas = []
    while True:
        print(tentativas)
        print('Chances: ', chances)
        for letra in palavra_secreta:
            if letra in tentativas:
                print(letra, end= ' ')
            else:
                print('_', end= ' ')
        palpite = input('\n\tÉ agora maninho... Qual letra você escolhe? ou, caso queira desistir, descreva "SAIR" para finalizar... ').lower()
        if palpite == 'sair':
            print('Desistiu né??? Que pena maninho... Da próxima, não seja covarde... \n\t\tTchal!!! ')
            break
        elif palpite not in letras_do_alfabeto or palpite == '':
            print('Puts maninho... Você não informou uma letra!!! Assim, não da em? Foi digitado o caractere ', palpite)
            continue
        elif palpite in tentativas:
            print("Você é desmemoriado ou o quê!? Você já tentou essa letra. Tente outra!")
            continue
        tentativas.append(palpite)
        if palpite in palavra_secreta:
            print("Wal!!! ACERTÔ, MIZERAVI! Gênio... ")
        else:
            chances -= 1
            print("Puts!!! Maninho, errou feio, errou rude!")
            print(chances)
        if chances == 0:
            print('Puts!!! Perdeu pivete... Foi enforcado... \n\tQue peninha.... \n\t\tQuem sabe na próxima, né???? ')
            print('GAME OVER... KKKKKKKKKKKKKKKKK ')
            break
        elif set(palavra_secreta).issubset(set(tentativas)):
            print(
                'Wal... Você super acertou meu caro!!!! \n\tShow de bola! \n\t\tMandou muito bem... \n\t\t\tContinue assim... \n\t\t\t\tA palavra secreta, éra: ',
                palavra_secreta)
            print('GAME OVER... Com vitória!!!! Sensacional...')
            break

def mensagem_de_boas_vindas():
    print('*' * 40)
    print(
        'Wal!!! Você escolheu jogar o jogo da forca com nomes de times? \n\tCorajoso você, em?? \n\t\tE aí! Está preparado? Vamos lá? \n\t\t\tBoa sorte maninho... ')
    print('*' * 40)

if (__name__ == '__main__'):
    jogar_forca_com_nomes_times()