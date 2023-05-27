
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("ERRO: Por favor, digite números inteiros válidos!")
            continue
        except(KeyError):
            print("O usuário preferio não digitar o valor esperado.")
            return 0
        else:
            return n

