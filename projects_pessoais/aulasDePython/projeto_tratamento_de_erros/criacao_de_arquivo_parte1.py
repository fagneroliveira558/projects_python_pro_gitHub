arq = open("fagner1.txt", 'w+')
arq.write('linha 1 \n ')
arq.write('linha 2 \n ')
arq.write('linha 3 \n ')

arq.seek(0, 0)
print(arq.read())

arq.seek(0, 0)
print(arq.readline())

arq.seek(0, 0)
print(arq.readlines())

arq.seek(0, 0)

print("Lendo linha a linha com for!")
for linhas in arq.readlines():
    print(linhas, end='')
