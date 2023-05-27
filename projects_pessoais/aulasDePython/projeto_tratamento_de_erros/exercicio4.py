from exercicio1 import leiaInt

geral = []
maior_idade = []
menor_idade = []

while True:
    geral.clear()
    geral[' nome '] = str(input("Digite o nome: "))
    geral[' idade '] = leiaInt("Digite a idade: ")
    resposta = str(input("Quer continuar inserindo dados? [S/N]"))
    if resposta in 'Nn':
        break

for i, v in enumerate(geral):
    if geral >= 21:
        maior_idade.append()
    else:
        menor_idade.append()

print("."*40)
print(f"As pessoas cadastradas na lista geral, são: {geral}")
print(f"As pessoas cadastradas na lista maiores de idade, são: {maior_idade}")
print(f"As pessoas cadastradas na lista menor de idade, são: {menor_idade}")
print("."*40)
