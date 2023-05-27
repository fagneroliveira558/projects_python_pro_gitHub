#Muito bem-vindo ao meu programa de cadastro de pessoas com seus respectivos pesos!

temp = []
pessoas = []

maior = menor = 0

while True:
    temp.append(str(input("Digite um nome válido: ")))
    temp.append(float(input("Digite o peso: ")))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    pessoas.append(temp[:])
    #Este código acima, é uma lista composta! Uma lista dentro de outra lista!
    temp.clear()
    resposta = str(input("Deseja continuar digitando? [S/N]"))
    if resposta in 'Nn':
        break
print(f"Você cadastrou: {pessoas}")

print(f"Temos: {len(pessoas)} pessoas cadastradas.")

print(f"A pessoa de maior peso, foi registrado num total, de: {maior}. A pessoa que foi registrada com menor peso, foi num total, de: {menor}")

