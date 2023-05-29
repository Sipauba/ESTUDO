from tkinter import * 

root = Tk()
root.geometry('300x200')

# Cria o menu
meuMenu = Menu(root)

def fileNew_click():
    print('FileMenu_Click')

# Menu File
# Cria as opções do menu
# Tearoff é um parâmetro que possibilita destacar o submenu da aplicação, arrancado-a da sua posição
fileMenu = Menu(meuMenu, tearoff=0)
fileMenu.add_command(label='New', command=fileNew_click)
fileMenu.add_command(label='Open')
fileMenu.add_command(label='Save')
# Separator cria uma linha que respeita a ordem como o código foi escrito
fileMenu.add_separator()
fileMenu.add_command(label='Exit')
# Define como será exibido o submenu
meuMenu.add_cascade(label='File', menu=fileMenu)

# Menu Edit
editMenu = Menu(meuMenu, tearoff=0)
editMenu.add_command(label='Copy')
editMenu.add_command(label='Past')
editMenu.add_command(label='Select all')
meuMenu.add_cascade(label='Edit', menu=editMenu)

# Define meuMenu como menu
root.config(menu=meuMenu)

root.mainloop()