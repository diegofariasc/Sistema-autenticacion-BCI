import tkinter as Tkinter
from ViewAuxiliar import ViewAuxiliar
from ViewPanel import ViewPanel
from View import View
from PIL import ImageTk, Image

# La clase representa la vista principal
class ViewPrincipal(ViewPanel):

    # Constructor de objetos de la clase
    def __init__(self):

        # Llamada al constructor de la superclase
        super().__init__()

        # Crear cada elemento del panel

        # Boton para crear un usuario
        imagenNuevoUsuario = Image.open("assets/ViewPrincipal/nuevoUsuario.png")
        renderNuevoUsuario= ImageTk.PhotoImage(imagenNuevoUsuario)

        etiquetaImagenNuevoUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            image=renderNuevoUsuario,
            cursor='hand2'
        ) # End label

        etiquetaImagenNuevoUsuario.pack()
        etiquetaImagenNuevoUsuario.place(x=25, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de crear usuario
        etiquetaDescripcionNuevoUsuario = Tkinter.Label( 
            self.canvas, 
            text='Nuevo usuario',
            bg=View.COLOR_CONTRASTE,
            fg=View.COLOR_TEXTO_PANEL,
            font="SegoeUI 11 normal"
        ) # End label
        etiquetaDescripcionNuevoUsuario.pack()
        etiquetaDescripcionNuevoUsuario.place(x=10, y=70, height=20, width=75)

        # Etiqueta descriptiva de la labor en la ventana
        etiquetaDescripcionVentana= Tkinter.Label( 
            self.canvas, 
            text='Seleccionar un usuario para acceder',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 13 normal"
        ) # End label
        etiquetaDescripcionVentana.pack()
        etiquetaDescripcionVentana.place(x=0, y=110, height=20, width=View.LARGO)

        # Recorte temporal
        ViewAuxiliar.recortarImagenUsuario("assets/ViewPrincipal/imagenUsuarioDefault.jpg")

        # Imagen de usuario
        imagenUsuario = Image.open("recortada.png")   # Reemplazar con BD
        imagenUsuario = imagenUsuario.resize((150,150))
        renderUsuario = ImageTk.PhotoImage(imagenUsuario)

        etiquetaImagenUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderUsuario,
        ) # End label

        etiquetaImagenUsuario.pack()
        etiquetaImagenUsuario.place(x=0, y=138, height=150, width=View.LARGO)

        # Imagen de moverse a la derecha
        imagenDerecha = Image.open("assets/ViewPrincipal/moverseDerecha.png")
        renderDerecha = ImageTk.PhotoImage(imagenDerecha)

        etiquetaImagenDerecha = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderDerecha,
            cursor='hand2'
        ) # End label

        etiquetaImagenDerecha.pack()
        etiquetaImagenDerecha.place(x=370, y=178, height=70, width=70)

        # Imagen de moverse a la izquierda
        imagenIzquierda = Image.open("assets/ViewPrincipal/moverseIzquierda.png")
        renderIzquierda = ImageTk.PhotoImage(imagenIzquierda)

        etiquetaImagenIzquierda = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderIzquierda,
            cursor='hand2'
        ) # End label

        etiquetaImagenIzquierda.pack()
        etiquetaImagenIzquierda.place(x=110, y=178, height=70, width=70)

        # Etiqueta con el nombre del usuario
        etiquetaNombreUsuario= Tkinter.Label( 
            self.canvas, 
            text='Nombre del usuario',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 16 normal"
        ) # End label
        etiquetaNombreUsuario.pack()
        etiquetaNombreUsuario.place(x=0, y=300, height=20, width=View.LARGO)

        # Etiqueta con el nombre del usuario
        etiquetaNombreUsuario= Tkinter.Label( 
            self.canvas, 
            text='Registrado el 01 de enero de 2021',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(94,94,94),
            font="SegoeUI 12 normal"
        ) # End label
        etiquetaNombreUsuario.pack()
        etiquetaNombreUsuario.place(x=0, y=320, height=20, width=View.LARGO)

        # Boton de escaneo EEG
        imagenEscaneoEEG = Image.open("assets/ViewPrincipal/escaneoEEG.png")
        renderEscaneoEEG  = ImageTk.PhotoImage(imagenEscaneoEEG)
        botonEscaneoEEG = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Usar escaneo EEG", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=renderEscaneoEEG,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button

        botonEscaneoEEG.pack()
        botonEscaneoEEG.place(x=135, y=345, height=28, width=135)

        # Boton de contrasena
        imagenContrasena = Image.open("assets/ViewPrincipal/contrasena.png")
        renderContrasena  = ImageTk.PhotoImage(imagenContrasena)
        botonContrasena = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Usar contraseña", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=renderContrasena,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button

        botonContrasena.pack()
        botonContrasena.place(x=280, y=345, height=28, width=135)

        # Ciclo principal
        self.ventana.mainloop()

