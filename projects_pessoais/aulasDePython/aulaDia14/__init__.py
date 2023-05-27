r = 'S'
sexo = str(input("Informe seu sexo: [M/F]")).strip().upper() [0]
while sexo not in 'Mm/Ff':
    sexo = str(input("Você digitou dados errados, favor digitar novamente: [M/F]"))
    print(f"{sexo} Registrado com sucesso! ")
r = str(input("Deseja continuar cadastrando? [S/N]").upper())
print(f"{sexo} Registrado com sucesso! ")
while r == 'S':
    sexo = str(input("Informe seu sexo: [M/F]")).strip().upper()[0]
    r = str(input("Deseja continuar cadastrando? [S/N]").upper())
    print(f"{sexo} Registrado com sucesso! ")
