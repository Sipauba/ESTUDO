from tkinter import * 

menu_inicial = Tk()

menu_inicial.title('Título')
menu_inicial.geometry('500x500')

# Forma alternativa de definir o valor do texto foda do método da label
# O set é para incluitr o valor na variável texto
texto = StringVar()
texto.set('Novo texto')

label1 = Label(
    menu_inicial,
    textvariable=texto,
    font='Arial 20',
    bg='red',
    fg='white'
)
label1.pack()
menu_inicial.mainloop()