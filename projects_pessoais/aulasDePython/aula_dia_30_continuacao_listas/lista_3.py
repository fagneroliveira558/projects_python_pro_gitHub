from  tratamento_de_ececao import leiaInt

num = []
pares = []
impares = []

while True:
    num.append(leiaInt("Digite um número: "))
    resposta = str(input("Quer continuar? [S/N]"))
    if resposta in 'Nn':
        break


for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

        print("-"*30)
print(f"A lista completa, é: {num}")
print(f"Os números pares, são: {pares}")
print(f"Os números impares, são: {impares}")
        print("-" * 30)