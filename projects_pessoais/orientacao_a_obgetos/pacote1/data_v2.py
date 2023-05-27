class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


data1 = Data()
data1.dia = 12
data1.mes = 10
data1.ano = 1970
print(data1)
