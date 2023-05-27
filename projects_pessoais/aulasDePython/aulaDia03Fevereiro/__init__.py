nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
if 0 <= idade <= 21:
    print(f"Olá! {nome}, Você tem: {idade} anos, Você é menor de idade!")
elif 21 < idade <= 65:
    print(f"Olá! {nome}, Você tem: {idade} anos, Você é maior de idade!")
elif 65 < idade <= 100:
    print(f"Olá! {nome}, Você tem: {idade} anos, Você está na melhor idade!")
else:
    print(f"Olá! {nome}, Lamento! Você digitou uma idade inválida!!!")
