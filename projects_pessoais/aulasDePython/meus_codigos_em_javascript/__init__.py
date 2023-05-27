a = float(input('Digite o primeiro lado do triângulo: '))
b= float(input('Digite o segundo lado do triângulo: '))
c = float(input('Digite o terceiro lado do triângulo: '))

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print('Este triângulo é equilátero!!! ')

