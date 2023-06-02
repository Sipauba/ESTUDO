from tkinter import *
from tkinter import ttk
import mysql.connector
from tkcalendar import DateEntry

"""
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

"""

root = Tk()
root.geometry('800x500')
root.title('Status Req. Mat. Consumo')



#----------------------------------------------

frame_cabecalho = Frame(root,
              width=640,
              height=110,
              relief=SOLID,
              bd=1,
              )
frame_cabecalho.pack(pady=(50,10))

frame_radio = Frame(root)
frame_radio.pack()

#-------------------------------------------------------------

label_filial = Label(frame_cabecalho, text='Filial')
label_filial.grid(row=0, column=0, pady=(20,0))

campo_filial = ttk.Combobox(frame_cabecalho, width=4, values=['1','3','4','5','6','17','18','19','20','61','70','99'])
campo_filial.grid(row=1, column=0, pady=(0,20), padx=(20,0))

label_num_req = Label(frame_cabecalho, text='Nº Requisição')
label_num_req.grid(row=0, column=1, pady=(20,0))

campo_requisicao = Entry(frame_cabecalho)
campo_requisicao.grid(row=1, column=1, pady=(0,20), padx=(20,0))

label_data_ini = Label(frame_cabecalho, text='Data Inicial')
label_data_ini.grid(row=0, column=2, pady=(20,0))

data_inicial = DateEntry(frame_cabecalho, date_pattern='dd/mm/yyyy')
data_inicial.grid(row=1, column=2, pady=(0,20), padx=(20,0))

label_data_fin = Label(frame_cabecalho, text='Data Final')
label_data_fin.grid(row=0,column=3, pady=(20,0))

data_final = DateEntry(frame_cabecalho, date_pattern='dd/mm/yyyy')
data_final.grid(row=1,column=3,  pady=(0,20), padx=(20,20))

#-------------------------------------------------------------------

valor_rad_aprov = IntVar()
valor_rad_cancel = IntVar()
valor_rad_todos = IntVar()

radio_aprov = Radiobutton(frame_radio,text='Aprovados', variable = valor_rad_aprov, value=1, indicatoron=1)
radio_aprov.grid(row=0, column=0)

radio_cancel = Radiobutton(frame_radio,text='Cancelados', variable = valor_rad_cancel, value=2, indicatoron=1)
radio_cancel.grid(row=0,column=1)

radio_todos = Radiobutton(frame_radio,text='Todos', variable = valor_rad_todos, value=3, indicatoron=1)
radio_todos.grid(row=0, column=2)

btn = Button(root,text='Pesquisar')
btn.pack(pady=(20,30))

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