from exercicio1 import leiaInt

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except(FileNotFoundError):
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso.")
        a.close()


def cadastrarUsuario(arq, nome, sexo, idade):
    try:
        a = open(arq, 'at')
    except:
        print("Erro, houve um erro ao abrir o arquivo.")
    else:
        try:
            a.write(f"seu nome: {nome}; seu sexo: {sexo}; e sua idade: {idade} anos\n")
        except:
            print("Houve um erro ao escrever os dados.")
        else:
            print(f"Novo registro de {nome}, adicionado com sucesso.")
            a.close()


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo.")
    else:
        cadastrarUsuario("Pessoas cadastradas.")
    finally:
        a.close()


arq = 'arquivo_2_de_fagner.txt'
