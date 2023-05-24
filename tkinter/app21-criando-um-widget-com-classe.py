from tkinter import * 

# Criando um widget
# Criando uma classe para o widget herdando tudo da classe Frame
class FrameNome(Frame):
    # Self é um mecaminismo interno da p´ropria classe
    def __init__(self, meuMaster):
        # A linha abaixo vai chamar o construtor da da super classe Frame
        super().__init__()
        # Alterando os valores da superclasse
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID
        
        # O self vai funcionar como root dentro da classe
        label_nome = Label(self, text='Nome: ')
        text_nome = Entry(self)
        
        label_nome.grid(row=0, column=0)
        text_nome.grid(row=0, column=1)

root = Tk()
root.title('App')

frame_nome_1 = FrameNome(root).grid()

        
root.mainloop()