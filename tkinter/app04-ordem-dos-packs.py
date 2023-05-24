from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Título')

label_1 = Label(menu_inicial, text = 'Este é o Label 1.')
label_2 = Label(menu_inicial, text = 'Este é o Label 2.')
cmd = Button(menu_inicial, text = 'Executar')
# A ordem que está os packs é a ordem que será exibido na janela
label_1.pack()
label_2.pack()
cmd.pack()


menu_inicial.mainloop()