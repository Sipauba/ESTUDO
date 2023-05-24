from tkinter import *

# Nesse caso é necessário converter o valor float para string para poder inclui-la na StringVar
# Para arredondar a temperatura em celsius podemos utilizar a função round
def converteTemp():
    F = float(textBox_1.get())
    C = (F-32)*5/9
    resultado.set('{} graus Celsius.'.format(str(round(C,1))))

root = Tk()
root.title('Aplicação')

resultado = StringVar()

label_1 = Label(root, text='Temp. Fahrenheit:' )
textBox_1 = Entry(root)
button_1 = Button(root, text='Converter',command=converteTemp)
label_2 = Label(root,textvariable=resultado)

label_1.grid()
textBox_1.grid()
button_1.grid()
label_2.grid()

root.mainloop()