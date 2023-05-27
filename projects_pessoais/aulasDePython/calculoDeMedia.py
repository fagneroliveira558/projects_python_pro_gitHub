# Programa de cálculo de média dos alunos!

nome = str(input("Por favor, informe o nome do aluno: "))
n1 = float(input("Informe a primeira nota do aluno: "))
n2 = float(input("Informe a segunda nota do aluno: "))
n3 = float(input("Informe a terceira nota do aluno: "))
n4 = float(input("Informe a quarta  nota do aluno: "))
resultado = n1 + n2 + n3 + n4
media = resultado / 4

if media == 10:
    print(f"Olá! Tudo bem? O aluno(A) {nome}, tem o conceito: Excelente!!! Você foi super aprovado! Sua nota final, é: {media}! Parabéns!")
elif media >= 8:
    print(f"Olá! Tudo bem? O aluno(A) {nome}, tem o conceito: Ótimo!!! Você foi muito bem aprovado! Sua nota final, é: {media}! Parabéns!")
elif media >= 6:
    print(f"Olá! Tudo bem? O aluno(A) {nome}, tem o conceito: Bom! Você foi aprovado! Sua nota final, é: {media}! Parabéns!")
elif media >= 4:
    print(f"Olá! Tudo bem? O aluno(A) {nome}, tem o conceito: Regular! Você foi direcionado para recuperação! Sua nota final, é: {media}! Não fique triste! Tem chanses ainda!")
else:
    print(f"Olá! Tudo bem? O aluno(A) {nome}, tem o conceito: Ruim! Você foi reprovado! Sua nota final, é: {media}! Infelizmente, não foi desta vez!")