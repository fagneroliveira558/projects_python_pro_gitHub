arq = "my_file_do_dia.txt"

def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except(FileNotFoundError):
        return  False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Ouve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso!")
        print(a.read())
    finally:
        a.close()


if not arquivoExiste(arq):
    criarArquivo(arq)