import adivinhacao_com_for
import forca

def escolha_o_jogo():
    print('*'*40)
    print('*** Olá!!! Tudo bem com você? \n\tMuito bom ter você aqui! \n\t\tAbaixo, escolha qual jogo deseja: \n***')
    print('*'*40)

    print('Digite (1) e, jogue o jogo da forca! \nDigite (2) e, jogue o jogo de adivinhação. \n\t\tDivirta-se... ')

    jogo = int(input('Qual jogo deseja: '))

    if (jogo == 1):
        print('Jogando forca... ')
        forca.jogar_jogo_da_forca()
    elif (jogo == 2):
        print('Jogando adivinhação... ')

        adivinhacao_com_for.jogar_jogo_de_adivinhacao()
    else:
        print('Ops... Opção inválida! ')


if (__name__ == '__main__'):
    escolha_o_jogo()