#Dicionário em python!

print("."*30)
print("Bem vindo a nossa prova de conhecimento gerais!")
print("."*30)

respostas_certas = 0

perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2 + 2',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '8',
            'd': '7',
        },
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 2 vezes 2',
        'respostas': {
            'a': '5',
            'b': '7',
            'c': '9',
            'd': '4',
        },
        'resposta_certa': 'd',
    },
    'pergunta 3': {
        'pergunta': 'Qual a linguagem de programação mais utilizada no momento?',
        'respostas': {
            'a': 'Java',
            'b': 'CSharp',
            'c': 'Python',
            'd': 'C++',
        },
        'resposta_certa': 'c',
    },
    'pergunta 4': {
        'pergunta': 'Qual assunto estudado neste exercício?',
        'respostas': {
            'a': 'Lista',
            'b': 'Tupla',
            'c': 'Funções',
            'd': 'Dicionário',
        },
        'resposta_certa': 'd',
    },
}

print("-"*30)
print("Escolha a opção correta")
print("-"*30)

for pk, pv in perguntas.items():
    print(f"{pk}:{pv['pergunta']}")

    print(f'resposta:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}: {rv}]')

    resposta_usuario = input("Qual sua resposta? ")

    if resposta_usuario == pv['resposta_certa']:
        print("Parabéns, você acertou a questão!")
        respostas_certas += 1
    else:
        print("Você errou, precisa estudar mais!")

qtde_perguntas = len(perguntas)
porcentagem_de_acertos = respostas_certas / qtde_perguntas * 100

print(f"Você acertou {respostas_certas} perguntas")
print(f"Você tem {porcentagem_de_acertos} de acertos")

