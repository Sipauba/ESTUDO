from tkinter import * 

class MinhaFrame(Frame):
    def __init__(self, parent):
        super().__init__()
        
        self['bd'] = 1
        self['relief'] = SOLID
        
        self.text_1_text = StringVar()
        self.label_1_text = StringVar()
        
        # Widgets
        self.label_1 = Label(self, textvariable = self.label_1_text).grid()
        text_1 =Entry(self, textvariable = self.text_1_text).grid()
        cmd_1 = Button(self, text='Clique', command=self.Executar).grid()
        
    def Executar(self):
        self.label_1_text.set('Olá, {}.'.format(self.text_1_text.get()))

root = Tk()

MinhaFrame(root).grid()

root.mainloop() 