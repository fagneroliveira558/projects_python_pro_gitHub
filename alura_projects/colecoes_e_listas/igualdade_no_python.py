class ContaCorrente:
    def __init__(self, codigoDaConta, nomeDoTitular, cpfDoTitular):
        self._codigoDaConta = codigoDaConta
        self._nomeDoTitular = nomeDoTitular
        self._cpfDoTitular = cpfDoTitular
        self._saldo = 0

    def __str__(self):
        return f'[>>> Código da conta corrente: {self._codigoDaConta} O saldo da conta, é: {self._saldo} reais... \n\tO titular da conta, é: {self._nomeDoTitular}! \n\t\tO CPF do titular, é: {self._cpfDoTitular}... <<<]'

    def depositar(self, valorDoDeposito):
        self._saldo += valorDoDeposito

    #def __eq__(self, outro):
        #if (type(outro) != ContaSalario):
            #return False



class ContaSalario:
    def __init__(self, codigoDaConta, nomeDoTitular, cpfDoTitular):
        self._codigoDaConta = codigoDaConta
        self._nomeDoTitular = nomeDoTitular
        self._cpfDoTitular = cpfDoTitular
        self._saldo = 0

    def depositar(self, valor_de_deposito):
        self._saldo += valor_de_deposito

    def sacar(self, valor_de_saque):
        self._saldo -= valor_de_saque + 6.50

    def __str__(self):
        return '[>>> Código da conta: {}... O saldo da conta, é: {} reais... \n\tO titular da conta, é: {}! \n\t\tO CPF do titular, é: {}... <<<]'.format(self._codigoDaConta, self._saldo, self._nomeDoTitular, self._cpfDoTitular)

    def __eq__(self, outro):
        if (type(outro) != ContaSalario):
            return False
        return self._codigoDaConta == outro._codigoDaConta and self._saldo == outro._saldo


class ContaMultiploSalario(ContaSalario):
    pass



conta1 = ContaSalario(3196, 'Fagner Oliveira Araujo', '222.222.222-22')
conta1.depositar(250)


conta2 = ContaSalario(3196, 'RuteNeia Amorim Oliveira', '333.333.333-33')
conta2.depositar(350)

contaCorrente1 = ContaCorrente(3196, 'Miguel Oliveira Araujo', '111.111.111-11')
contaCorrente1.depositar(250)


print(contaCorrente1 == conta1)

