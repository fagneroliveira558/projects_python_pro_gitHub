from datetime import date

atual = date.today().year
maiorIdade = menorIdade = 0
for pessoa in range(1,6 ):
    nasc = int(input(f"Em que ano a pessoa {pessoa} nasceu? "))
    idade = atual - nasc
    if idade >= 21:
        maiorIdade += 1
    else:
        menorIdade += 1
print(f"autodo temos: {maiorIdade} pessoas maiores de idade! ")
print(f"Autodo temos: {menorIdade} pessoas menores de idade! ")

