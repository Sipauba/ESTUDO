from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Título')
# Define o tamanho da janela
menu_inicial.geometry('500x300')
# Muda a cor do BackGround da janela para azul
#menu_inicial['bg'] = 'blue'
# Essa será a funçção que será execultada ao clicar no botão. É importante que a função seja definida antes da chamada dda função
def clique(mensagem):
    print (mensagem)
# Para criar um botão, o termo btn pode ser qualquer palavra de minha preferência. Text é o texto que ficará impresso no botão e command vai buscar uma função para executar ao pressionar o botão
# A expressão lambda é para que a função do comando só seja executada ao realizar o clique, sem essa expressão, o programa já executa a função e ao clicar não acontece nada
btn1 = Button(menu_inicial, text='Executar', command=lambda:clique('Nova mensagem'))
btn1.pack()
btn2 = Button(menu_inicial, text='Clicar', command=lambda:print('OK'))
btn2.pack()

menu_inicial.mainloop()