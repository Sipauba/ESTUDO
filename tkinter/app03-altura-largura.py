from tkinter import *

menu_inicial = Tk()
menu_inicial.title('Titulo')

# Dimensões da janela
largura = 500
altura = 300

# Resolução do nosso sistema
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
print(largura_screen, altura_screen)

# Posição da janela
# Essa pequena equação fará com que a janela seja iniciada exatamente no centro da tela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# Definir a geometry
# O %d é como se fosse o {} do .format. As variáveis vão entrar nas espaços na mesma ordem que estão colocadas
menu_inicial.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

menu_inicial.mainloop()
