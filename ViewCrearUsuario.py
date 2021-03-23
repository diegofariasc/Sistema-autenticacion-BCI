import tkinter as Tkinter
from ViewAuxiliar import ViewAuxiliar
from View import View
from PIL import ImageTk, Image

# La clase representa la vista al crear un usuario
class ViewCrearUsuario(View):

    def __init__(self):

        # Llamada al constructor de la superclase
        super().__init__()

        # Ajustar ventana general
        self.ventana.geometry("%sx%s"%(View.LARGO,View.ALTO + 100))
        self.canvas.config(height=View.ALTO + 100)
        self.etiquetaPrograma.place(x=10, y=490, height=20, width=View.LARGO)
        self.ventana.title("Sistema de autenticación - Crear usuario")

        # Etiqueta descriptiva de la labor en la ventana
        etiquetaDescripcionVentana= Tkinter.Label( 
            self.canvas, 
            text='Registrar un nuevo usuario',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 15 normal"
        ) # End label
        etiquetaDescripcionVentana.pack()
        etiquetaDescripcionVentana.place(x=0, y=20, height=20, width=View.LARGO)

        # Etiqueta descriptiva de la labor en la ventana
        etiquetaInstruccion= Tkinter.Label( 
            self.canvas, 
            text='Proporcione la información del usuario que desea crear',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 13 normal"
        ) # End label
        etiquetaInstruccion.pack()
        etiquetaInstruccion.place(x=0, y=40, height=20, width=View.LARGO)

        # Etiqueta seleccionar imagen
        etiquetaSeleccionarImagen= Tkinter.Label( 
            self.canvas, 
            text='Elegir imagen',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(104,104,104),
            font="SegoeUI 9 normal",
            anchor='w',
            cursor='hand2'
        ) # End label
        etiquetaSeleccionarImagen.pack()
        etiquetaSeleccionarImagen.place(x=70, y=165, height=20, width=100)

        # Imagen de usuario
        imagenUsuario = Image.open("assets/ViewCrearUsuario/imagenNuevoUsuarioDefault.png") 
        imagenUsuario = imagenUsuario.resize((80,80))
        renderUsuario = ImageTk.PhotoImage(imagenUsuario)

        etiquetaImagenUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderUsuario,
        ) # End label
        etiquetaImagenUsuario.pack()
        etiquetaImagenUsuario.place(x=70, y=80, height=80, width=80)

        # Imagen campo nombre usuario
        imagenNombreUsuario = Image.open("assets/ViewCrearUsuario/campoNombreUsuario.png")
        renderNombreUsuario  = ImageTk.PhotoImage(imagenNombreUsuario)
        etiquetaImagenNombreUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderNombreUsuario
        ) # End label

        etiquetaImagenNombreUsuario.pack()
        etiquetaImagenNombreUsuario.place(x=170, y=85, height=20, width=20)

        # Campo nombre de usuario
        campoNombre = Tkinter.Entry(
            self.canvas, 
            width = 15,
            highlightbackground=View.COLOR_FONDO,
            font="SegoeUI 10 italic",
            fg=ViewAuxiliar.obtenerColor(124,124,124)
        ) # End entry
        campoNombre.insert(0, 'Nombre de usuario')
        
        campoNombre.pack()
        campoNombre.place(x=192, y=81, height=28, width=250)


        # Imagen campo contrasena
        imagenContrasena = Image.open("assets/ViewPrincipal/contrasena.png")
        renderContrasena  = ImageTk.PhotoImage(imagenContrasena)
        etiquetaImagenContrasena = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderContrasena
        ) # End label

        etiquetaImagenContrasena.pack()
        etiquetaImagenContrasena.place(x=170, y=115, height=20, width=20)

        # Campo contrasena
        campoContrasena = Tkinter.Entry(
            self.canvas, 
            width = 15,
            highlightbackground=View.COLOR_FONDO,
            font="SegoeUI 10 italic",
            fg=ViewAuxiliar.obtenerColor(124,124,124)
        ) # End entry
        campoContrasena.insert(0, 'Contraseña auxiliar')
        
        campoContrasena.pack()
        campoContrasena.place(x=192, y=111, height=28, width=250)

        # Imagen campo confirmar contrasena
        etiquetaImagenConfirmarContrasena = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=renderContrasena
        ) # End label

        etiquetaImagenConfirmarContrasena.pack()
        etiquetaImagenConfirmarContrasena.place(x=170, y=145, height=20, width=20)

        # Campo confirmar contrasena
        campoConfirmarContrasena = Tkinter.Entry(
            self.canvas, 
            width = 15,
            highlightbackground=View.COLOR_FONDO,
            font="SegoeUI 10 italic",
            fg=ViewAuxiliar.obtenerColor(124,124,124)
        ) # End entry
        campoConfirmarContrasena.insert(0, 'Confirmar contraseña')
        
        campoConfirmarContrasena.pack()
        campoConfirmarContrasena.place(x=192, y=141, height=28, width=250)

        # Etiqueta descriptiva de la seccion de datos EEG
        etiquetaSeccionEEG= Tkinter.Label( 
            self.canvas, 
            text='Datos de entrenamiento EEG',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(94,94,94),
            font="SegoeUI 11 normal",
            anchor='w'
        ) # End label
        etiquetaSeccionEEG.pack()
        etiquetaSeccionEEG.place(x=170, y=191, height=20, width=220)

        # Boton de escaneo EEG
        imagenEscaneoEEG = Image.open("assets/ViewPrincipal/escaneoEEG.png")
        renderEscaneoEEG  = ImageTk.PhotoImage(imagenEscaneoEEG)
        botonEscaneoEEG = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Registrar EEG", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=renderEscaneoEEG,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button

        botonEscaneoEEG.pack()
        botonEscaneoEEG.place(x=170, y=211, height=28, width=115)

        # Boton de cargar archivo EEG
        imagenCargarArchivo = Image.open("assets/ViewCrearUsuario/importarDatos.png")
        renderCargarArchivo  = ImageTk.PhotoImage(imagenCargarArchivo)
        botonCargarArchivo = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Cargar registro", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=renderCargarArchivo,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button
        botonCargarArchivo.pack()
        botonCargarArchivo.place(x=290, y=211, height=28, width=115)

        # Etiqueta descriptiva de la seleccion de nivel de seguridad
        etiquetaInstruccion= Tkinter.Label( 
            self.canvas, 
            text='Seleccione el nivel de seguridad esperado:',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 13 normal"
        ) # End label
        etiquetaInstruccion.pack()
        etiquetaInstruccion.place(x=0, y=261, height=20, width=View.LARGO)

        # Crear panel para mostrar seleccion de nivel de seguridad
        self.selector = self.canvas.create_rectangle( 
            215, 285, 345, 430, 
            fill=View.COLOR_SELECTOR, 
            outline=View.COLOR_SELECTOR
        ) # End create_rectangle
        self.canvas.tag_raise(self.selector)


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
        etiquetaImagenSeguridadBaja.place(x=80, y=290, height=90, width=120)

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
        etiquetaImagenSeguridadMedia.place(x=220, y=290, height=90, width=120)

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
        etiquetaImagenSeguridadAlta.place(x=360, y=294, height=90, width=120)

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
        etiquetaTituloSeguridadBaja.place(x=80, y=382, height=20, width=120)

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
        etiquetaTituloSeguridadMedia.place(x=220, y=382, height=20, width=120)

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
        etiquetaTituloSeguridadAlta.place(x=360, y=382, height=20, width=120)

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
        etiquetaDescripcionSeguridadBaja.place(x=80, y=405, height=20, width=120)

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
        etiquetaDescripcionSeguridadMedia.place(x=220, y=405, height=20, width=120)

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
        etiquetaDescripcionSeguridadAlta.place(x=360, y=405, height=20, width=120)

        # Boton para cancelar registro
        imagenCancelar = Image.open("assets/ViewCrearUsuario/cancelar.png")
        renderCancelar = ImageTk.PhotoImage(imagenCancelar)
        botonCancelar = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text =" Cancelar", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            cursor='hand2',
            image=renderCancelar,
            compound = Tkinter.LEFT,
        ) # End button
        botonCancelar.pack()
        botonCancelar.place(x=340, y=470, height=28, width=90)

        # Boton para efectuar registro
        imagenRegistrar = Image.open("assets/ViewCrearUsuario/registrar.png")
        renderRegistrar  = ImageTk.PhotoImage(imagenRegistrar)
        botonRegistrar = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text =" Registrar", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            cursor='hand2',
            image=renderRegistrar,
            compound = Tkinter.LEFT,
        ) # End button
        botonRegistrar.pack()
        botonRegistrar.place(x=440, y=470, height=28, width=90)

        # Ciclo principal
        self.ventana.mainloop()

