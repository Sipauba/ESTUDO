from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Título')
menu_inicial.geometry('500x300')
# É possível acrescentar inúmeros argumentos como a for da letra(fg), o background(bg), fonte
# Lembrando que a cor pode ser descrita como hexadecimal (ex: #000000)
label_1 = Label(menu_inicial, 
                text = 'Este é o Label 1',
                bg = 'yellow',
                fg = 'red',
                font = 'Times')
label_1.pack()
# Na fonte é possível colocar outros argumentos como tamanho da fonte, negrito e itálico
label_2 = Label(menu_inicial, 
                text = 'Este é o Label 1',
                bg = 'yellow',
                fg = 'red',
                font = 'Arial 20 bold italic')
label_2.pack()

menu_inicial.mainloop()