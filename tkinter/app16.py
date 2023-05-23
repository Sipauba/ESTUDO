from tkinter import *
# Função que irá alterar o valor do textvariable e exibir na label_2
def mostrarNome():
    vartexto.set('O seu nome é {}'.format(textBox_1.get()))
    

root = Tk()
root.title('Aplicação')

# Definindo o valor da variável como StringVar. Isso é importante, pois o textvariable só funciona com esse tipo de variável
vartexto = StringVar()

# Definindo os Widgets. Observe que o label_2 possui textvariable que será definido pelo textbox_1 e depois exibido após execução da função mostrarNome
label_1 = Label(root,text='O seu nome é:')
textBox_1 = Entry(root)
button_1 = Button(root,text='Executar',command=mostrarNome)
label_2 = Label(root,textvariable=vartexto)

# Posicionando os Widgets
label_1.grid()
textBox_1.grid()
button_1.grid()
label_2.grid()

root.mainloop()