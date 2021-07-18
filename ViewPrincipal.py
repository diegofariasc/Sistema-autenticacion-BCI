from ViewAuxiliar   import ViewAuxiliar
from ViewPanel      import ViewPanel
from View           import View
from PIL            import ImageTk, Image

import tkinter as Tkinter

# La clase representa la vista principal
class ViewPrincipal(ViewPanel):

    # Constructor de objetos de la clase
    def construirView(self):

        # Llamada al constructor de la superclase
        super().construirView()

        # Crear cada elemento del panel

        # Boton para crear un usuario
        self.imagenNuevoUsuario = Image.open("assets/ViewPrincipal/nuevoUsuario.png")
        self.renderNuevoUsuario= ImageTk.PhotoImage(self.imagenNuevoUsuario, master=self.ventana)

        self.etiquetaImagenNuevoUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            image=self.renderNuevoUsuario,
            cursor='hand2'
        ) # End label

        self.etiquetaImagenNuevoUsuario.pack()
        self.etiquetaImagenNuevoUsuario.place(x=25, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de crear usuario
        self.etiquetaDescripcionNuevoUsuario = Tkinter.Label( 
            self.canvas, 
            text='Nuevo usuario',
            bg=View.COLOR_CONTRASTE,
            fg=View.COLOR_TEXTO_PANEL,
            font="SegoeUI 11 normal"
        ) # End label
        self.etiquetaDescripcionNuevoUsuario.pack()
        self.etiquetaDescripcionNuevoUsuario.place(x=10, y=70, height=20, width=75)


        # Boton para abortar inicio
        self.imagenAbortarInicio = Image.open("assets/ViewPrincipal/abortarInicio.png")
        self.renderAbortarInicio = ImageTk.PhotoImage(self.imagenAbortarInicio, master=self.ventana)

        self.etiquetaImagenAbortarInicio = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            image=self.renderAbortarInicio,
            cursor='hand2'
        ) # End label

        self.etiquetaImagenAbortarInicio.pack()
        self.etiquetaImagenAbortarInicio.place(x=25, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de crear usuario
        self.etiquetaDescripcionAbortarInicio = Tkinter.Label( 
            self.canvas, 
            text='Abortar inicio',
            bg=View.COLOR_CONTRASTE,
            fg=View.COLOR_TEXTO_PANEL,
            font="SegoeUI 11 normal"
        ) # End label
        self.etiquetaDescripcionAbortarInicio.pack()
        self.etiquetaDescripcionAbortarInicio.place(x=10, y=70, height=20, width=75)


        # Etiqueta descriptiva de la labor en la ventana
        self.etiquetaDescripcionVentana= Tkinter.Label( 
            self.canvas, 
            text='Seleccionar un usuario para acceder',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 13 normal"
        ) # End label
        self.etiquetaDescripcionVentana.pack()
        self.etiquetaDescripcionVentana.place(x=0, y=110, height=20, width=View.LARGO)

        # Imagen de usuario
        self.etiquetaImagenUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO
        ) # End label

        self.etiquetaImagenUsuario.pack()
        self.etiquetaImagenUsuario.place(x=0, y=138, height=150, width=View.LARGO)

        # Imagen de moverse a la derecha
        self.imagenDerecha = Image.open("assets/ViewPrincipal/moverseDerecha.png")
        self.renderDerecha = ImageTk.PhotoImage(self.imagenDerecha, master=self.ventana)
        self.imagenDerechaDesactivado = Image.open("assets/ViewPrincipal/moverseDerechaDesactivado.png")
        self.renderDerechaDesactivado = ImageTk.PhotoImage(self.imagenDerechaDesactivado, master=self.ventana)

        self.etiquetaImagenDerecha = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderDerecha,
            cursor='hand2'
        ) # End label
        self.etiquetaImagenDerecha.place(x=370, y=178, height=70, width=70)

        # Imagen de moverse a la izquierda
        self.imagenIzquierda = Image.open("assets/ViewPrincipal/moverseIzquierda.png")
        self.renderIzquierda = ImageTk.PhotoImage(self.imagenIzquierda, master=self.ventana)
        self.imagenIzquierdaDesactivado = Image.open("assets/ViewPrincipal/moverseIzquierdaDesactivado.png")
        self.renderIzquierdaDesactivado = ImageTk.PhotoImage(self.imagenIzquierdaDesactivado, master=self.ventana)

        self.etiquetaImagenIzquierda = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderIzquierda,
            cursor='hand2'
        ) # End label
        self.etiquetaImagenIzquierda.place(x=110, y=178, height=70, width=70)

        # Etiqueta con el nombre del usuario
        self.etiquetaNombreUsuario= Tkinter.Label( 
            self.canvas, 
            text='Nombre del usuario',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 16 normal"
        ) # End label
        self.etiquetaNombreUsuario.place(x=0, y=300, height=20, width=View.LARGO)

        # Etiqueta con la fecha de registro
        self.etiquetaFechaRegistro = Tkinter.Label( 
            self.canvas, 
            text='Registrado el 01 de enero de 2021',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(94,94,94),
            font="SegoeUI 12 normal"
        ) # End label
        self.etiquetaFechaRegistro.pack()
        self.etiquetaFechaRegistro.place(x=0, y=320, height=20, width=View.LARGO)

        # Boton de escaneo EEG
        self.imagenEscaneoEEG = Image.open("assets/ViewPrincipal/escaneoEEG.png")
        self.renderEscaneoEEG  = ImageTk.PhotoImage(self.imagenEscaneoEEG, master=self.ventana)
        self.botonEscaneoEEG = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Usar escaneo EEG", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=self.renderEscaneoEEG,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button

        self.botonEscaneoEEG.pack()
        self.botonEscaneoEEG.place(x=135, y=345, height=28, width=135)

        # Boton de contrasena
        self.imagenContrasena = Image.open("assets/ViewPrincipal/contrasena.png")
        self.renderContrasena  = ImageTk.PhotoImage(self.imagenContrasena, master=self.ventana)
        self.botonContrasena = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Usar contraseña", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=self.renderContrasena,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button

        self.botonContrasena.pack()
        self.botonContrasena.place(x=280, y=345, height=28, width=135)

        # Campo contrasena
        self.campoContrasena = Tkinter.Entry(
            self.canvas, 
            width = 17,
            highlightbackground=View.COLOR_FONDO,
            font="SegoeUI 11 italic",
            fg=ViewAuxiliar.obtenerColor(124,124,124)
        ) # End entry
        self.campoContrasena.insert(0, 'Contraseña')
        
        # Boton para ingresar con contrasena
        self.imagenIngresar = Image.open("assets/ViewPrincipal/ingresar.png")
        self.renderIngresar = ImageTk.PhotoImage(self.imagenIngresar, master=self.ventana)

        self.etiquetaImagenIngresar = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderIngresar,
            cursor='hand2'
        ) # End label

        # Boton para ingresar volver a la seleccion de metodo de ingreso
        self.imagenVolverMetodoIngreso = Image.open("assets/ViewPrincipal/regresarMetodoIngreso.png")
        self.renderVolverMetodoIngreso = ImageTk.PhotoImage(self.imagenVolverMetodoIngreso, master=self.ventana)

        self.etiquetaVolverMetodoIngreso = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderVolverMetodoIngreso,
            cursor='hand2'
        ) # End label



    def establecerListeners( self, controller ):
        self.etiquetaImagenNuevoUsuario.bind("<Button-1>", controller.etiquetaImagenNuevoUsuario_Click)
        self.etiquetaImagenDerecha.bind("<Button-1>", controller.etiquetaImagenDerecha_Click)
        self.etiquetaImagenIzquierda.bind("<Button-1>", controller.etiquetaImagenIzquierda_Click)
        self.etiquetaImagenAbortarInicio.bind("<Button-1>", controller.etiquetaImagenAbortarInicio_Click)
        self.botonContrasena.bind("<Button-1>", controller.botonContrasena_Click)
        self.campoContrasena.bind("<FocusIn>", controller.campoContrasena_Focus)
        self.campoContrasena.bind("<FocusOut>", controller.campoContrasena_LostFocus)
        self.etiquetaVolverMetodoIngreso.bind("<Button-1>", controller.etiquetaVolverMetodoIngreso_Click)
        self.etiquetaImagenIngresar.bind("<Button-1>", controller.etiquetaImagenIngresar_Click)
        