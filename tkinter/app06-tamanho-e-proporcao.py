from tkinter import *

menu_inicial =Tk()
menu_inicial.title('Título')
# Este código foi criado para demonstrar que o WIDTH é proporcional ao tamanho da fonte
# Nos dois labels abaixo, os dois possuem o mesmo valor de width, porém na prática não são o mesmo, já que o tamanho da fonte é diferente
label_1 =Label(menu_inicial,
                      text='Este é o Label 1',
                      font='Arial 20',
                      bg='red',
                      width=20)
label_1.pack()

label_2 =Label(menu_inicial,
                      text='Este é o Label 1',
                      font='Arial 40',
                      bg='red',
                      width=20)
label_2.pack()

menu_inicial.mainloop()

