print('''
    seja bem-vindo(a) a uma cauculadora básica em Python. Digite os valores desejados e em seguida escolha a opção intencionada.
''')

def inputs():
    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print('''
            escolha entre as opções:
            1) Soma.
            2) subtração.
            3) multiplicação.
            4) divisão.
                        ''')
            opc = int(input(" "))
            if opc == 1:
                print(soma(n1, n2))
                break
        except ValueError:
            print("Digite apenas números! ")

def soma(n1, n2):
    r = n1+n2
    return resultado(round(r, 2))


def resultado(r):
    return f"O resultado é: {r}"

while True:
    inputs()
    check = input(" Deseja realizar outra operação? Digite S para sim ou qualquer outra letra para fechar esta aplicação: ")
    if check.upper() == "S":
        continue
    else:
        print("Obrigado... ")
        break



def subtrair(n)