from tkinter import * 

root = Tk()
#root.geometry('400x300')

# O método widget reorganiza a mensagem de forma que possa caber no tamanho do widget
# Se o text apresentado for menor que o tamanho do widget, não haverá "espaço de sobra"  
t = Message(root,
            text='Este é o texto do message Widget.',
            width=100)
t.pack()

root.mainloop()