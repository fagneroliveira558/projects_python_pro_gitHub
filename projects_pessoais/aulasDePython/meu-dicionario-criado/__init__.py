#Meu dicionário que estou desenvolvendo!

print("."*40)
print("Olá! Seja muito bem-vindo a prova final!")
print("."*40)

respostas_certas = 0
perguntas = {
    'pergunta 1': {
        'pergunta': 'Qual é a linguagem de programação mais utilizada hoje?',
        'respostas': {
            'a': 'cobol',
            'b': 'python',
            'c': 'c++',
            'd': 'java',
        },
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Qual é a melhor idade no Brasil?',
        'respostas': {
            'a': '30 anos',
            'b': '18 anos',
            'c': '45 anos',
            'd': '70 anos',
        },
        'resposta_certa': 'd',
    },
    'pergunta 3': {
        'pergunta': 'Qual é o país mais lindo, belo, maravilhoso e tope de se viver? Claro, perdendo infelizmente para, corrupção e robalheira?',
        'respostas': {
            'a': 'Argentina',
            'b': 'Bolívia',
            'c': 'Venesuela',
            'd': 'Brasil',
        },
        'resposta_certa': 'd',
    }
}

print("."*40)
print("Por favor, escolha a opção correta: ")
print("."*40)

for pk, pv in perguntas.items():
    print(f"{pk}:{pv['pergunta']}")

    print(f'resposta:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}: {rv}]')
    resposta_usuario = (input("Por favor, digite aqui, sua resposta: "))

    if resposta_usuario == pv['resposta_certa']:
        print("Meus parabéns meu lindo! Você super acertou esta questão!!!")
        respostas_certas += 1
    else:
        print("Putz! Você errou! Não foi desta vez! Precisa estudar um pouco mais!!!")

qtde_perguntas = len(perguntas)
porcentagem_de_acertos = respostas_certas / qtde_perguntas * 100


print(f"Você acertou: {respostas_certas}")
print(f"Você tem {porcentagem_de_acertos} de acertos!")