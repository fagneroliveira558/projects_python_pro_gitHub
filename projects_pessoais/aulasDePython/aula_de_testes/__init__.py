nome_aluno = str(input("Informe o nome do aluno: "))
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
nota3 = float(input("Informe a terceira nota do aluno: "))
soma = nota1 + nota2 + nota3

media = soma / 3
if media == 10:
    print(f"O aluno {nome_aluno}!! Foi super aprovado!!! Seu conseito é excelente!!!! Sua média, é{media}")
elif media >= 8:
    print(f"O aluno {nome_aluno}! Foi aprovado com conseito ótimo! Sua média, é: {media}")
elif media >= 6:
    print(f"O aluno {nome_aluno}! Foi aprovado com conseito bom! Sua média, é: {media}")
elif media >= 4:
    print(f"O aluno {nome_aluno}! Ficou em recuperação! Mas, fique tranquilo, você ainda tem oportunidades! Sua média, é: {media}")
else:
    print(f"O aluno {nome_aluno}! Foi infelizmente, reprovado!!!! Sua média, foi: {media}")
