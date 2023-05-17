from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Título')
menu_inicial.geometry('500x500')
# O \n serve pra fazer a quebra de linha
# O argumento bd pode ser escrito como borderwidth e surtirá o mesmo efeito
# O bd é a expessura da borda
label_1 = Label(
    menu_inicial,
    text='Frase 1\nFrase 2',
    font='Arial 20',
    bd=1,
    relief='solid'
).pack()


menu_inicial.mainloop()