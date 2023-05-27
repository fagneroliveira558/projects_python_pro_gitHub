nome = ("Fagner", "Marcos", "Antonio", "Heider", "Vagner", "Victor", "Fernanda", "Franklin", "Edinalva", "Angelica", "Mirian", "Renata")

#print(nome)

#print(nome[1])

#print(nome[-1])

#print(nome[:4])

#print(len(nome))

#nome[3] = "Roberto'"
#print(nome)

for pessoa, i in enumerate(nome):
    print(f"{pessoa + 1})", i)