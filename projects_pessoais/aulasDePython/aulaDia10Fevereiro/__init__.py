from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print(''' Sua opção: 
[0] = pedra
[1] = papel
[2] = tesoura''')

jogador = int(input("Qual a sua jogada? "))
print("-"*30)
print(f"O computador jogou: {itens[computador]} ")
print(f"O jogador jogou: {itens[jogador]} ")
print("-"*30)

if computador == 0:
    if jogador == 0:
        print("Esta jogada deu impate!")
    elif jogador == 1:
        print("Você venceu!")
    elif jogador == 2:
        print("O computador venceu!")
    else:
        print("Jogada inválida!")

elif computador == 1:
    if jogador == 0:
        print("Computador venceu!")

    elif jogador == 1:
        print("A jogada deu impate!")
    elif jogador == 2:
        print("O jogador venceu!")
    else:
        print("Jogada inválida!")

elif computador == 2:
    if jogador == 0:
        print("O jogador venceu!")
    elif jogador == 1:
        print("O computador venceu!")
    elif jogador == 2:
        print("A jogada deu impate!")
    else:
        print("Jogada inválida!")
