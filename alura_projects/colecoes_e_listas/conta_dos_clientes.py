from abc import ABCMeta, abstractmethod




class Conta_dos_clientes(metaclass=ABCMeta):
    def __init__(self, codigo, titular_da_conta, cpfDoTitularDaConta):
        self._codigo = codigo
        self._saldo = 0
        self._titular_da_conta = titular_da_conta
        self._cpfDoTitularDaConta = cpfDoTitularDaConta

    def sacar(self, valor):
        self._saldo -= valor

    def depositar_valor(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return '[>>Código da conta: {} Saldo {} reais... \n\tTitular da conta: {} \n\t\tCPF do titular da conta: {} <<'.format(self._codigo, self._saldo, self._titular_da_conta, self._cpfDoTitularDaConta)


class ContaCorrente(Conta_dos_clientes):
    def passa_o_mes(self):
        self._saldo -= 2
    def sacar(self, valor):
        self._saldo -= valor + 7



class ContaPoupanca(Conta_dos_clientes):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaDeInvestimentos(Conta_dos_clientes):
    pass



conta13 = ContaCorrente(13, 'Zoe Miwa Amorim', '222.222.222-22')
conta13.depositar_valor(1000)
conta13.passa_o_mes()


conta14 = ContaPoupanca(14, 'Alícia Amorim', '333.333.333-33')
conta14.depositar_valor(1500)
conta14.passa_o_mes()
conta15 = ContaCorrente(16, 'Fagner Araujo', '111.111.111-11')
conta15.depositar_valor(1500)
conta15.passa_o_mes()

conta16 = ContaPoupanca(15, 'RuteNeia Santos', '444.444.444-44')
conta16.depositar_valor(1500)
conta16.passa_o_mes()

conta18 = ContaPoupanca(17, 'Miguel Lorenzo', '555.555.555-55')
conta18.depositar_valor(1000)
conta18.passa_o_mes()


conta17 = ContaCorrente(18, 'Kamila Amorim', '666.666.666-66')
conta17.depositar_valor(1500)
conta17.passa_o_mes()


todas_as_contas = [conta13, conta14, conta15, conta16, conta17, conta18]




for contas in todas_as_contas:
    print(contas)

