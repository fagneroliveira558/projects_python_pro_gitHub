import random

def imprime_mensagem_boas_vindas():
    print('*' * 40)
    print('*** Olá!!! Tudo bem? \n\tSeja muito bem-vindo(a) ao jogo da forca... \n\t\tE aí! Preparado? \n***')
    print('*' * 40)


def jogar_jogo_da_forca():
    imprime_mensagem_boas_vindas()
    palavra_secreta = carrega_palavra_secreta()
    palavra_secreta = carrega_palavra_secreta('lista_de_frutas.txt')
    #print(numero)
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    numeros_de_erros = 0
    total_de_tentativas = 6
    print(letras_acertadas)
    while (not acertou and not  enforcou):
        chute = pede_chute()
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            numeros_de_erros += 1
            #print('Você já tem {} erros... '.format(numeros_de_erros))
            desenhando_o_bonequinho(numeros_de_erros)

        enforcou = numeros_de_erros == 7
        acertou = '_' not  in letras_acertadas

        print(letras_acertadas)
    if (acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)
        #desenhando_o_bonequinho(numeros_de_erros)
    print('Fim do jogo... ')

def carrega_palavra_secreta(nome_do_arquivo='lista_de_nomes.txt', primeira_linha_valida=0):
    criar_arquivo = open(nome_do_arquivo, 'r')
    lista_de_frutas = []

    for linha in criar_arquivo:
        linha = linha.strip()
        lista_de_frutas.append(linha)
    criar_arquivo.close()
    numero = random.randrange(primeira_linha_valida, len(lista_de_frutas))
    palavra_secreta = lista_de_frutas[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input('E aí!!! Qual letra você escolhe maninho... ')
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        acertou_a_letra = chute == letra
        if (acertou_a_letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor(palavra_secreta):
    print('Wal!!! Você super acertou meu brother... \n\t\tSensacional de mais!!! \n\t\tA palavra secreta é: ',
          palavra_secreta)

def imprime_mensagem_perdedor(palavra_secreta):
    print('Puts... Maninho, você perdeu! Não foi desta vez... \n\t\tFalou... \n\t\t\tA palavra secreta, era: ',
          palavra_secreta)

def desenhando_o_bonequinho(numeros_de_erros):
    if (numeros_de_erros == 1):
        print('Puts queridinho... Desenhei a cabecinha!!! ')
    elif (numeros_de_erros == 2):
        print('Puts queridinho... Desenhei o bracinho direito!!! ')
    elif (numeros_de_erros == 3):
        print('Puts queridinho... Desenhei o bracinho esquerdo!!! ')
    elif (numeros_de_erros == 4):
        print('Puts queridinho... Desenhei o corpinho!!! ')
    elif (numeros_de_erros == 5):
        print('Puts queridinho... Desenhei a perninha direita!!! ')
    elif (numeros_de_erros == 6):
        print('Puts queridinho... Desenhei a perninha esquerda!!!')
    else:
        print('Puts amigãoooooooooooooooooo! Perdeu feioooooo... \n\t\tFoi enforcado!!! ')


if (__name__ == '__main__'):
    jogar_jogo_da_forca()