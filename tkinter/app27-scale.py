from tkinter import *

root = Tk()
root.geometry('300x200')

# Esta função vai pegar o valor da scale e imprimir esse valor no console 
def vervalor():
    print(slide.get())

# Este método cria um widget que controla uma espécie de scroll para controle de "volume" 
# Estes parâmetros definem onde começa e onde termina e define a orientação pela horizontal
# Resolution define que a escala mude de valor de 0.5 a 0.5
slide = Scale(root,
              from_=0,
              to=100,
              orient=HORIZONTAL,
              resolution=0.5)
slide.pack()

cmd = Button(root,
             text='Ver Valor',
             command=vervalor)
cmd.pack()

root.mainloop()