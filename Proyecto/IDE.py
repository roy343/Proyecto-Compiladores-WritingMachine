from tkinter import *
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from lexer import lexicalAnalizer
from Parser import sintacticAnalizer


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

        self.MainWindow.configure(bg="#040625")

        # Buttons
        Button(self.MainWindow, text="ABRIR", background = "white", foreground = "black" ,command=self.OpenButtonClick).place(x=5, y=1)
        Button(self.MainWindow, text="GUARDAR", background = "white", foreground = "black" ,command=self.SaveButtonClick).place(x=47.5, y=1)
        Button(self.MainWindow, text="COMPILAR", background = "yellow", foreground = "black" , command=self.compileButtonClick).place(x=550, y=1)
        Button(self.MainWindow, text="CORRER", background = "yellow", foreground = "black" , command=self.compileButtonClick).place(x=620, y=1)
        Button(self.MainWindow, text="SALIR", background = "red", foreground = "black" ,command=lambda: self.MainWindow.destroy()).place(x=945, y=1)

        # Inserta las dos areas de texto

        self.CodeTextArea = Text(self.MainWindow, font = 14, bg='#040625', fg="white")
        self.CodeTextArea.place(x=30, y=30, width=960, height=500)

        self.OutputTextArea = Text(self.MainWindow, font = 14 ,bg='#040625', fg="white")
        self.OutputTextArea.place(x=30, y=535, width=960, height=260)

        self.MainWindow.mainloop()

    def OpenButtonClick(self):
        nombrearch = fd.askopenfilename(initialdir=".", title="Seleccione archivo",
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

        if cadena != "":
            lista = lexicalAnalizer(cadena)
            #print(cadena)
            sintacticAnalizer(cadena)
            for i in lista:
                self.OutputTextArea.insert(INSERT,i)
                self.OutputTextArea.insert(INSERT,'\n')
                
        else:
            mb.showwarning("Error","Debes escribir código!!")

    def setCodeTextArea(self, output):
        self.CodeTextArea.delete('1.0', END)
        self.CodeTextArea.insert(INSERT, output)

    def setOutputText(self, output):
        self.OutputTextArea.insert(INSERT, cadena)


IDE = Gui()
