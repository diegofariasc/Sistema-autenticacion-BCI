
from ViewAuxiliar import ViewAuxiliar
import tkinter as Tkinter

# La clase representa cualquier vista
class View():

    # Variables para inicializacion
    LARGO = 550
    ALTO = 410
    COLOR_FONDO = ViewAuxiliar.obtenerColor(243,242,242)
    COLOR_CONTRASTE = ViewAuxiliar.obtenerColor(64,64,64)
    COLOR_TEXTO_PANEL = ViewAuxiliar.obtenerColor(220,220,220)
    COLOR_SELECTOR = ViewAuxiliar.obtenerColor(225,225,225)

    # Constructor
    def __init__(self):
        
        # Crear ventana y su canvas
        self.ventana = Tkinter.Tk()
        self.canvas = Tkinter.Canvas( 
            self.ventana, 
            width=View.LARGO, 
            height=View.ALTO,
            bg=View.COLOR_FONDO, 
            highlightthickness=0
        ) # End canvas
        self.canvas.pack()

        # Parametros generales de la ventana
        self.ventana.geometry("%sx%s" % (View.LARGO, View.ALTO))
        self.ventana.title("Sistema de autenticación - Nombre del usuario")

         # Etiqueta del programa
        self.etiquetaPrograma= Tkinter.Label( 
            self.canvas, 
            text='Programa de honores. Universidad de las Américas Puebla',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(134,134,134),
            font="SegoeUI 9 italic",
            anchor='w'
        ) # End label
        self.etiquetaPrograma.pack()
        self.etiquetaPrograma.place(x=10, y=390, height=20, width=View.LARGO)



