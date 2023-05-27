class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return '[>>>O código da conta, é: {} E o saldo, é: {} reais... <<<]'.format(self.codigo, self.saldo)


conta_do_fagner = ContaCorrente(3196)
conta_da_neia = ContaCorrente(47685)
conta_do_arnaldo = ContaCorrente(1278)
conta_da_nalva = ContaCorrente(2307)

conta_da_neia.depositar(1000)
conta_do_fagner.depositar(500)
conta_da_nalva.depositar(1200)
conta_do_arnaldo.depositar(2300)
conta_do_fagner.depositar(1000)



def depositar_para_todas(contas):
    for conta in contas:
        conta.depositar(200)
        #print(conta)
contas = [conta_do_fagner, conta_da_neia, conta_do_arnaldo, conta_da_nalva]
print(contas[0], contas[1], contas[2], contas[3])
depositar_para_todas(contas)
print(contas[0], contas[1], contas[2], contas[3])


#for conta in contas:

    #print(conta)
