from tkinter import *
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from lexer import lexicalAnalizer



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
        self.OptionBar = Canvas(self.MainWindow, width=1003, height=25, bg="#BDBDBD").place(x=-3, y=-3)

        # Buttons
        Button(self.OptionBar, text="ABRIR", command=self.OpenButtonClick).place(x=5, y=1)
        Button(self.OptionBar, text="GUARDAR", command=self.SaveButtonClick).place(x=70, y=1)
        Button(self.OptionBar, text="COMPILAR", command=self.compileButtonClick).place(x=160, y=1)
        Button(self.OptionBar, text="SALIR", command=lambda: self.MainWindow.destroy()).place(x=945, y=1)

        # Inserta las dos areas de texto

        self.CodeTextArea = Text(self.MainWindow, bg='#E0F8F1')
        self.CodeTextArea.place(x=10, y=30, width=980, height=500)

        self.OutputTextArea = Text(self.MainWindow, bg='#E0F8F1')
        self.OutputTextArea.place(x=10, y=535, width=980, height=260)

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
        print(cadena)
        lexicalAnalizer(cadena)



    def setCodeTextArea(self, output):
        self.CodeTextArea.delete('1.0', END)
        self.CodeTextArea.insert(INSERT, output)

    def setOutputText(self, output):
        self.OutputTextArea.insert(END, output)


IDE = Gui()
