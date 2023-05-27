class Conta:
    def __init__(self, numero_da_conta, titular, saldo, limite_de_credito = 1500.0):
        print('Criando um objeto... {} '.format(self))
        self.__numero_da_conta = numero_da_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite_de_credito = limite_de_credito

    def extrato(self):
        print('Saldo {} reais do titular {}! \n\tLimite de crédito disponível, é de: {} reais... '.format(self.__saldo, self.__titular, self.__limite_de_credito))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_de_saque):
        valor_disponivel_de_saque = self.__saldo + self.__limite_de_credito
        return valor_de_saque <= valor_disponivel_de_saque

    def sacar(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print('Saldo realizado com sucesso... \n\tO saldo em conta, é: {} reais! '.format(self.__saldo))
        else:
            print('O valor de: {} reais, ultrapassa seu saldo disponível em conta! '.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saudo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite_de_credito(self):
        return self.__limite_de_credito

    @limite_de_credito.setter
    def limite_de_credito(self, limite_de_credito):
        self.__limite_de_credito = limite_de_credito

    @staticmethod
    def codigo_do_banco():
        return '001'

    @staticmethod
    def codigo_dos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}