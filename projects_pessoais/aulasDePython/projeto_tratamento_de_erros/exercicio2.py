
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("ERRO: Por favor, digite números válidos!")
            continue
        except(KeyError):
            print("O usuário preferio não digitar o valor esperado.")
            return 0
        else:
            return n

numero = leiaFloat("Digite um número: ")
print(numero)
