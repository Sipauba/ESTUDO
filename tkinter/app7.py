from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Título')
menu_inicial.geometry('500x500')
# O \n serve pra fazer a quebra de linha
# O argumento bd pode ser escrito como borderwidth e surtirá o mesmo efeito
# O bd é a expessura da borda
# Relief é o tipo de borda
label_1 = Label(
    menu_inicial,
    text='solid\nFrase 2',
    font='Arial 20',
    bd=10,
    relief='solid'
).pack()

label_2 = Label(
    menu_inicial,
    text='flat\nFrase 2',
    font='Arial 20',
    bd=10,
    relief='flat'
).pack()

label_3 = Label(
    menu_inicial,
    text='raised\nFrase 2',
    font='Arial 20',
    bd=10,
    relief='raised'
).pack()

label_4 = Label(
    menu_inicial,
    text='sunken\nFrase 2',
    font='Arial 20',
    bd=10,
    relief='sunken'
).pack()

label_5 = Label(
    menu_inicial,
    text='ridge\nFrase 2',
    font='Arial 20',
    bd=10,
    relief='ridge'
).pack()

label_6 = Label(
    menu_inicial,
    text='groove\nFrase 2',
    font='Arial 20',
    bd=50,
    relief='groove'
).pack()


menu_inicial.mainloop()