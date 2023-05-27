from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []


    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))


    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]


    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'



#Classe responsável por erdar ação e comportamento!
#Subclasse a seguir!
class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()


    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito else '')



def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Lavar roupas')
    casa.add('Estender roupas')
    casa.add('Passar roupas')
    casa.add('Guardar roupas')
    casa.add('Lavar pratos')
    casa.add('Secar pratos')
    casa.add('Guardar pratos')
    print(casa)


    casa.procurar('Lavar roupas').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    print(casa)

    mercado = Projeto('Fazer compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Frutas frescas')
    mercado.add('Carne de frango')
    mercado.add('Carne de porco')
    mercado.add('Carne de boi')
    mercado.add('Tomates')
    mercado.add('Alface')
    mercado.add('Couve')
    mercado.add('Brócoles')
    print(mercado)

    comprar_carne = mercado.procurar('Carne de frango')
    comprar_carne.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')
    print(mercado)

if __name__ == '__main__':
    main()
