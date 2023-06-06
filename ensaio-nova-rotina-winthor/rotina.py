from tkinter import *
from tkinter import ttk
import cx_Oracle
from tkcalendar import DateEntry


# Parâmetros de conexão
host = '10.85.0.73'
servico = 'XE'
usuario = 'SYSTEM'
senha = 'CAIXA'

# Encontra o arquivo que aponta para o banco de dados
cx_Oracle.init_oracle_client(lib_dir="C:/oraclexe/app/oracle/product/10.2.0/server/NETWORK/ADMIN/instantclient_19_19")

# Faz a conexão ao banco de dados
conecta_banco = cx_Oracle.connect(usuario, senha, f'{host}/{servico}')

# Cria um cursor no banco para que seja possível fazer consultas e alterações no banco de dados
cursor = conecta_banco.cursor()

# Esta função executa a consulta que irá preencher a treeview com as informações sobre arequisição
def consultar():

    filial = campo_filial.get()
    num_req = campo_requisicao.get()
    data_ini = data_inicial.get_date()
    data_fin = data_final.get_date()

    consulta = 'SELECT NUMPREREQUISICAO, CODFILIAL, DATA, CODFUNCREQ, MOTIVO, SITUACAO, NUMTRANSVENDA FROM PCPREREQMATCONSUMOC WHERE CODFILIAL = {}'.format(filial)
    
    # Estas condições irão concatenar com o valor da variável 'consulta' dependendo se será fornecido o número da requisição ou as datas inicial e final
    if num_req:
        consulta += 'AND NUMPREREQUISICAO = {}'.format(num_req)
    if data_ini and data_fin:
        data_ini = data_ini.strftime('%d-%b-%Y')
        data_fin = data_fin.strftime('%d-%b-%Y')
        consulta += " AND DATA BETWEEN TO_DATE('{}', 'DD-MON-YYYY') AND TO_DATE('{}', 'DD-MON-YYYY')".format(data_ini, data_fin)
    """
    if data_ini and data_final:
        consulta += 'AND DATA BETWEEN {} AND {}'.format(data_ini, data_fin)
    """
    # Executa a consulta
    cursor.execute(consulta)

    # Limpa todos os dados que possam estar na treeview
    tree.delete(*tree.get_children())

    # Imprime linha a linha o resultado na treeview (da primeira até a ultima)
    for linha in cursor:
        tree.insert('','end', values=linha)


root = Tk()
root.geometry('800x500')
root.title('Status Req. Mat. Consumo')

#----------------------------------------------

# Frame que contém as informações iniciais necessárias para a consulta 
frame_cabecalho = Frame(root,
              width=640,
              height=110,
              relief=SOLID,
              bd=1,
              )
frame_cabecalho.pack(pady=(50,10))


#-------------------------------------------------------------

label_filial = Label(frame_cabecalho, text='Filial')
label_filial.grid(row=0, column=0, pady=(20,0))

campo_filial = ttk.Combobox(frame_cabecalho, width=4, values=['1','3','4','5','6','17','18','19','20','61','70','99'])
campo_filial.current(4)
campo_filial.grid(row=1, column=0, pady=(0,20), padx=(20,0))

label_num_req = Label(frame_cabecalho, text='Nº Requisição')
label_num_req.grid(row=0, column=1, pady=(20,0))

campo_requisicao = Entry(frame_cabecalho)
campo_requisicao.grid(row=1, column=1, pady=(0,20), padx=(20,0))

label_data_ini = Label(frame_cabecalho, text='Data Inicial')
label_data_ini.grid(row=0, column=2, pady=(20,0))

data_inicial = DateEntry(frame_cabecalho, date_pattern='dd/mm/yyyy')
data_inicial.set_date(None)
data_inicial.grid(row=1, column=2, pady=(0,20), padx=(20,0))

label_data_fin = Label(frame_cabecalho, text='Data Final')
label_data_fin.grid(row=0,column=3, pady=(20,0))

data_final = DateEntry(frame_cabecalho, date_pattern='dd/mm/yyyy')
data_final.set_date(None)
data_final.grid(row=1,column=3,  pady=(0,20), padx=(20,20))

#-------------------------------------------------------------------

# Frame apenas para conter os radios
frame_radio = Frame(root)
frame_radio.pack()

valor_radio = IntVar()

def aprovados():
    print('Aprovados')
    
def cancelados():
    print('Cancelados')

def todos():
    print('Todos')

radio_aprov = Radiobutton(frame_radio,text='Aprovados', variable = valor_radio, value=1, command=aprovados, indicatoron=1)
radio_aprov.grid(row=0, column=0)

radio_cancel = Radiobutton(frame_radio,text='Cancelados', variable = valor_radio, value=2, command=cancelados, indicatoron=1)
radio_cancel.grid(row=0,column=1)

radio_todos = Radiobutton(frame_radio,text='Todos', variable = valor_radio, value=3, command=todos, indicatoron=1)
radio_todos.grid(row=0, column=2)

radio_todos.select()

btn = Button(root, text='Pesquisar', command=consultar)
btn.pack(pady=(20,30))

# Define o a quantidade de colunas
tree = ttk.Treeview(root, columns=('coluna1','coluna2','coluna3','coluna4','coluna5','coluna6','coluna7'))

# Nomeia o cabeçalho das colunas
tree.heading('coluna1',text='NUMREQ')
tree.heading('coluna2',text='FILIAL')
tree.heading('coluna3',text='DATA')
tree.heading('coluna4',text='CODFUNC')
tree.heading('coluna5',text='MOTIVO')
tree.heading('coluna6',text='SITUACAO')
tree.heading('coluna7',text='TRANSVENDA')

tree.column('coluna1', width=60)
tree.column('coluna2', width=40)
tree.column('coluna3', width=90)
tree.column('coluna4', width=90)
tree.column('coluna5', width=90)
tree.column('coluna6', width=70)
tree.column('coluna7', width=90)

# Por padrão é incluido uma coluna inicial 'obrigatória' (columnId) que pode ser ocultada com o comando abaixo
tree.column('#0',width=0)

tree.pack()

# Define a posição e as dimensões da treeview na janela
x = 50
y = 250
width = 700
height = 200
tree.place(x=x, y=y, width=width, height=height)

root.mainloop()
#