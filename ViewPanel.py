


import tkinter as Tkinter
from View import View       

# La clase representa una vista con panel superior
class ViewPanel(View):

    def construirView(self):

        # Llamada al constructor de la superclase
        super().construirView()

        # Crear panel superior
        self.canvas.create_rectangle( 
            View.LARGO, 95, 0, 0, 
            fill=View.COLOR_CONTRASTE, 
            outline=View.COLOR_CONTRASTE
        ) # End create_rectangle

        # Etiqueta de titulo de la ventana
        etiquetaTitulo = Tkinter.Label( 
            self.canvas, 
            text='Sistema de autenticación basado en BCI',
            bg=View.COLOR_CONTRASTE,
            fg=View.COLOR_TEXTO_PANEL,
            anchor='w',
            font="SegoeUI 12 normal"
        ) # End label
        etiquetaTitulo.pack()
        etiquetaTitulo.place(x=10, y=3, height=20, width=300)