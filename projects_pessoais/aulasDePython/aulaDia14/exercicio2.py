from time import sleep

n = int(input("Digite um número: "))
for cont in range(n, -1, -1):
    print(cont)
    sleep(1.3)
print("Bum! Bum! Bum Bum!\n Fim!")

for cont in range(0,n):
    print(cont)
    sleep(1.3)
print("Fim do regreço!")
