#for c in range(1,10):
#    print(c)

#c = 1
#while c < 10:
#    print(c)
#    c += 1

#n = 1
#while n != 0:
    #n = int(input("digite um número: "))


#r = "S"
#while r == "S":
#    nome = str(input("Informe o nome: "))
#    r = str(input("Deseja continuar? [S/N").upper())


n = 1
par = impar = 0
while n != 0:
    n = int(input("Informe um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f"Você digitou {par}  números pares, e digitou {impar} números impares."
      f"")