print("." * 40)
print("{:^30}".format("Seja muito bem-vindo ao banco 24 horas!"))
print("." * 40)
valor = int(input("Qual valor deseja sacar: $"))
total = valor
cedula = 200
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f"Total de {totalCedula} Cédulas R$ {cedula}")
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        totalCedula = 0
        if total == 0:
            break
print("." * 40)
print("Muitíssimo obrigado por utilizar nossos serviços!")
print("." * 40)
print("Volte sempre!!!")
print("." * 40)