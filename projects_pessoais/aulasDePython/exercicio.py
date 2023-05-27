# Exercício da última aula.

nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
endereco = str(input("Informe aqui, seu endereço completo: "))
if 0 <= idade <= 21:
    print(f"Olá {nome}!\n Tudo bem com você? Você tem: {idade} Anos!\n Que legal!\n Muito bom! Você mora, na: {endereco}\n Então, você ainda não é maior de idade! ")
elif 21 < idade <= 65:
    print(f"Olá {nome}!\n Tudo bem com você? Você tem: {idade} Anos!\n Que legal!\n Muito bom! Você mora, na: {endereco}\n Sensacional! Você é maior de idade! ")
elif 65 < idade <= 105:
    print(f"Olá {nome}!\n Tudo bem com você? Você tem: {idade} Anos!\n Que legal!\n Muito bom! Você mora, na: {endereco}\n Sensacional!!! Você está na melhor idade!")
else:
    print(f"Olá {nome}!\n Tudo bem com você? Você tem: {idade} Anos!\n Que legal!\n Muito bom! Você mora, na: {endereco}\n Lamento! Você digitou uma idade inválida!!!")
