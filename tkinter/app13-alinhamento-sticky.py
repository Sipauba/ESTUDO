from tkinter import *

root = Tk()
root.title('Login')

# A propriedade sticky define o alinhamento do texto dentro do campo. Seu parâmetro são os pontos cardeais
Label(root, text='Usuário:').grid(row=0, sticky=W)
Label(root, text='Senha:').grid(row=1, sticky=W)

# O método Entry cria um campo de entrada de texto
text_usuario = Entry(root).grid(row=0,column=1)
text_senha = Entry(root).grid(row=1,column=1)

btn_login = Button(root, text='Login').grid(row=2, column=1, sticky=E)
root.mainloop()
