idades = [30, 27, 18, 21, 26, 20, 44, 51]
idades.insert(0, 22)
idades.append(45)
idades.append(24)
idades.append(23)
idades.append(34)
idades.extend([25, 33, 36, 43, 53, 61, 71, 32, 12, 10, 13, 14, 16])
for listar_idades in idades:
    if 27 in idades:
        idades.remove(27)
        print('Idade 27 removido com sucesso... ')
    print(listar_idades)

#print(len(idades))

#idades_no_ano_que_vem = [(idade + 1 ) for idade in idades]
#print(idades_no_ano_que_vem)

#idades_no_ano_que_vem = []
#for idade in idades:
    #idades_no_ano_que_vem.append(idade + 1)
    #print(idades_no_ano_que_vem)


    atualizar_idades = [(idade) for idade in idades if idade >= 23]
    print(atualizar_idades)
