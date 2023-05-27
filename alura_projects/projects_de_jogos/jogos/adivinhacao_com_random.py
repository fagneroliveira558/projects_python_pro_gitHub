import random

print('*' * 40)
print(
    'Olá!!! Tudo bem com você? \n\t\tSejam muito bem-vindos(as) ao nosso jogo de adivinhação dinâmico... \n\t\tVamos lá??? ')
print('*' * 40)

# numero_secreto = round(random.random() * 100)
numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

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

