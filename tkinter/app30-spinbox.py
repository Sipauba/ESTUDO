from tkinter import *

root= Tk()
root.geometry('300x200')

def executar():
    print(spinbox_1.get())
    print(spinbox_2.get())
    print(spinbox_3.get())

# Este método cria uma caixa de entrada de um valor numérico que pode ser incrementado por dois botões, um que aumenta e outro que diminui
spinbox_1 = Spinbox(root,from_=0,to=10)
spinbox_1.pack()

# O parâmetro wrap faz com que os valores voltem ao início ao finalizar os itens da lista
# O seu valor padrão é False
spinbox_2 = Spinbox(root, values=(10,20,30,40,50), wrap=True)
spinbox_2.pack()

# É possível acrescentar valores do tipo tring no spinbox
spinbox_3 = Spinbox(root, values=('Mateus','Ana','Rita'), wrap=True)
spinbox_3.pack()

# Botão criado para exibir o valor da spinbox
cmd = Button(root, text='Clique', command=executar)
cmd.pack()


root.mainloop()