from tkinter import *


root = Tk()

lista_1 = Listbox(root)
lista_1.pack()
lista_2 = Listbox(root)
lista_2.pack()
lista_3 = Listbox(root)
lista_3.pack()

# Inserir um item de cada vez
# É necessário que os item sejam todos do tipo string
# O número representa a posição do item na lista, porém, se o número for substituido pelo argumento END a ordem da lista será definida pela ordem que foi escrita no códogo
lista_1.insert(0,"Primeiro item da lista")
lista_1.insert(1,"Segundo item da lista")
lista_1.insert(3,"Terceiro item da lista")

lista_2.insert(END,"Quarto item da lista")
lista_2.insert(END,"Quinto item da lista")
lista_2.insert(END,"Sexto item da lista")

# Inserindo vários itens a partir de uma list
nomes = ['João','Ana','Carlos']
for nome in nomes:
    lista_3.insert(END,nome)

# Deletando itens da lista
# Os parâmetros do delete é a primeira posiçãoo e a última posição
#lista_1.delet(0,2)

# Imprimindo no console o item elecionado da lista
def executar():
    print(lista_1.get(ACTIVE))

cmd= Button(root, text='Clique', command=executar)
cmd.pack()

root.mainloop()