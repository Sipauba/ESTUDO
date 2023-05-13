# O mesmo professor do desafio anterior que sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos alunos
# e mostre a ordem sorteada. 

from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')

alunos = [n1,n2,n3]
sorteado = shuffle(alunos)

print('A ordem de apresentação é: {}'.format(alunos))