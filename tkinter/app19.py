from tkinter import *

root = Tk()

root.title('App')

# Frame é como se fosse uma forma de encapsular os widgets em espaços definidos dentro da janela
# Nesse caso. é nessessáio incluir o frame no root e depois incluir o frame no parâmetro dos widgets como se fosse o root
frame_login = Frame(root)

label_usuario = Label(frame_login,text= 'Usuário: ')
label_password = Label(frame_login,text='Password: ')
text_usuario = Entry(frame_login)
text_password = Entry(frame_login)
cmd_entrar = Button(frame_login,text='Entrar')

label_usuario.grid(row=0,column=0)
label_password.grid(row=1,column=0)
text_usuario.grid(row=0,column=1)
text_password.grid(row=1,column=1)
cmd_entrar.grid(row=2,column=1)

frame_login.grid()

root.mainloop()