# faça um programa que leia o comprimento doo cateto oposto e do cateto adjacente
# de um triângulo retângulo e calcule o comprimento da hipotenusa

from math import pow
cat1 = int(input('Informe a medida do primeiro cateto(cm): '))
cat2 = int(input('Informe a medida do segundo cateto(cm): '))

hip = int(pow(cat1,2) + pow(cat2,2))
print('O valor da Hipotenusa é: {}'.format(hip))

