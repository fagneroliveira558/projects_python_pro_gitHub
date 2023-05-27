from exercicio1 import leiaInt

pessoa = {}
cadastrados = []
soma = media = 0

while True:
    pessoa.clear()
    pessoa[' nome '] = str(input("Digite um nome: "))
    while True:
        pessoa[' sexo '] = str(input("Digite o sexo: [M/F]")).upper()[0]
        if pessoa[' sexo '] in 'MF':
            break
        print("Erro: Por favor, digite M para masculino, ou, F para feminino.")
    pessoa[' idade '] = leiaInt("Digite a idade: ")
    soma += pessoa[' idade ']
    cadastrados.append(pessoa.copy())
    while True:
        resposta = str(input("Quer continuar inserindo dados? [S/N]")).upper()[0]
        if resposta in 'SN':
            break
        print("Erro: Digite S para sim, ou, N para não.")
    if resposta == 'N':
        break

print('-'*30)
print(f"Altodo, temos, {len(cadastrados)} pessoas cadastradas.")
print('-'*30)
media = soma / len(cadastrados)
print(f"A media de pessoas, cadastradas, tem: {media:5.2f} anos.")
print('-'*30)
print("As mulheres cadastradas, foram: ", end='')
for mulheres in cadastrados:
    if mulheres[' sexo '] in 'Ff':
        print(f"{mulheres[' nome ']}", end='')

    else:
        print("Até o momento, não foi encontrado nenhuma mulher cadastrada!")
print('-'*30)
print("As pessoas que estão a cima da média, são ", end='')
for p in cadastrados:
    if p[' idade '] >= media:
        print('               ')
        for k, v in p.items():
            print(f"{k} = {v} ; ", end='')
        print()
        print("<< Enserrado >>")
