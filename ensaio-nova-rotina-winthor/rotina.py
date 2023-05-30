from tkinter import *
from tkinter import ttk
import mysql.connector

# Variável que irá conectar a aplicação com o banco de dados
conecta_banco = mysql.connector.connect(
    host='192.168.40.112',
    user='mateus19',
    password='florentim19',
    database='db_teste'
)

cursor = conecta_banco.cursor()

def consultar():
    # Executa um comando SQL para cbuscar todos os dados da tabela
    cursor.execute('select * from tbteste')

    # Limpa todo o campo da treeview para apresentar o novo resultado
    tree.delete(*tree.get_children())

    # Preenche a treeview com o resultado da consulta
    for linha in cursor:
        # Este comando vai percorrer cada linha encontrada na consulta e inserir na treeview
        tree.insert('','end',values=linha)

    cursor.close()
    conecta_banco.close()


root = Tk()
#root.geometry('300x200')

frame = Frame(root)

btn = Button(root,text='Consultar',command=consultar)
btn.pack()

# Define o a quantidade de colunas
tree = ttk.Treeview(root, columns=('coluna1','coluna2','coluna3'))
# Nomeia o cabeçalho das colunas
tree.heading('coluna1',text='ID')
tree.heading('coluna2',text='Nome')
tree.heading('coluna3',text='Idade')
# Por padrão é incluido uma coluna inicial 'obrigatória' (columnId) que pode ser ocutada com o comando abaixo
tree.column('#0',width=0)
tree.pack()

root.mainloop()