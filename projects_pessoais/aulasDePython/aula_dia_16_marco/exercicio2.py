valores = []
while True:
    valores.append(input("Digite um valor: "))
    resposta = str(input("Quer continuar digitando? [S/N]"))
    if resposta in 'Nn':
        break
print(f"Você digitou {len(valores)} valores!")

valores.sort()
print(f"Os valores digitados na lista crescente, são: {valores}")

valores.sort(reverse=True)
print(f"Os valores da lista em ordem decrescente, são: {valores}")

if '5' not in valores:
    print("O número 5 não faz parte da lista!")
else:
    print("O número 5 faz parte da lista!")
