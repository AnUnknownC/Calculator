from tkinter import *
from math import *
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x600")
ventana.resizable(False, False)
ventana.configure(background = "gray42")
Pantalla = Entry(ventana, font = ("arial", 20, "bold"), width = 22, borderwidth = 10, background = "CadetBlue1")
# Pantalla.place(x = 20, y = 60) #Usa coordenadas para situar los widgets (botones en la pantalla)
Pantalla.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 20)

buttonColor = "gray99"
widthButton = 10
heightButton = 3

Button0 = Button(ventana, text = "0", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 1, column = 0, pady = 10)
Button1 = Button(ventana, text = "1", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 1, column = 1, pady = 10)
Button2 = Button(ventana, text = "2", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 1, column = 2, pady = 10)
Button3 = Button(ventana, text = "3", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 1, column = 3, pady = 10)

Button4 = Button(ventana, text = "4", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 2, column = 0, pady = 10)
Button5 = Button(ventana, text = "5", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 2, column = 1, pady = 10)
Button6 = Button(ventana, text = "6", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 2, column = 2, pady = 10)
Button7 = Button(ventana, text = "7", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 2, column = 3, pady = 10)

Button8 = Button(ventana, text = "8", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 3, column = 0, pady = 10)
Button9 = Button(ventana, text = "9", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 3, column = 1, pady = 10)
ButtonPi = Button(ventana, text = "pi", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 3, column = 2, pady = 10)
ButtonDot = Button(ventana, text = ".", bg = buttonColor, width = widthButton, height = heightButton).grid(row = 3, column = 3, pady = 10)

ventana.mainloop()