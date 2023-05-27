#Prova de conhecimentos gerais!!

print("."*40)
print("Olá! Tudo bem contigo? E aí, preparado? Começa agora sua prova final! Vamos lá?")
print("."*40)

respostas_certas = 0

perguntas = {
    'pergunta 1': {
        'pergunta': 'Qual é o nome do doce composto por queijo e goiabada?',
        'respostas': {
            'a': 'Cangica',
            'b': 'Goiabada salgada',
            'c': 'Queijo doce',
            'd': 'Romeu e julieta',
        },
'resposta_certa': 'd',
    },
    'pergunta 2': {
        'pergunta': 'Quantos anos uma pessoa é considerada maior de idade no Brasil?',
        'respostas': {
            'a': '15 anos',
            'b': '16 anos',
            'c': '13 anos',
            'd': '21 anos',
        },
        'resposta_certa': 'd',
    },
    'pergunta 3': {
        'pergunta': 'A linguagem de programação python, é considerada?',
        'respostas': {
            'a': 'Liguagem de programação front-end',
            'b': 'Linguagem de programação em banco de dados',
            'c': 'Linguagem de programação back-end',
            'd': 'Linguagem de programação para modelar um banco de dados',
        },
        'resposta_certa': 'c',
    },
    'pergunta 4': {
        'pergunta': 'O que significa sigla CSS?',
        'respostas': {
            'a': 'Folhas de estilos em cascata',
            'b': 'Linguagem de marcação de programação',
            'c': 'Linguagem de marcação de hipertexto',
            'd': 'Estilos apenas das fontes das páginas web'
        },
        'resposta_certa': 'a',
    },
    'pergunta 5': {
        'pergunta': 'Este questionário, foi desenvolvido, em?',
        'respostas': {
            'a': 'Tuplas',
            'b': 'Listas',
            'c': 'Dicionário',
            'd': 'Apenas em estrutura de repetição',
        },
        'resposta_certa': 'c',
    },

}

print("."*40)
print("Escolha a opção correta: ")
print("."*40)

for pk, pv in perguntas.items():
    print(f"{pk}:{pv['pergunta']}")

    print(f'resposta:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}: {rv}]')

    resposta_usuario = str(input("Por favor, informe qual sua resposta: "))
    if resposta_usuario == pv['resposta_certa']:
        print("Meus parabéns meu lindo!!! Você super acertou!")
        respostas_certas += 1
    else:
        print("Putz meu lindo! Esta, você errou. Precisa estudar mais, tá?")

qtd_perguntas = len(perguntas)
porcentagem_de_acertos = respostas_certas / qtd_perguntas * 100

print(f"Então vamos lá! Você acertou: {respostas_certas} perguntas!")
print(f"Você tem: {porcentagem_de_acertos} de acerto!")