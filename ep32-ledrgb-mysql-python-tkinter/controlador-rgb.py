from tkinter import *
import mysql.connector

#----------------------------------------

conexao = mysql.connector.connect(
    host='192.168.40.112',
    user='mateus19',
    password='florentim19',
    database='db_teste'
)

#-------------------------------------------------------------------------

def atualiza_cor(valor):
    valor_red = int(red.get())
    valor_green = int(green.get())
    valor_blue = int(blue.get())
    
    print('R:{} G:{} B:{}'.format(valor_red, valor_green, valor_blue))

    altera_cor = f'#{valor_red:02x}{valor_green:02x}{valor_blue:02x}'
    cor_resultado.config(bg=altera_cor)

    cursor = conexao.cursor()
    cursor.execute('UPDATE RGB SET RED = {}, GREEN = {}, BLUE = {} WHERE ID = 1'.format(valor_red,valor_green, valor_blue))
    conexao.commit()
    

#-----------------------------------------------------------------------------

root = Tk()
root.title('Controlador RGB')
root.geometry('300x370')

#------------------------------------------------------------------------------------------

cores = Frame(root)
cores.pack()

label_red = Label(cores, text='Vermelho', fg='red')
label_green = Label(cores, text='Verde',fg='green')
label_blue = Label(cores, text='Azul', fg='blue')

red = Scale(cores, from_=0, to=255, orient=HORIZONTAL, fg='red', command=atualiza_cor)
green = Scale(cores, from_=0, to=255, orient=HORIZONTAL, fg='green',command=atualiza_cor)
blue = Scale(cores, from_=0, to=255, orient=HORIZONTAL, fg='blue',command=atualiza_cor)

label_red.grid(row=0, column=0)
red.grid(row=0, column=1)
label_green.grid(row=1, column=0)
green.grid(row=1, column=1)
label_blue.grid(row=2, column=0)
blue.grid(row=2, column=1)

#-----------------------------------------------------------------------------------------------

cor_resultado = Frame(root, width=20, height=20, bg='')
cor_resultado.pack()

root.mainloop()