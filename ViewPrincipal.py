import tkinter as Tkinter
from ViewAuxiliar import ViewAuxiliar
from PIL import ImageTk, Image 

# La clase representa la vista principal
class ViewPrincipal():

    # Constructor de objetos de la clase
    def __init__(self):

        # Variables para inicializacion
        largo = 700
        alto = 500
        colorFondo = ViewAuxiliar.obtenerColor(243,242,242)
        colorContraste = ViewAuxiliar.obtenerColor(64,64,64)

        # Crear ventana y su canvas
        self.__ventana = Tkinter.Tk()
        self.__canvas = Tkinter.Canvas( self.__ventana, 
                                        width=largo, 
                                        height=alto,
                                        bg=colorFondo, 
                                        highlightthickness=0)
        self.__canvas.pack()

        # Parametros generales de la ventana
        self.__ventana.geometry("%sx%s" % (largo, alto))
        self.__ventana.title("Sistema de autenticación")

        # Crear panel superior
        self.__canvas.create_rectangle( largo, 100, 0, 0, 
                                        fill=colorContraste, 
                                        outline=colorContraste)

        etiquetaTitulo = Tkinter.Label( self.__canvas, 
                                        text='Sistema de autenticación basado en BCI',
                                        bg=colorContraste,
                                        fg=ViewAuxiliar.obtenerColor(220,220,220),
                                        anchor='w',
                                        font="SegoeUI 12 normal")
        etiquetaTitulo.pack()
        etiquetaTitulo.place(x=8, y=3, height=20, width=300)

        # Ciclo principal
        self.__ventana.mainloop()


# Llamada al metodo principal
interfaz = ViewPrincipal()
interfaz.construir()