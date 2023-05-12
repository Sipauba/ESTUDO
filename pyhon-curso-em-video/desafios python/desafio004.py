variavel = input('Digite algo: ')
tipo = type(variavel)
print('O tipo primitivo da variável é: {}'.format(tipo))
print('É  alfa numérico? ', variavel.isalnum())
print('É alfabético? ', variavel.isalpha())
print('É decimal? ', variavel.isdecimal())
print('É numérico? ', variavel.isnumeric())
print('É imprimível? ', variavel.isprintable())



