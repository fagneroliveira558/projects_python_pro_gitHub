from datetime import datetime


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
    casa = []
    casa.append(Tarefa('Lavar roupas'))
    casa.append(Tarefa('Estender roupas'))
    casa.append(Tarefa('Passar roupas'))
    casa.append(Tarefa('Guardar roupas'))
    casa.append(Tarefa('Lavar pratos'))
    casa.append(Tarefa('Secar pratos'))
    casa.append(Tarefa('Guardar pratos'))


    for tarefa in casa:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()
