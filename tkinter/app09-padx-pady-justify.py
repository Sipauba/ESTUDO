from tkinter import *

menu_inicial = Tk()

menu_inicial.title('Título')
menu_inicial.geometry('500x500')

# O pad define a distância entre a borda externa até o conteúdo interno, ou seja, da borda até o começo da letra, seja horizontal (padx) ou vertical (pady)
label1 = Label(
    menu_inicial,
    text='Frase de teste',
    font='Arial 20',
    bd=1,
    relief='solid',
    padx=50,
    pady=50
)
label1.pack()

# A distância não é influenciada pelo tamanho da fonte
# Para justtificar utiliza-se o argumento justify com a direção em inglês e letras maiúsculas (LEFT, RIGHT e etc)
label2 = Label(
    menu_inicial,
    text='Frase de teste\nOutra frase de teste\nE outra',
    font='Arial 10',
    bd=1,
    relief='solid',
    padx=10,
    pady=10,
    justify=RIGHT
)
label2.pack()

# Se usarmos o justify sem utilizar o anchor o testeo será justificado sempre ao centro, mas obedecendo à instrução do argumento
label3 = Label(
    menu_inicial,
    text='Frase de teste\nOutra frase de teste\nE outra',
    font='Arial 10',
    bd=1,
    relief='solid',
    width=30,
    height=5,
    justify=LEFT,

)
label3.pack()

menu_inicial.mainloop()