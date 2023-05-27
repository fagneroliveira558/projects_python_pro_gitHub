class Data:
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

data1 = Data()
data1.dia = 1
data1.mes = 1
data1.ano = 1970
#print(data1)


data2 = Data()
data2.dia = 15
data2.mes = 2
data2.ano = 1992
print(data2)

