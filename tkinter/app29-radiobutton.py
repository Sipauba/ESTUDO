from tkinter import * 

root = Tk()

frameA = Frame(root, bd=1,relief=SOLID)
frameA.pack()

frameB = Frame(root, bd=1,relief=SOLID)
frameB.pack()

# Esta variável irá armazenar o valor do radio A e B
valor_a = IntVar()
valor_b = IntVar()

def radio_func_1():
    print('Opção 1')

def radio_func_2():
    print('Opção 2')

def radio_func_3():
    print('Opção 3')

# O método parâmetro indicatoron irá mudar o formato da marcação do radio
# Só possui os valores 1 ou 0, sendo o 1 o padrão
# FRAME A
radio_1 = Radiobutton(frameA,
        text='Opção A 1',
        variable=valor_a,
        value=1,
        command=radio_func_1,
        indicatoron=1)

radio_2 = Radiobutton(frameA,
        text='Opção A 2',
        variable=valor_a,
        value=2,
        command=radio_func_2,
        indicatoron=1)

radio_3 = Radiobutton(frameA,
        text='Opção A 3',
        variable=valor_a,
        value=3,
        command=radio_func_3,
        indicatoron=1)

radio_1.pack()
radio_2.pack()
radio_3.pack()

# FRAME B

radio_4 = Radiobutton(frameB,
        text='Opção B 1',
        variable=valor_b,
        value=1,
        command=radio_func_1,
        indicatoron=1)

radio_5 = Radiobutton(frameB,
        text='Opção B 2',
        variable=valor_b,
        value=2,
        command=radio_func_2,
        indicatoron=1)

radio_6 = Radiobutton(frameB,
        text='Opção B 3',
        variable=valor_b,
        value=3,
        command=radio_func_3,
        indicatoron=1)

radio_4.pack()
radio_5.pack()
radio_6.pack()

# Este método fará com que ao iniciar o programa o radio1 já esteja marcado
radio_1.select()

def ver_radio():
    print(valor_a.get())

cmd = Button(root,
             text='Executar',
             command=ver_radio)

cmd.pack()

root.mainloop()