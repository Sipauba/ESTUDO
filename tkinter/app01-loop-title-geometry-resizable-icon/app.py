from tkinter import *

# Inicia a janela. É necessário o mainloop, pois se não a janela inicia e fecha instantaneamente.
# O mainloop mantém a aplicação aberta, como o void loop do c++
menu_inicial = Tk()
menu_inicial.title('Primeiro APP')

# 500x250 é a dimensão da janela e o 200+200 é a posição que a janela irá iniciar na tela
menu_inicial.geometry('500x250+200+200')

# Este objeto recebe dois parâmetros booleanos para dizer se vai ser permitido ou não redimencionar a largura e a altura
menu_inicial.resizable(True,True)
# Define os valores mínimos para redimensionamento da janela
#menu_inicial.minsize(500,250)
# Define os valores máximo para o redimensionamento da janela
#menu_inicial.maxsize(700,400)
# O parâmetro zoomed faz com que a aplicação seja iniciada maximizada
# E o iconic faz com que a aplicação seja iniciada minimizada
#menu_inicial.state('iconic')
menu_inicial.iconbitmap('imagem/icon.ico')
menu_inicial.mainloop()