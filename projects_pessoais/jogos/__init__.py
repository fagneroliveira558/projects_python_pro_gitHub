import jogo_da_forca
import adivinhar
import forca_com_nomes_de_times

print('-'*30)
print('Muito bem-vindo ao nosso menu! ')
print('-'*30)
print('1. Adivinhação.')
print('2. Forca')
print('3. Forca com nomes de times')
escolha = int(input("E aí! Qual jogo quer jogar... "))
if escolha == 1:
    adivinhar.jogo_de_adivinhar()

elif escolha == 2:
    jogo_da_forca.jogar_jogo_da_forca()

elif escolha == 3:
    forca_com_nomes_de_times.jogar_forca_com_nomes_times()