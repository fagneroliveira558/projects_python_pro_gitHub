total20 = 0
total21 = 0
totalHomens20 = 0
totalHomens21 = 0
totalMulheres20 = 0
totalMulheres21 = 0

while True:
    idade = int(input("Digite sua idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Informe seu sexo: 'MF'")).strip().upper()[0]
        if idade <= 21:
            total20 += 1
        elif idade >= 21:
            total21 += 1

        if sexo == 'M' and idade <= 20:
            totalHomens20 += 1
        elif sexo == 'M' and idade >= 21:
            totalHomens21 += 1

        if sexo == 'F' and idade <= 20:
            totalMulheres20 += 1
        elif sexo == 'F' and idade >= 21:
            totalMulheres21 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input("Deseja continuar: 'SN'")).strip().upper()[0]

        if resposta == 'N':
            print("Obrigado por usar nosso sistema")
    break
print("fim")


