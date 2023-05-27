from exercicio1 import leiaInt

num = []
pares = []
impares = []

while True:
    num.append(leiaInt("Digite um número: "))
    resposta = str(input("Quer continuar digitando? [S/N]"))
    if resposta in 'Nn':
        break

for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

        print("."*40)
        print(f"Os valores digitados armazenados na lista geral, são: {num}")
        print(f"Os valores digitados armazenados na lista dos pares, são: {pares}")
        print(f"Os valores digitados armazenados na lista dos ímpares, são: {impares}")
        print("." * 40)
