from tkinter import *
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from lexer import lexicalAnalizer

import os


class Gui:

    def __init__(self):
        self.MainWindow = Tk()

        ####################################  Centra la ventana  #######################################################

        w = 1000
        h = 800

        ws = self.MainWindow.winfo_screenwidth()
        hs = self.MainWindow.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        self.MainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

        ################################################################################################################

        self.MainWindow.title("TEC Writing Machine")
        self.MainWindow.geometry("1000x800")
        self.OptionBar = Canvas(self.MainWindow, width=1003, height=1031, bg="white").place(x=-3, y=-3)

        # Buttons
        Button(self.OptionBar, text="Abrir", bg="#37AF97", fg="black" , command=self.OpenButtonClick).place(x=5, y=2)
        Button(self.OptionBar, text="Guardar ",bg="#37AF97", fg="black", command=self.SaveButtonClick).place(x=50, y=2)
        Button(self.OptionBar, text="COMPILAR", bg="orange", fg="black", command=self.compileButtonClick).place(x=800, y=505)
        Button(self.OptionBar, text="SALIR", bg="red", fg="black",command=lambda: self.MainWindow.destroy()).place(x=945, y=1)

        # Inserta las dos areas de texto

        self.CodeTextArea = Text(self.MainWindow, bg='#FFFFFF')
        self.CodeTextArea.place(x=40, y=30, width=980, height=470)

        self.OutputTextArea = Text(self.MainWindow, bg='#FFFFFF')
        self.OutputTextArea.place(x=40, y=535, width=980, height=260)

        

        self.MainWindow.mainloop()

    def OpenButtonClick(self):
        nombrearch = fd.askopenfilename(initialdir="/", title="Seleccione archivo",
                                        filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombrearch != '':
            archi1 = open(nombrearch, "r", encoding="utf-8")
            contenido = archi1.read()
            archi1.close()
            self.setCodeTextArea(contenido)

    def SaveButtonClick(self):
        nombrearch = fd.asksaveasfilename(initialdir="/", title="Guardar como",
                                          filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
        if nombrearch != '':
            archi1 = open(nombrearch, "w", encoding="utf-8")
            archi1.write(self.CodeTextArea.get("1.0", END))
            archi1.close()
            mb.showinfo("Información", "Los datos fueron guardados en la siguiente ruta: " + nombrearch + ".")


    def compileButtonClick(self):
        cadena = self.CodeTextArea.get("1.0", END)
        lista = lexicalAnalizer(cadena)
        print(lista)
        for i in lista:
            self.OutputTextArea.insert(INSERT, i)
            self.OutputTextArea.insert(INSERT, '\n')


    def setCodeTextArea(self, output):
        self.CodeTextArea.delete('1.0', END)
        self.CodeTextArea.insert(INSERT, output)

    def setOutputText(self, output):
        self.OutputTextArea.insert(INSERT, output)







IDE = Gui()
