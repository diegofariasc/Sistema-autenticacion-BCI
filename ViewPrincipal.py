import tkinter as Tkinter
from ViewAuxiliar import ViewAuxiliar
from PIL import ImageTk, Image

# La clase representa la vista principal
class ViewPrincipal():

    # Constructor de objetos de la clase
    def __init__(self):

        # Variables para inicializacion
        largo = 550
        alto = 410
        colorFondo = ViewAuxiliar.obtenerColor(243,242,242)
        colorContraste = ViewAuxiliar.obtenerColor(64,64,64)
        colorTextoPanel = ViewAuxiliar.obtenerColor(220,220,220)

        # Crear ventana y su canvas
        self.__ventana = Tkinter.Tk()
        self.__canvas = Tkinter.Canvas( 
            self.__ventana, 
            width=largo, 
            height=alto,
            bg=colorFondo, 
            highlightthickness=0
        ) # End canvas
        self.__canvas.pack()

        # Parametros generales de la ventana
        self.__ventana.geometry("%sx%s" % (largo, alto))
        self.__ventana.title("Sistema de autenticación")

        # Crear panel superior
        self.__canvas.create_rectangle( 
            largo, 95, 0, 0, 
            fill=colorContraste, 
            outline=colorContraste
        ) # End create_rectangle

        etiquetaTitulo = Tkinter.Label( 
            self.__canvas, 
            text='Sistema de autenticación basado en BCI',
            bg=colorContraste,
            fg=colorTextoPanel,
            anchor='w',
            font="SegoeUI 12 normal"
        ) # End label
        
        etiquetaTitulo.pack()
        etiquetaTitulo.place(x=10, y=3, height=20, width=300)

        # Crear cada elemento del panel

        # Boton para crear un usuario
        imagenNuevoUsuario = Image.open("assets/ViewPrincipal/nuevoUsuario.png")
        renderNuevoUsuario= ImageTk.PhotoImage(imagenNuevoUsuario)

        etiquetaImagenNuevoUsuario = Tkinter.Label( 
            self.__canvas, 
            bg=colorContraste,
            image=renderNuevoUsuario,
            cursor='hand2'
        ) # End label

        etiquetaImagenNuevoUsuario.pack()
        etiquetaImagenNuevoUsuario.place(x=25, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de crear usuario
        etiquetaDescripcionNuevoUsuario = Tkinter.Label( 
            self.__canvas, 
            text='Nuevo usuario',
            bg=colorContraste,
            fg=colorTextoPanel,
            font="SegoeUI 11 normal"
        ) # End label
        etiquetaDescripcionNuevoUsuario.pack()
        etiquetaDescripcionNuevoUsuario.place(x=10, y=70, height=20, width=75)

        # Boton para eliminar un usuario
        imagenEliminarUsuario = Image.open("assets/ViewPrincipal/eliminarUsuario.png")
        renderEliminarUsuario= ImageTk.PhotoImage(imagenEliminarUsuario)

        etiquetaImagenEliminarUsuario = Tkinter.Label( 
            self.__canvas, 
            bg=colorContraste,
            image=renderEliminarUsuario,
            cursor='hand2'
        ) # End label

        etiquetaImagenEliminarUsuario.pack()
        etiquetaImagenEliminarUsuario.place(x=110, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de eliminar usuario
        etiquetaDescripcionEliminarUsuario = Tkinter.Label( 
            self.__canvas, 
            text='Eliminar perfil',
            bg=colorContraste,
            fg=colorTextoPanel,
            font="SegoeUI 11 normal"
        ) # End label
        etiquetaDescripcionEliminarUsuario.pack()
        etiquetaDescripcionEliminarUsuario.place(x=95, y=70, height=20, width=75)

        # Boton para configurar un usuario
        imagenConfigurar = Image.open("assets/ViewPrincipal/configurar.png")
        renderConfigurar= ImageTk.PhotoImage(imagenConfigurar)

        etiquetaImagenConfigurar = Tkinter.Label( 
            self.__canvas, 
            bg=colorContraste,
            image=renderConfigurar,
            cursor='hand2'
        ) # End label

        etiquetaImagenConfigurar.pack()
        etiquetaImagenConfigurar.place(x=195, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de configurar usuario
        etiquetaDescripcionConfigurar = Tkinter.Label( 
            self.__canvas, 
            text='Configuración',
            bg=colorContraste,
            fg=colorTextoPanel,
            font="SegoeUI 11 normal"
        ) # End label
        etiquetaDescripcionConfigurar.pack()
        etiquetaDescripcionConfigurar.place(x=180, y=70, height=20, width=75)

        # Etiqueta descriptiva de la labor en la ventana
        etiquetaDescripcionVentana= Tkinter.Label( 
            self.__canvas, 
            text='Seleccionar un usuario para acceder',
            bg=colorFondo,
            fg=colorContraste,
            font="SegoeUI 13 normal"
        ) # End label
        etiquetaDescripcionVentana.pack()
        etiquetaDescripcionVentana.place(x=0, y=110, height=20, width=largo)

        # Recorte temporal
        ViewAuxiliar.recortarImagenUsuario("assets/ViewPrincipal/imagenUsuarioDefault.jpg")

        # Imagen de usuario
        imagenUsuario = Image.open("recortada.png")   # Reemplazar con BD
        imagenUsuario = imagenUsuario.resize((150,150))
        renderUsuario = ImageTk.PhotoImage(imagenUsuario)

        etiquetaImagenUsuario = Tkinter.Label( 
            self.__canvas, 
            bg=colorFondo,
            image=renderUsuario,
        ) # End label

        etiquetaImagenUsuario.pack()
        etiquetaImagenUsuario.place(x=0, y=138, height=150, width=largo)

        # Imagen de moverse a la derecha
        imagenDerecha = Image.open("assets/ViewPrincipal/moverseDerecha.png")
        renderDerecha = ImageTk.PhotoImage(imagenDerecha)

        etiquetaImagenDerecha = Tkinter.Label( 
            self.__canvas, 
            bg=colorFondo,
            image=renderDerecha,
            cursor='hand2'
        ) # End label

        etiquetaImagenDerecha.pack()
        etiquetaImagenDerecha.place(x=370, y=178, height=70, width=70)

        # Imagen de moverse a la izquierda
        imagenIzquierda = Image.open("assets/ViewPrincipal/moverseIzquierda.png")
        renderIzquierda = ImageTk.PhotoImage(imagenIzquierda)

        etiquetaImagenIzquierda = Tkinter.Label( 
            self.__canvas, 
            bg=colorFondo,
            image=renderIzquierda,
            cursor='hand2'
        ) # End label

        etiquetaImagenIzquierda.pack()
        etiquetaImagenIzquierda.place(x=110, y=178, height=70, width=70)

        # Etiqueta con el nombre del usuario
        etiquetaNombreUsuario= Tkinter.Label( 
            self.__canvas, 
            text='Nombre del usuario',
            bg=colorFondo,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 16 normal"
        ) # End label
        etiquetaNombreUsuario.pack()
        etiquetaNombreUsuario.place(x=0, y=300, height=20, width=largo)

        # Etiqueta con el nombre del usuario
        etiquetaNombreUsuario= Tkinter.Label( 
            self.__canvas, 
            text='Registrado el 01 de enero de 2021',
            bg=colorFondo,
            fg=ViewAuxiliar.obtenerColor(94,94,94),
            font="SegoeUI 12 normal"
        ) # End label
        etiquetaNombreUsuario.pack()
        etiquetaNombreUsuario.place(x=0, y=320, height=20, width=largo)

        # Boton de escaneo EEG
        imagenEscaneoEEG = Image.open("assets/ViewPrincipal/escaneoEEG.png")
        renderEscaneoEEG  = ImageTk.PhotoImage(imagenEscaneoEEG)
        botonEscaneoEEG = Tkinter.Button( 
            self.__canvas, 
            fg=colorContraste, 
            text ="Usar escaneo EEG", 
            font="SegoeUI 11 normal",
            highlightbackground=colorFondo,
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
            self.__canvas, 
            fg=colorContraste, 
            text ="Usar contraseña", 
            font="SegoeUI 11 normal",
            highlightbackground=colorFondo,
            image=renderContrasena,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button

        botonContrasena.pack()
        botonContrasena.place(x=280, y=345, height=28, width=135)

        # Etiqueta del programa
        etiquetaPrograma= Tkinter.Label( 
            self.__canvas, 
            text='Programa de honores. Universidad de las Américas Puebla',
            bg=colorFondo,
            fg=ViewAuxiliar.obtenerColor(134,134,134),
            font="SegoeUI 9 italic",
            anchor='w'
        ) # End label
        etiquetaPrograma.pack()
        etiquetaPrograma.place(x=10, y=390, height=20, width=largo)

        # Ciclo principal
        self.__ventana.mainloop()

# Llamada al metodo principal
interfaz = ViewPrincipal()
