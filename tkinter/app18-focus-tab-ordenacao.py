from tkinter import * 

def executar():
    label_1['text'] = t1.get()
    label_2['text'] = t2.get()
    label_3['text'] = t3.get()

root = Tk()

root.title('Aplicação')

t1=Entry(root)
t2=Entry(root)
t3=Entry(root)

label_1 = Label(root)
label_2 = Label(root)
label_3 = Label(root)

botao = Button(root,text='Executar',command=executar)

# Ao selecionar um dos campos e pressionar TAB, o cursor será movido para o próximo campo respeitando a ordem em que os campos foram dispostos abaixo
t1.grid()
t2.grid()
t3.grid()

label_1.grid()
label_2.grid()
label_3.grid()

botao.grid()


# O parâmetro focus faz com que ao abrir o arquivo o cursor já esteja no campo selecionado
t1.focus()

root.mainloop()

# Esta aplicação tem o objetivo de demonstrar que a ordem que o código é escrito pode alterar alguns pontos no funcionamento do programa