# Um professor que sortear um dos alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import randint

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')

alunos = [n1,n2,n3]

sorteado = randint(0,2)

print('O aluno sorteado foi: {}!'.format(alunos[sorteado]))


