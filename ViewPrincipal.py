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

        # Ciclo principal
        self.__ventana.mainloop()


# Llamada al metodo principal
interfaz = ViewPrincipal()
interfaz.construir()