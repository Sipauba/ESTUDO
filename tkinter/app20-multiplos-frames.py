from tkinter import *

root = Tk()
root.title('App')

#----------- FRAME NOME WIDGETS --------------
frame_nome = Frame(root)

label_nome = Label(frame_nome,text='Nome: ')
label_apelido = Label(frame_nome,text='Apelido: ')

text_nome = Entry(frame_nome)
text_apelido = Entry(frame_nome)

#----------- FRAME MORADA WIDGETS --------------
frame_morada = Frame(root) 

label_rua = Label(frame_morada,text='Rua: ')
label_cidade = Label(frame_morada,text='Cidade: ')

text_rua = Entry(frame_morada)
text_cidade = Entry(frame_morada)

#----------- ROOT WIDGET --------------
cmd_salvar = Button(root,text='Salvar')

#----------- FRAME NOME LAYOUT --------------
label_nome.grid(row=0,column=0)
label_apelido.grid(row=1,column=0)
text_nome.grid(row=0,column=1)
text_apelido.grid(row=1,column=1)

#----------- FRAME MORADA LAYOUT --------------
label_rua.grid(row=0,column=0)
label_cidade.grid(row=1,column=0)
text_rua.grid(row=0,column=1)
text_cidade.grid(row=1,column=1)

#----------- LAYOUT DOS FRAMES --------------
# Os frames podem ser posicionados na grid de acordo com posicionamento de linhas e colunas
frame_nome.grid(row=0,column=0)
frame_morada.grid(row=0,column=1)

cmd_salvar.grid()



root.mainloop()