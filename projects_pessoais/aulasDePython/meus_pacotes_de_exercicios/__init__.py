from executar_funcoes import somar, subtrair, multiplicar, dividir

opcao = str(input('Escolha qual operação matemática deseja: Ou, digite sair caso queira... '))

if opcao == 'adição':
    print(somar())

elif opcao == 'subtração':
    print(subtrair())


elif opcao == 'multiplicação':
    print(multiplicar())


elif opcao == 'divisão':
    print(dividir())



else:
    print('Você escolheu sair... ')
