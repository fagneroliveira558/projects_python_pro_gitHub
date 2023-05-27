from aulasDePython.validacao_de_dados import leiaInt
from criando_arquivo_bloco_de_notas import arquivoExiste

from criando_arquivo_bloco_de_notas import criarArquivo

from criando_arquivo_bloco_de_notas import cadastrarUsuario

from criando_arquivo_bloco_de_notas import lerArquivo

arq = 'Miguel.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    nome = str(input("Digite um nome: "))
    while True:
        sexo = str(input("Informe o sexo: [M/F]")).upper()[0]
        if sexo in 'FM':
            break
        print("ERRO: por favor digite M mascolino ou F feminino.")
    idade = leiaInt("Digite a idade: ")
    cadastrarUsuario(arq, nome, sexo, idade)
    while True:
        resposta = str(input("Quer continuar cadastrando dados? [S/N] ")).upper()[0]
        if resposta in 'SN':
            break
        print("ERRO: Digite apenas S ou N")
    if resposta == 'N':
        break

