from tkinter import * 

menu_inicial = Tk()

menu_inicial.title('Título')
menu_inicial.geometry('500x500')

# Desta forma os dois objetos serão alocados de cima para baixo (um em cima do outro)
label1 = Label(menu_inicial, text='Label 1', font='Arial 20', bg='red')
label2 = Label(menu_inicial, text='Label 2', font='Arial 20', bg='green')
label3 = Label(menu_inicial, text='Label 2', font='Arial 20', bg='blue')

#label1.pack()
#label2.pack()

# O Pack e o grid não funcionam bem juntos, dando problemas na geometria
# Após a elaboração dos argumentos das labels, é necessário definir em qual posição de linha ou coluna serão exibidos
# Exemplo: se eu definir a posição 1 e 9, se não houver nada entre essas posições, o espaço será ignorado e será considerado 1 e 2
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)

btn1 = Button(menu_inicial,text='Botão 1')
btn2 = Button(menu_inicial,text='Botão 2')
btn3 = Button(menu_inicial,text='Botão 3')

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)


menu_inicial.mainloop()