import tkinter as Tkinter
from ViewAuxiliar import ViewAuxiliar
from ViewPanel import ViewPanel
from View import View
from PIL import ImageTk, Image

# La clase representa la vista cuando el usuario ha accedido
class ViewIniciado(ViewPanel):

    def construirView(self):

        # Llamada al constructor de la superclase
        super().construirView()

        # Crear cada elemento del panel


        # Boton para cerrar sesion
        self.imagenCerrarSesion = Image.open("assets/ViewIniciado/cerrarSesion.png")
        self.renderCerrarSesion = ImageTk.PhotoImage(self.imagenCerrarSesion, master=self.ventana)
        self.etiquetaImagenCerrarSesion = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            image=self.renderCerrarSesion,
            cursor='hand2'
        ) # End label
        self.etiquetaImagenCerrarSesion.pack()
        self.etiquetaImagenCerrarSesion.place(x=25, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de eliminar usuario
        self.etiquetaDescripcionCerrarSesion = Tkinter.Label( 
            self.canvas, 
            text='Cerrar sesión',
            bg=View.COLOR_CONTRASTE,
            fg=View.COLOR_TEXTO_PANEL,
            font="SegoeUI 11 normal"
        ) # End label
        self.etiquetaDescripcionCerrarSesion.pack()
        self.etiquetaDescripcionCerrarSesion.place(x=10, y=70, height=20, width=75)

        # Boton para eliminar un usuario
        self.imagenEliminarUsuario = Image.open("assets/ViewIniciado/eliminarUsuario.png")
        self.renderEliminarUsuario= ImageTk.PhotoImage(self.imagenEliminarUsuario, master=self.ventana)
        self.etiquetaImagenEliminarUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_CONTRASTE,
            image=self.renderEliminarUsuario,
            cursor='hand2'
        ) # End label
        self.etiquetaImagenEliminarUsuario.pack()
        self.etiquetaImagenEliminarUsuario.place(x=110, y=25, height=45, width=45)

        # Etiqueta correspondiente al boton de eliminar usuario
        self.etiquetaDescripcionEliminarUsuario = Tkinter.Label( 
            self.canvas, 
            text='Eliminar perfil',
            bg=View.COLOR_CONTRASTE,
            fg=View.COLOR_TEXTO_PANEL,
            font="SegoeUI 11 normal"
        ) # End label
        self.etiquetaDescripcionEliminarUsuario.pack()
        self.etiquetaDescripcionEliminarUsuario.place(x=95, y=70, height=20, width=75)


        # Imagen de usuario
        self.imagenUsuario = Image.open("recortada.png")   # Reemplazar con BD
        self.imagenUsuario = self.imagenUsuario.resize((60,60))
        self.renderUsuario = ImageTk.PhotoImage(self.imagenUsuario, master=self.ventana)
        self.etiquetaImagenUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderUsuario,
        ) # End label
        self.etiquetaImagenUsuario.pack()
        self.etiquetaImagenUsuario.place(x=10, y=105, height=60, width=60)

        # Etiqueta con el nombre del usuario
        self.etiquetaNombreUsuario= Tkinter.Label( 
            self.canvas, 
            text='Nombre del usuario',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 16 normal",
            anchor='w'
        ) # End label
        self.etiquetaNombreUsuario.pack()
        self.etiquetaNombreUsuario.place(x=80, y=107, height=20, width=View.LARGO)

        # Etiqueta con la fecha de registro del usuario
        self.etiquetaFechaRegistro= Tkinter.Label( 
            self.canvas, 
            text='Registrado el 01 de enero de 2021',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(94,94,94),
            font="SegoeUI 12 normal",
            anchor='w'
        ) # End label
        self.etiquetaFechaRegistro.pack()
        self.etiquetaFechaRegistro.place(x=80, y=127, height=20, width=View.LARGO)

        # Imagen de muestras
        self.imagenMuestras = Image.open("assets/ViewIniciado/muestras.png")
        self.renderMuestras= ImageTk.PhotoImage(self.imagenMuestras, master=self.ventana)
        self.etiquetaImagenMuestras = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderMuestras
        ) # End label
        self.etiquetaImagenMuestras.pack()
        self.etiquetaImagenMuestras.place(x=80, y=148, height=16, width=16)

        # Etiqueta con el numero de muestras disponibles
        self.etiquetaMuestras= Tkinter.Label( 
            self.canvas, 
            text='Muestras disponibles: 0',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(124,124,124),
            font="SegoeUI 12 normal",
            anchor='w'
        ) # End label
        self.etiquetaMuestras.pack()
        self.etiquetaMuestras.place(x=101, y=147, height=16, width=200)

        # Etiqueta descriptiva de los niveles de seguridad 
        self.etiquetaDescripcionNiveles= Tkinter.Label( 
            self.canvas, 
            text='Niveles de seguridad del sistema:',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 13 normal"
        ) # End label
        self.etiquetaDescripcionNiveles.pack()
        self.etiquetaDescripcionNiveles.place(x=0, y=180, height=20, width=View.LARGO)

        # Imagen de seguridad baja
        self.imagenSeguridadBaja = Image.open("assets/ViewIniciado/seguridadBaja.png")
        self.renderSeguridadBaja = ImageTk.PhotoImage(self.imagenSeguridadBaja, master=self.ventana)
        self.etiquetaImagenSeguridadBaja = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderSeguridadBaja,
            cursor='hand2'
        ) # End label
        self.etiquetaImagenSeguridadBaja.pack()
        self.etiquetaImagenSeguridadBaja.place(x=80, y=220, height=90, width=120)

        # Imagen de seguridad media
        self.imagenSeguridadMedia = Image.open("assets/ViewIniciado/seguridadMedia.png")
        self.renderSeguridadMedia = ImageTk.PhotoImage(self.imagenSeguridadMedia, master=self.ventana)
        self.etiquetaImagenSeguridadMedia = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_SELECTOR,
            image=self.renderSeguridadMedia,
            cursor='hand2'
        ) # End label
        self.etiquetaImagenSeguridadMedia.pack()
        self.etiquetaImagenSeguridadMedia.place(x=220, y=220, height=90, width=120)

        # Imagen de seguridad alta
        self.imagenSeguridadAlta = Image.open("assets/ViewIniciado/seguridadAlta.png")
        self.renderSeguridadAlta = ImageTk.PhotoImage(self.imagenSeguridadAlta, master=self.ventana)
        self.etiquetaImagenSeguridadAlta = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderSeguridadAlta,
            cursor='hand2'
        ) # End label
        self.etiquetaImagenSeguridadAlta.pack()
        self.etiquetaImagenSeguridadAlta.place(x=360, y=224, height=90, width=120)

        # Etiqueta de titulo seguridad baja
        self.etiquetaTituloSeguridadBaja = Tkinter.Label( 
            self.canvas, 
            text='Reducido',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 14 normal",
            cursor='hand2'
        ) # End label
        self.etiquetaTituloSeguridadBaja.pack()
        self.etiquetaTituloSeguridadBaja.place(x=80, y=312, height=20, width=120)

        # Etiqueta de titulo seguridad media
        self.etiquetaTituloSeguridadMedia = Tkinter.Label( 
            self.canvas, 
            text='Intermedio*',
            bg=View.COLOR_SELECTOR,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 14 normal",
            cursor='hand2'
        ) # End label
        self.etiquetaTituloSeguridadMedia.pack()
        self.etiquetaTituloSeguridadMedia.place(x=220, y=312, height=20, width=120)

        # Etiqueta de titulo seguridad alta
        self.etiquetaTituloSeguridadAlta= Tkinter.Label( 
            self.canvas, 
            text='Máximo',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(64,64,64),
            font="SegoeUI 14 normal",
            cursor='hand2'
        ) # End label
        self.etiquetaTituloSeguridadAlta.pack()
        self.etiquetaTituloSeguridadAlta.place(x=360, y=312, height=20, width=120)

        # Etiqueta de descripcion seguridad baja
        self.etiquetaDescripcionSeguridadBaja = Tkinter.Label( 
            self.canvas, 
            text='Acceso al aprobar 1/5\n experimentos',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(104,104,104),
            font="SegoeUI 10 normal",
            cursor='hand2'
        ) # End label
        self.etiquetaDescripcionSeguridadBaja.pack()
        self.etiquetaDescripcionSeguridadBaja.place(x=80, y=335, height=30, width=120)

        # Etiqueta de descripcion seguridad media
        self.etiquetaDescripcionSeguridadMedia = Tkinter.Label( 
            self.canvas, 
            text='Acceso al aprobar 3/5\n experimentos',
            bg=View.COLOR_SELECTOR,
            fg=ViewAuxiliar.obtenerColor(104,104,104),
            font="SegoeUI 10 normal",
            cursor='hand2'
        ) # End label
        self.etiquetaDescripcionSeguridadMedia.pack()
        self.etiquetaDescripcionSeguridadMedia.place(x=220, y=335, height=30, width=120)

        # Etiqueta de descripcion seguridad alta
        self.etiquetaDescripcionSeguridadAlta = Tkinter.Label( 
            self.canvas, 
            text='Acceso al aprobar 5/5\n experimentos',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(104,104,104),
            font="SegoeUI 10 normal",
            cursor='hand2'
        ) # End label
        self.etiquetaDescripcionSeguridadAlta.pack()
        self.etiquetaDescripcionSeguridadAlta.place(x=360, y=335, height=30, width=120)

        # Crear panel para mostrar seleccion de nivel de seguridad
        self.selector = self.canvas.create_rectangle( 
            215, 215, 345, 370, 
            fill=View.COLOR_SELECTOR, 
            outline=View.COLOR_SELECTOR
        ) # End create_rectangle
        self.canvas.tag_raise(self.selector)

    def establecerListeners( self, controller ):

        # Controles para botones de seguridad alta 
        self.etiquetaImagenSeguridadAlta.bind("<Button-1>", controller.opcionSeguridadAlta_Click)
        self.etiquetaTituloSeguridadAlta.bind("<Button-1>", controller.opcionSeguridadAlta_Click)
        self.etiquetaDescripcionSeguridadAlta.bind("<Button-1>", controller.opcionSeguridadAlta_Click)

        # Controles para botones de seguridad media 
        self.etiquetaImagenSeguridadMedia.bind("<Button-1>", controller.opcionSeguridadMedia_Click)
        self.etiquetaTituloSeguridadMedia.bind("<Button-1>", controller.opcionSeguridadMedia_Click)
        self.etiquetaDescripcionSeguridadMedia.bind("<Button-1>", controller.opcionSeguridadMedia_Click)

        # Controles para botones de seguridad baja 
        self.etiquetaImagenSeguridadBaja.bind("<Button-1>", controller.opcionSeguridadBaja_Click)
        self.etiquetaTituloSeguridadBaja.bind("<Button-1>", controller.opcionSeguridadBaja_Click)
        self.etiquetaDescripcionSeguridadBaja.bind("<Button-1>", controller.opcionSeguridadBaja_Click)

        # Control para eliminar usuario
        self.etiquetaImagenEliminarUsuario.bind("<Button-1>", controller.etiquetaImagenEliminarUsuario_Click)
        
        # Control para cerrar sesion 
        self.etiquetaImagenCerrarSesion.bind("<Button-1>", controller.etiquetaImagenCerrarSesion_Click)