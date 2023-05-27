class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self._nome} - Likes: {self._likes}!'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} minutos... \n\tLikes: {self.likes}... \n\t\tAno de lançamento: {self.ano}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas... \n\tLikes: {self.likes}... \n\t\tAno de lançamento: {self.ano}'

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas


    def __len__(self):
        return len(self._programas)

    def __getitem__(self, item):
        return self._programas[item]


vingadores = Filme('vingadores - guerra infinita', 2018, 160)

rei_leao = Filme('rei leão - o retorno', 2020, 90)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
abdn = Filme('a branca de neve - a volta das emoções', 2022, 100)
luta_rua = Filme('lutador de rua - quebrando regras', 2013, 90)


demolidor.dar_likes()
demolidor.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
rei_leao.dar_likes()
rei_leao.dar_likes()
rei_leao.dar_likes()
rei_leao.dar_likes()
rei_leao.dar_likes()
rei_leao.dar_likes()
rei_leao.dar_likes()
abdn.dar_likes()
abdn.dar_likes()
abdn.dar_likes()
abdn.dar_likes()
abdn.dar_likes()
abdn.dar_likes()
abdn.dar_likes()
abdn.dar_likes()
luta_rua.dar_likes()
luta_rua.dar_likes()
luta_rua.dar_likes()
luta_rua.dar_likes()
luta_rua.dar_likes()
luta_rua.dar_likes()
luta_rua.dar_likes()
luta_rua.dar_likes()



listinha = [vingadores, atlanta, demolidor, tmep, rei_leao, abdn, luta_rua]

minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(len(minha_playlist))