class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registrar_horas(self, horas):
        print('Horas registradas... ')

    def mostrar_tarefas(self):
        print('Fez muita coisa... ')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer... ')

    def busca_curso_do_mes(self, mes = None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos deste mês... ')


class Alura(Funcionario):
    #def mostrar_tarefas(self):
        #print('Fez muita coisa, Alurete... ')

    def busca_perguntas_sem_respostas(self):
        print('Mostrando perguntas não respondidas do fórum... ')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass


miguel = Junior('Miguel')
miguel.busca_perguntas_sem_respostas()
fagner = Pleno('Fagner')
fagner.busca_perguntas_sem_respostas()
fagner.busca_curso_do_mes()
fagner.mostrar_tarefas()
#print(fagner)
print(miguel)
