import tkinter as Tkinter
from ViewAuxiliar import ViewAuxiliar
from ViewPanel import ViewPanel
from View import View
from PIL import ImageTk, Image

# La clase representa la vista cuando el usuario ha accedido
class ViewIniciado(ViewPanel):

    def __init__(self):

        # Llamada al constructor de la superclase
        super().__init__()

        # Crear cada elemento del panel

        # Boton para eliminar un usuario
        imagenEliminarUsuario = Image.open("assets/ViewPrincipal/eliminarUsuario.png")
        renderEliminarUsuario= ImageTk.PhotoImage(imagenEliminarUsuario)
        etiquetaImagenEliminarUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            image=renderEliminarUsuario,
            cursor='hand2'
        ) # End label
        etiquetaImagenEliminarUsuario.pack()
        etiquetaImagenEliminarUsuario.place(x=25, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de eliminar usuario
        etiquetaDescripcionEliminarUsuario = Tkinter.Label( 
            self.canvas, 
            text='Eliminar perfil',
            bg=View.COLOR_CONTRASTE,
            fg=View.COLOR_TEXTO_PANEL,
            font="SegoeUI 11 normal"
        ) # End label
        etiquetaDescripcionEliminarUsuario.pack()
        etiquetaDescripcionEliminarUsuario.place(x=10, y=70, height=20, width=75)

        # Imagen de usuario
        imagenUsuario = Image.open("recortada.png")   # Reemplazar con BD
        imagenUsuario = imagenUsuario.resize((60,60))
        renderUsuario = ImageTk.PhotoImage(imagenUsuario)
        etiquetaImagenUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderUsuario,
        ) # End label
        etiquetaImagenUsuario.pack()
        etiquetaImagenUsuario.place(x=10, y=105, height=60, width=60)

        # Etiqueta con el nombre del usuario
        etiquetaNombreUsuario= Tkinter.Label( 
            self.canvas, 
            text='Nombre del usuario',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 16 normal",
            anchor='w'
        ) # End label
        etiquetaNombreUsuario.pack()
        etiquetaNombreUsuario.place(x=80, y=107, height=20, width=View.LARGO)

        # Etiqueta con la fecha de registro del usuario
        etiquetaRegistro= Tkinter.Label( 
            self.canvas, 
            text='Registrado el 01 de enero de 2021',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(94,94,94),
            font="SegoeUI 12 normal",
            anchor='w'
        ) # End label
        etiquetaRegistro.pack()
        etiquetaRegistro.place(x=80, y=127, height=20, width=View.LARGO)

        # Imagen de muestras
        imagenMuestras = Image.open("assets/ViewIniciado/muestras.png")
        renderMuestras= ImageTk.PhotoImage(imagenMuestras)
        etiquetaImagenMuestras = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderMuestras
        ) # End label
        etiquetaImagenMuestras.pack()
        etiquetaImagenMuestras.place(x=80, y=148, height=16, width=16)

        # Etiqueta con el numero de muestras disponibles
        etiquetaMuestras= Tkinter.Label( 
            self.canvas, 
            text='Muestras disponibles: 0',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(124,124,124),
            font="SegoeUI 12 normal",
            anchor='w'
        ) # End label
        etiquetaMuestras.pack()
        etiquetaMuestras.place(x=106, y=149, height=16, width=200)

        # Imagen de calidad
        imagenCalidad = Image.open("assets/ViewIniciado/calidad.png")
        renderCalidad = ImageTk.PhotoImage(imagenCalidad)
        etiquetaImagenCalidad = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderCalidad
        ) # End label
        etiquetaImagenCalidad.pack()
        etiquetaImagenCalidad.place(x=270, y=148, height=16, width=16)

        # Etiqueta con la calidad se la senal
        etiquetaCalidad= Tkinter.Label( 
            self.canvas, 
            text='Calidad de señales: 100.0%',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(124,124,124),
            font="SegoeUI 12 normal",
            anchor='w'
        ) # End label
        etiquetaCalidad.pack()
        etiquetaCalidad.place(x=293, y=149, height=16, width=200)

        # Etiqueta descriptiva de los niveles de seguridad 
        etiquetaDescripcionNiveles= Tkinter.Label( 
            self.canvas, 
            text='Niveles de seguridad del sistema:',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 13 normal"
        ) # End label
        etiquetaDescripcionNiveles.pack()
        etiquetaDescripcionNiveles.place(x=0, y=180, height=20, width=View.LARGO)

        # Imagen de seguridad baja
        imagenSeguridadBaja = Image.open("assets/ViewIniciado/seguridadBaja.png")
        renderSeguridadBaja = ImageTk.PhotoImage(imagenSeguridadBaja)
        etiquetaImagenSeguridadBaja = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderSeguridadBaja,
            cursor='hand2'
        ) # End label
        etiquetaImagenSeguridadBaja.pack()
        etiquetaImagenSeguridadBaja.place(x=80, y=220, height=90, width=120)

        # Imagen de seguridad media
        imagenSeguridadMedia = Image.open("assets/ViewIniciado/seguridadMedia.png")
        renderSeguridadMedia = ImageTk.PhotoImage(imagenSeguridadMedia)
        etiquetaImagenSeguridadMedia = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_SELECTOR,
            image=renderSeguridadMedia,
            cursor='hand2'
        ) # End label
        etiquetaImagenSeguridadMedia.pack()
        etiquetaImagenSeguridadMedia.place(x=220, y=220, height=90, width=120)

        # Imagen de seguridad alta
        imagenSeguridadAlta = Image.open("assets/ViewIniciado/seguridadAlta.png")
        renderSeguridadAlta = ImageTk.PhotoImage(imagenSeguridadAlta)
        etiquetaImagenSeguridadAlta = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderSeguridadAlta,
            cursor='hand2'
        ) # End label
        etiquetaImagenSeguridadAlta.pack()
        etiquetaImagenSeguridadAlta.place(x=360, y=224, height=90, width=120)

        # Etiqueta de titulo seguridad baja
        etiquetaTituloSeguridadBaja = Tkinter.Label( 
            self.canvas, 
            text='Reducido',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 14 normal",
            cursor='hand2'
        ) # End label
        etiquetaTituloSeguridadBaja.pack()
        etiquetaTituloSeguridadBaja.place(x=80, y=312, height=20, width=120)

        # Etiqueta de titulo seguridad media
        etiquetaTituloSeguridadMedia = Tkinter.Label( 
            self.canvas, 
            text='Intermedio*',
            bg=View.COLOR_SELECTOR,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 14 normal",
            cursor='hand2'
        ) # End label
        etiquetaTituloSeguridadMedia.pack()
        etiquetaTituloSeguridadMedia.place(x=220, y=312, height=20, width=120)

        # Etiqueta de titulo seguridad alta
        etiquetaTituloSeguridadAlta= Tkinter.Label( 
            self.canvas, 
            text='Máximo',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 14 normal",
            cursor='hand2'
        ) # End label
        etiquetaTituloSeguridadAlta.pack()
        etiquetaTituloSeguridadAlta.place(x=360, y=312, height=20, width=120)

        # Etiqueta de descripcion seguridad baja
        etiquetaDescripcionSeguridadBaja = Tkinter.Label( 
            self.canvas, 
            text='Acceso al aprobar 1/5\n experimentos',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(104,104,104),
            font="SegoeUI 10 normal",
            cursor='hand2'
        ) # End label
        etiquetaDescripcionSeguridadBaja.pack()
        etiquetaDescripcionSeguridadBaja.place(x=80, y=335, height=20, width=120)

        # Etiqueta de descripcion seguridad media
        etiquetaDescripcionSeguridadMedia = Tkinter.Label( 
            self.canvas, 
            text='Acceso al aprobar 3/5\n experimentos',
            bg=View.COLOR_SELECTOR,
            fg=ViewAuxiliar.obtenerColor(104,104,104),
            font="SegoeUI 10 normal",
            cursor='hand2'
        ) # End label
        etiquetaDescripcionSeguridadMedia.pack()
        etiquetaDescripcionSeguridadMedia.place(x=220, y=335, height=20, width=120)

        # Etiqueta de descripcion seguridad alta
        etiquetaDescripcionSeguridadAlta = Tkinter.Label( 
            self.canvas, 
            text='Acceso al aprobar 5/5\n experimentos',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(104,104,104),
            font="SegoeUI 10 normal",
            cursor='hand2'
        ) # End label
        etiquetaDescripcionSeguridadAlta.pack()
        etiquetaDescripcionSeguridadAlta.place(x=360, y=335, height=20, width=120)

        # Etiqueta del programa
        etiquetaPrograma= Tkinter.Label( 
            self.canvas, 
            text='Programa de honores. Universidad de las Américas Puebla' +
            '           * Configuración recomendada',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(134,134,134),
            font="SegoeUI 9 italic",
            anchor='w'
        ) # End label
        etiquetaPrograma.pack()
        etiquetaPrograma.place(x=10, y=390, height=20, width=View.LARGO)

        # Crear panel para mostrar seleccion de nivel de seguridad
        self.selector = self.canvas.create_rectangle( 
            215, 215, 345, 360, 
            fill=View.COLOR_SELECTOR, 
            outline=View.COLOR_SELECTOR
        ) # End create_rectangle
        self.canvas.tag_raise(self.selector)

        # Ciclo principal
        self.ventana.mainloop()