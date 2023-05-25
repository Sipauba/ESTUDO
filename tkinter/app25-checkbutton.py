from tkinter import * 

root = Tk()

# Função criada para exibir no console o valor atual da checkbox
def apresentar():
    print(valor_check.get())

# O valor da checkbox é inteiro ou boleano (0,1)
valor_check = IntVar()

check = Checkbutton(
    root,
    text='Esta é uma CHECKBOX',
    variable=valor_check,
    command=apresentar
    ).pack()

root.mainloop()