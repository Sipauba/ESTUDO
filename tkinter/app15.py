from tkinter import *

# Sempre definir as funções e a lógica antes de iniciar o GUI
def mostrarNome():
    nome = textbox_1.get()
    label_final = Label(root, text='Seu nome é {}'.format(nome))
    label_final.grid()

# Iniciando o GUI
root = Tk()
root.geometry('200x100')

# Criando os widgets
label_1 = Label(root, text='Escreva seu nome:')
textbox_1=Entry(root)
button_1 = Button(root, text='Executar', command=mostrarNome)

# Organizando os widgets
# Como não foi definido linhas e nem colunas, será exibido de cima para baixo na ordem que foi construido
label_1.grid()
textbox_1.grid()
button_1.grid()

root.mainloop()