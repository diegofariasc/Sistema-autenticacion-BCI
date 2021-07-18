
from ViewAuxiliar import ViewAuxiliar
import tkinter as Tkinter
import abc

# La clase representa cualquier vista
class View(metaclass=abc.ABCMeta):

    # Variables para inicializacion
    LARGO = 550
    ALTO = 410
    COLOR_FONDO = ViewAuxiliar.obtenerColor(243,242,242)
    COLOR_CONTRASTE = ViewAuxiliar.obtenerColor(64,64,64)
    COLOR_TEXTO_PANEL = ViewAuxiliar.obtenerColor(220,220,220)
    COLOR_SELECTOR = ViewAuxiliar.obtenerColor(225,225,225)

    # Constructor
    def construirView(self):
        
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
        self.ventana.resizable(False, False)

        tamanoPantallaX =self.ventana.winfo_screenwidth()
        tamanoPantallaY =self.ventana.winfo_screenheight()
        posicionVentanaX = (tamanoPantallaX-View.LARGO)/2
        posicionVentanaY = (tamanoPantallaY-View.ALTO)/2 -View.ALTO * 0.2

        # Parametros generales de la ventana
        self.ventana.geometry('%dx%d+%d+%d' % (View.LARGO, View.ALTO,posicionVentanaX,posicionVentanaY))
        self.ventana.title("Sistema de autenticación")

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

    @abc.abstractmethod
    def establecerListeners( self, controller ):
        # Metodo para relacionar el controller con el view
        return
