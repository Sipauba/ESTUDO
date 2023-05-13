# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

angulo = int(input('Informe o valor do ângulo(graus): '))
# só queria entender porque a função que converte para graus se chama radianos
# é confuso e contraditório
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Os valores trigonométricos são:')
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))
