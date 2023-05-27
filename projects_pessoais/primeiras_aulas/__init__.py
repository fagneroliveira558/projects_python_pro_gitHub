print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 256
shute = int(input("Adivinhe meu número secreto: Duvído? "))
acertou = shute == numero_secreto
maior = shute > numero_secreto
menor = shute < numero_secreto

if (acertou):
    print('Wal!!! Você super acertou.... Mandou muito bem!! ')
elif (maior):
    print('Puts maninho!!!! Você jogou um número maior do que o esperado... ')
elif (menor):
    print('Puts maninho!!! Você jogou um número menor do que o esperado... ')
