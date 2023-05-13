# Um professor que sortear um dos alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import randint

sorteio = randint(1,5)

if sorteio == 1:
    print('Mateus foi o escolhido!')
elif sorteio == 2:
    print('Ana foi a escolhida!')
elif sorteio == 3:
    print('Rita foi a escolhida!')
elif sorteio == 4:
    print('Sipa foi o escolhido!')
elif sorteio == 5:
    print('Ana Rita foi a escolhida!')
