from tkinter import * 

root = Tk()
root.geometry('300x200')

def abrirFormulario():
    # Cria uma nova janela dentro do root
    top = Toplevel()
    top.title('Novo formulário')
    top.geometry('200x100')
    label_1 = Label(top,text='Label na nova janela')
    label_1.pack()

btn = Button(root, text='Novo...', command=abrirFormulario)
btn.pack()

root.mainloop()