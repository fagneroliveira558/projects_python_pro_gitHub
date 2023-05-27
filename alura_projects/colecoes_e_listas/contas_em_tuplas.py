class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return '[>>>O código da conta, é: {} E o saldo, é: {} reais... <<<]'.format(self.codigo, self.saldo)

#conta_do_fagner = ContaCorrente(3196)
#conta_da_neia = ContaCorrente(47685)
#conta_do_arnaldo = ContaCorrente(1278)
#conta_da_nalva = ContaCorrente(2307)

fagner = ('fagner oliveira araujo', 1992, 31)
neia = ('ruteneia santos amorim', 1992, 31)
arnaldo = ('arnaldo ribeiro araujo', 1970, 52)
nalva = ('edinalva oliveira araujo', 1973, 49)

conta_do_fagner = (3196, 3500)
conta_do_arnaldo = (1278, 4800)
conta_da_nalva = (1667, 5800)
conta_da_neia = (1661, 14850)

def depositar_salario(conta):
    novo_saldo = conta[1] + 200
    codigo = conta[0]
    return (codigo, novo_saldo)

conta_do_fagner = depositar_salario(conta_do_fagner)
print(conta_do_fagner)
