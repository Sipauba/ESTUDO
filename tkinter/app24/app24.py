from tkinter import * 

root = Tk()

# É necessário incluir todo o caminho da imagem e substituir a contrabarra por barra 
# Não é possível alterar o tamanho da imagem no código, é necessário editar a imagem para que fique do tamanho desejado antes de incluí-la no código
img = PhotoImage(file="C:/Users/mateus.sipauba/Desktop/git/ESTUDO/tkinter/app24/images/print.png")

# A propriedade image inclui uma imagem no label
label_imagem = Label(root, image = img).pack()

root.mainloop()