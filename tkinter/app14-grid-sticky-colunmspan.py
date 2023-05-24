from tkinter import * 

root = Tk()

root.title('Título')

# O parâmetro columnspan serve para definir quantas colunas o campo irá ocupar. No caso abaixo o terceiro campo ocupa os dois campos dos labels anteriores
# Observação: desta forma o terceiro campo fica centralizado e fica um pequeno espaço dos dois lados do campo
# Para resolver esse problema dos campos é só utilizar o parâmetro sticky e definir para alinar para esquerda e direita ao mesmo tempo, assim os espaço serão preenchidos
Label(root, width=20,bg='red').grid(column=0)
Label(root, width=20,bg='green').grid(column=1)
Label(root, width=40,bg='blue').grid(columnspan=2, sticky='we')

'''
Label(root,text='texto',bg='red').grid(column=0)
Label(root,text='texto',bg='green').grid(column=1)
Label(root,text='texto',bg='blue').grid(columnspan=2, sticky='we')
'''

root.mainloop()