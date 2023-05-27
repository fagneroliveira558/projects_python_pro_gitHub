print('''
seja bem-vindo(a) a uma cauculadora básica em Python. Digite os valores desejados e em seguida escolha a opção intencionada.
''')

def inputs():
    while True:
        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            print('''
            escolha entre as opções:
            1) Soma.
            2) Subtração.
            3) Multiplicação.
            4) Divisão.
            ''')
            opcao = int(input(' '))
            if opcao == 1:
                print(soma(num1, num2))
            break
        except ValueError:
            print('Digite apenas números! ')



def soma(num1, num2):
    r = num1 + num2
    return resultado(round(r, 2))


def resultado(r):
    return f'O resultado, é: {r}'


while True:
    inputs()
    check = input(' Deseja realizar outra operação? Digite S para sim ou qualquer outra letra para fechar esta aplicação: ')
    if check.upper() == 'S':
        continue
    else:
        print('Muitíssomo obrigado! ')
        break
