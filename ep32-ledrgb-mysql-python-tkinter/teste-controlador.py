import mysql.connector
from tkinter import *

#-----------------------------------------

conexao = mysql.connector.connect(
    host='192.168.40.112',
    user='mateus19',
    password='florentim19',
    database='db_teste'
)

def atualiza_cor():

    cursor = conexao.cursor()
    cursor.execute('SELECT RED FROM RGB WHERE ID = 1')
    red = cursor.fetchone()[0]
    cursor.execute('SELECT GREEN FROM RGB WHERE ID = 1')
    green = cursor.fetchone()[0]
    cursor.execute('SELECT BLUE FROM RGB WHERE ID = 1')
    blue = cursor.fetchone()[0]


    altera_cor = f'#{red:02x}{green:02x}{blue:02x}'
    frame.config(bg=altera_cor)

    root.after(1000,atualiza_cor)



#------------------------------------------

root = Tk()
root.title('Testa controlador RGB')
root.geometry('100x100')

#------------------------------------------

frame = Frame(root, width=80, height=80, bg='')
frame.pack()


atualiza_cor()

root.mainloop()