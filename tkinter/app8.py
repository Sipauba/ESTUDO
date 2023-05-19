from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Título')
menu_inicial.geometry('500x300')
# Se as dimensões da label for menor que o conteúdo dela, a informação ficará cortada, nesse exemplo a fonte torna as letras maiores que o width = 7, por tanto o conteudo da label fica cortado.
# O argumento height neste caso define o espaço em quantidade de linhas, portanto, é diretamente afetado pelo tamanho da fonte
labe1 = Label(
    menu_inicial,
    text='0123456789\n0123456789\n0123456789',
    font='Arial 20',
    bd=1,
    relief='solid',
    width=25,
    height=2
)
labe1.pack()

# O argumento anchor irá definir o alinhamento do texto na label, o local do alinhamento é definido os pontos cardeais com letras maiúsculas e em inglês (N,S,E,W,NW,NE,SE,SW)
labe2 = Label(
    menu_inicial,
    text='0123456789',
    font='Arial 20',
    bd=1,
    relief='solid',
    width=25,
    height=4,
    anchor=N
)
labe1.pack()
menu_inicial.mainloop()
