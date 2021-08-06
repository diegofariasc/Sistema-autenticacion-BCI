from View           import View
from ViewAuxiliar   import ViewAuxiliar
from PIL            import ImageTk, Image

import tkinter as Tkinter

# La clase representa la vista principal
class ViewRecopilador(View):

    # Constructor de objetos de la clase
    def construirView(self):

        # Llamada al constructor de la superclase
        super().construirView()

        # Configurar el fondo y la etiqueta del programa
        self.canvas.config(
            bg=View.COLOR_CONTRASTE
        ) # End config
        self.etiquetaPrograma.config(
            bg=View.COLOR_CONTRASTE,
            fg=ViewAuxiliar.obtenerColor(120,120,120)
        ) # End config

        # Imagen descriptiva
        self.imagenMovimientoMano = Image.open("assets/ViewRecopilador/mano.png")
        self.renderImagenMovimientoMano = ImageTk.PhotoImage(self.imagenMovimientoMano, master=self.ventana)
        self.imagenMovimientoPie = Image.open("assets/ViewRecopilador/pie.png")
        self.renderImagenMovimientoPie = ImageTk.PhotoImage(self.imagenMovimientoPie, master=self.ventana)
        self.imagenMovimientoReposo = Image.open("assets/ViewRecopilador/reposo.png")
        self.renderImagenMovimientoReposo = ImageTk.PhotoImage(self.imagenMovimientoReposo, master=self.ventana)
        self.imagenMovimientoAtencion = Image.open("assets/ViewRecopilador/atencion.png")
        self.renderImagenMovimientoAtencion = ImageTk.PhotoImage(self.imagenMovimientoAtencion, master=self.ventana)
        self.imagenMovimientoFinalizado = Image.open("assets/ViewRecopilador/finalizado.png")
        self.renderImagenMovimientoFinalizado = ImageTk.PhotoImage(self.imagenMovimientoFinalizado, master=self.ventana)

        self.etiquetaImagenMovimiento = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE
        ) # End label

        self.etiquetaImagenMovimiento.place(x= (self.LARGO - 100) / 2, y= 100, height=100, width=100)

        # Imagen derecha
        self.imagenDerecha = Image.open("assets/ViewRecopilador/derecha.png")
        self.renderImagenDerecha = ImageTk.PhotoImage(self.imagenDerecha, master=self.ventana)

        self.etiquetaImagenDerecha = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            image=self.renderImagenDerecha
        ) # End label

        # Imagen izquierda
        self.imagenIzquierda = Image.open("assets/ViewRecopilador/izquierda.png")
        self.renderImagenIzquierda = ImageTk.PhotoImage(self.imagenIzquierda, master=self.ventana)

        self.etiquetaImagenIzquierda = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            image=self.renderImagenIzquierda
        ) # End label

        self.etiquetaDescripcionMovimiento = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            fg=ViewAuxiliar.obtenerColor(241,196,15),
            text="",
            font="SegoeUI 19 bold",
            cursor='hand2'
        ) # End label

        self.etiquetaDescripcionMovimiento.place(x=0, y= 220, height=24, width=self.LARGO)

    def establecerListeners( self, controller ):
        pass
        