lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]

maiorValor = lista[0]
menorValor = lista[0]
listaPares = []

#for index in range(0, len(lista)):

for index in range(0, len(lista)):
    if (lista[index] % 2 == 0):
        listaPares.append(lista[index])
    #if (maiorValor < lista [index]):
    #if (menorValor > lista[index]):
        #menorValor = lista[index]

#print(menorValor)

print(listaPares)
