def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("Erro! Por favor, digite um número inteiro válido. ")
        if ok:
            break
    return  valor


if __name__ == '__main__':
    numero = leiaInt("Digite um valor: ")
    print(numero)



def leiaStringt(msn):
    ok = False
    nome = ""
    while True:
        palavra = str(input(msn))
        if palavra.isprintable():
            nome = str(palavra)
            ok = True
        else:
            print("Erro: Por favor, digite apenas, frases ou palavras.")
        if ok:
            break
    return  nome


if __name__ == '__main__':
    escreva = leiaStringt("Digite seu nome: ")
    print(escreva)
