from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Título')
menu_inicial.geometry('500x500')

# Duas formas diferentes de criar a label e preencher com os argumentos
label1 = Label(
    menu_inicial,
    text='Frase de teste',
    font='Arial 20',
    bd=1,
    relief='solid'
)
label1.pack()

# Essa forma pode ser necessária para alterar o valor do argumento de acordo com a necessidade do código
label2 = Label(menu_inicial)
label2['text'] = 'Texto da label 2'
label2['font'] = 'Arial 20' 
label2['bd'] = 1 
label2['relief'] = 'solid'
label2.pack()

# Este comando mostra todas as propriedades disponíveis
print(label2.keys())

# Este comando imprime no console todas as propriedades e os seus respectivos valores
for item in label2.keys():
    print('{} : {}'.format(item, label2[item]))

menu_inicial.mainloop()