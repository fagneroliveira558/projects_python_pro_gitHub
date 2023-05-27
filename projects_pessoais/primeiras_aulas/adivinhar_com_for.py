print('-'*30)
print('Seja muito bem-vindo(a) ao jogo de adivinhação!!! ')
print('-'*30)

i = int(input('Digite o número de partida: '))
j = int(input('Digite o número de parada: '))
k = int(input('Digite o intervalo de números: Exemplo: De um em um... de De 2 em 2... Exemplo de 3 em 3 etc... '))
for rodada in range(i, j, k):
    print(rodada)
