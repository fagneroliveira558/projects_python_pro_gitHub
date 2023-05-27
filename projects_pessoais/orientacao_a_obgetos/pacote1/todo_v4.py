from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendentes(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento


    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Tarefa concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Tarefa vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Lavar roupas', datetime.now())
    casa.add('Estender roupas', datetime.now())
    casa.add('Passar roupas', datetime.now())
    casa.add('Guardar roupas', datetime.now())
    casa.add('Lavar pratos', datetime.now())
    casa.add('Secar pratos', datetime.now())
    casa.add('Guardar pratos', datetime.now())
    print(casa)

    casa.procurar('Lavar pratos').concluir()
    for tarefa in casa:
        print(f'- {tarefa}')
    print(casa)


    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Frutas frescas')
    mercado.add('Carne de frango')
    mercado.add('Carne de porco')
    mercado.add('Carne de boi')
    mercado.add('Tomate', datetime.now() + timedelta(days=3, seconds=1))
    mercado.add('Alface', datetime.now() + timedelta(days=3, seconds=1))
    mercado.add('Couve', datetime.now() + timedelta(days=3, seconds=1))
    mercado.add('Brócoles', datetime.now() + timedelta(days=3, seconds=1))
    print(mercado)

    comprar_carne = mercado.procurar('Carne de frango')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)



if __name__ == '__main__':
    main()
