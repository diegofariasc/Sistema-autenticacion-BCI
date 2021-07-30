import tkinter as Tkinter
from ViewAuxiliar import ViewAuxiliar
from View import View
from PIL import ImageTk, Image

# La clase representa la vista al crear un usuario
class ViewCrearUsuario(View):

    def construirView(self):

        # Llamada al constructor de la superclase
        super().construirView()

        # Ajustar ventana general
        self.ventana.geometry("%sx%s"%(View.LARGO,View.ALTO + 100))
        self.canvas.config(height=View.ALTO + 100)
        self.etiquetaPrograma.place(x=10, y=490, height=20, width=View.LARGO)
        self.ventana.title("Sistema de autenticación - Crear usuario")

        # Etiqueta descriptiva de la labor en la ventana
        self.etiquetaDescripcionVentana= Tkinter.Label( 
            self.canvas, 
            text='Registrar un nuevo usuario',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 15 normal"
        ) # End label
        self.etiquetaDescripcionVentana.pack()
        self.etiquetaDescripcionVentana.place(x=0, y=20, height=20, width=View.LARGO)

        # Etiqueta descriptiva de la labor en la ventana
        self.etiquetaInstruccion= Tkinter.Label( 
            self.canvas, 
            text='Proporcione la información del usuario que desea crear',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 13 normal"
        ) # End label
        self.etiquetaInstruccion.pack()
        self.etiquetaInstruccion.place(x=0, y=40, height=20, width=View.LARGO)

        # Etiqueta seleccionar imagen
        self.etiquetaSeleccionarImagen= Tkinter.Label( 
            self.canvas, 
            text='Elegir imagen',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(104,104,104),
            font="SegoeUI 9 normal",
            anchor='w',
            cursor='hand2'
        ) # End label
        self.etiquetaSeleccionarImagen.pack()
        self.etiquetaSeleccionarImagen.place(x=70, y=165, height=20, width=100)

        # Imagen de usuario
        self.imagenUsuario = Image.open("assets/ViewCrearUsuario/imagenNuevoUsuarioDefault.png") 
        self.renderUsuario = ImageTk.PhotoImage(self.imagenUsuario.resize((80,80)), master=self.ventana)

        self.etiquetaImagenUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderUsuario,
        ) # End label
        self.etiquetaImagenUsuario.pack()
        self.etiquetaImagenUsuario.place(x=70, y=80, height=80, width=80)

        # Imagen campo nombre usuario
        self.imagenNombreUsuario = Image.open("assets/ViewCrearUsuario/campoNombreUsuario.png")
        self.renderNombreUsuario  = ImageTk.PhotoImage(self.imagenNombreUsuario, master=self.ventana)
        self.etiquetaImagenNombreUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderNombreUsuario
        ) # End label

        self.etiquetaImagenNombreUsuario.pack()
        self.etiquetaImagenNombreUsuario.place(x=170, y=85, height=20, width=20)

        # Campo nombre de usuario
        self.campoNombre = Tkinter.Entry(
            self.canvas, 
            width = 15,
            highlightbackground=View.COLOR_FONDO,
            font="SegoeUI 10 italic",
            fg=ViewAuxiliar.obtenerColor(124,124,124)
        ) # End entry
        self.campoNombre.insert(0, 'Nombre de usuario')
        
        self.campoNombre.pack()
        self.campoNombre.place(x=192, y=81, height=28, width=250)

        # Imagenes validaciones
        self.imagenValidacionError = Image.open("assets/Compartidas/error.png")
        self.renderValidacionError  = ImageTk.PhotoImage(self.imagenValidacionError, master=self.ventana)
        self.imagenValidacionCorrecta = Image.open("assets/Compartidas/correcto.png")
        self.renderValidacionCorrecta  = ImageTk.PhotoImage(self.imagenValidacionCorrecta, master=self.ventana)

        # Imagen validacion nombre usuario
        self.etiquetaImagenValidacionNombreUsuario = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderValidacionError
        ) # End label

        self.etiquetaImagenValidacionNombreUsuario.pack()
        self.etiquetaImagenValidacionNombreUsuario.place(x=447, y=85, height=20, width=20)


        # Imagen campo contrasena
        self.imagenContrasena = Image.open("assets/ViewPrincipal/contrasena.png")
        self.renderContrasena  = ImageTk.PhotoImage(self.imagenContrasena, master=self.ventana)
        self.etiquetaImagenContrasena = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderContrasena
        ) # End label

        self.etiquetaImagenContrasena.pack()
        self.etiquetaImagenContrasena.place(x=170, y=115, height=20, width=20)

        # Campo contrasena
        self.campoContrasena = Tkinter.Entry(
            self.canvas, 
            width = 15,
            highlightbackground=View.COLOR_FONDO,
            font="SegoeUI 10 italic",
            fg=ViewAuxiliar.obtenerColor(124,124,124)
        ) # End entry
        self.campoContrasena.insert(0, 'Contraseña auxiliar')
        
        self.campoContrasena.pack()
        self.campoContrasena.place(x=192, y=111, height=28, width=250)

        # Imagen validacion contrasena
        self.etiquetaImagenValidacionContrasena = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderValidacionError
        ) # End label

        self.etiquetaImagenValidacionContrasena.pack()
        self.etiquetaImagenValidacionContrasena.place(x=447, y=111, height=20, width=20)

        # Imagen campo confirmar contrasena
        self.etiquetaImagenConfirmarContrasena = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderContrasena
        ) # End label

        self.etiquetaImagenConfirmarContrasena.pack()
        self.etiquetaImagenConfirmarContrasena.place(x=170, y=145, height=20, width=20)

        # Campo confirmar contrasena
        self.campoConfirmarContrasena = Tkinter.Entry(
            self.canvas, 
            width = 15,
            highlightbackground=View.COLOR_FONDO,
            font="SegoeUI 10 italic",
            fg=ViewAuxiliar.obtenerColor(124,124,124)
        ) # End entry
        self.campoConfirmarContrasena.insert(0, 'Confirmar contraseña')
        
        self.campoConfirmarContrasena.pack()
        self.campoConfirmarContrasena.place(x=192, y=141, height=28, width=250)

        # Imagen validacion contrasena
        self.etiquetaImagenValidacionConfirmarContrasena = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderValidacionError
        ) # End label

        self.etiquetaImagenValidacionConfirmarContrasena.pack()
        self.etiquetaImagenValidacionConfirmarContrasena.place(x=447, y=141, height=20, width=20)

        # Etiqueta descriptiva de la seccion de datos EEG
        self.etiquetaSeccionEEG= Tkinter.Label( 
            self.canvas, 
            text='Datos de entrenamiento EEG: No seleccionados',
            bg=View.COLOR_FONDO,
            fg=ViewAuxiliar.obtenerColor(94,94,94),
            font="SegoeUI 11 normal",
            anchor='w'
        ) # End label
        self.etiquetaSeccionEEG.pack()
        self.etiquetaSeccionEEG.place(x=193, y=191, height=20, width=350)

        # Boton de escaneo EEG
        self.imagenEscaneoEEG = Image.open("assets/ViewPrincipal/escaneoEEG.png")
        self.renderEscaneoEEG  = ImageTk.PhotoImage(self.imagenEscaneoEEG, master=self.ventana)
        self.botonEscaneoEEG = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Registrar EEG", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=self.renderEscaneoEEG,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button

        self.botonEscaneoEEG.pack()
        self.botonEscaneoEEG.place(x=170, y=211, height=28, width=115)

        # Boton de cargar archivo EEG
        self.imagenCargarArchivo = Image.open("assets/ViewCrearUsuario/importarDatos.png")
        self.renderCargarArchivo  = ImageTk.PhotoImage(self.imagenCargarArchivo, master=self.ventana)
        self.botonCargarArchivo = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Cargar registro", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=self.renderCargarArchivo,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button
        self.botonCargarArchivo.pack()
        self.botonCargarArchivo.place(x=290, y=211, height=28, width=115)


        # Boton de eliminar origen de datos EEG
        self.imagenDescartarDatos = Image.open("assets/ViewCrearUsuario/descartar.png")
        self.renderDescartarDatos  = ImageTk.PhotoImage(self.imagenDescartarDatos, master=self.ventana)
        self.botonDescartarDatos = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text ="Descartar datos", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            image=self.renderDescartarDatos,
            compound = Tkinter.LEFT,
            cursor='hand2'
        ) # End button


        # Imagen validacion origen de datos EEG
        self.etiquetaImagenValidacionDatosEEG = Tkinter.Label( 
            self.canvas, 
            bg=View.COLOR_FONDO,
            image=self.renderValidacionError
        ) # End label

        self.etiquetaImagenValidacionDatosEEG.pack()
        self.etiquetaImagenValidacionDatosEEG.place(x=170, y=190, height=20, width=20)


        # Etiqueta descriptiva de la seleccion de nivel de seguridad
        self.etiquetaInstruccion= Tkinter.Label( 
            self.canvas, 
            text='Seleccione el nivel de seguridad esperado:',
            bg=View.COLOR_FONDO,
            fg=View.COLOR_CONTRASTE,
            font="SegoeUI 13 normal"
        ) # End label
        self.etiquetaInstruccion.pack()
        self.etiquetaInstruccion.place(x=0, y=261, height=20, width=View.LARGO)

        # Crear panel para mostrar seleccion de nivel de seguridad
        self.selector = self.canvas.create_rectangle( 
            215, 285, 345, 430, 
            fill=View.COLOR_SELECTOR, 
            outline=View.COLOR_SELECTOR
        ) # End create_rectangle
        self.canvas.tag_raise(self.selector)

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
        self.etiquetaImagenSeguridadBaja.place(x=80, y=290, height=90, width=120)

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
        self.etiquetaImagenSeguridadMedia.place(x=220, y=290, height=90, width=120)

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
        self.etiquetaImagenSeguridadAlta.place(x=360, y=294, height=90, width=120)

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
        self.etiquetaTituloSeguridadBaja.place(x=80, y=382, height=20, width=120)

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
        self.etiquetaTituloSeguridadMedia.place(x=220, y=382, height=20, width=120)

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
        self.etiquetaTituloSeguridadAlta.place(x=360, y=382, height=20, width=120)

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
        self.etiquetaDescripcionSeguridadBaja.place(x=80, y=405, height=20, width=120)

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
        self.etiquetaDescripcionSeguridadMedia.place(x=220, y=405, height=20, width=120)

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
        self.etiquetaDescripcionSeguridadAlta.place(x=360, y=405, height=20, width=120)

        # Boton para cancelar registro
        self.imagenCancelar = Image.open("assets/ViewCrearUsuario/cancelar.png")
        self.renderCancelar = ImageTk.PhotoImage(self.imagenCancelar, master=self.ventana)
        self.botonCancelar = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text =" Cancelar", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            cursor='hand2',
            image=self.renderCancelar,
            compound = Tkinter.LEFT,
        ) # End button
        self.botonCancelar.pack()
        self.botonCancelar.place(x=340, y=470, height=28, width=90)

        # Boton para efectuar registro
        self.imagenRegistrar = Image.open("assets/ViewCrearUsuario/registrar.png")
        self.renderRegistrar  = ImageTk.PhotoImage(self.imagenRegistrar, master=self.ventana)
        self.botonRegistrar = Tkinter.Button( 
            self.canvas, 
            fg=View.COLOR_CONTRASTE, 
            text =" Registrar", 
            font="SegoeUI 11 normal",
            highlightbackground=View.COLOR_FONDO,
            cursor='hand2',
            image=self.renderRegistrar,
            compound = Tkinter.LEFT,
        ) # End button
        self.botonRegistrar.pack()
        self.botonRegistrar.place(x=440, y=470, height=28, width=90)

        # Desactivar inicialmente el boton de registrar
        self.botonRegistrar["state"] = 'disable'

    def establecerListeners( self, controller ):

        # Etiqueta de seleccionar imagen
        self.etiquetaSeleccionarImagen.bind("<Button-1>", controller.etiquetaSeleccionarImagen_Click)

        # Botones cancelar y registrar
        self.botonRegistrar.bind("<Button-1>", controller.botonRegistrar_Click)
        self.botonCancelar.bind("<Button-1>", controller.botonCancelar_Click)

        # Boton cargar registros y recopilar informacion EEG
        self.botonEscaneoEEG.bind("<Button-1>", controller.botonRegistrarEEG_Click)
        self.botonCargarArchivo.bind("<Button-1>", controller.botonCargarArchivo_Click)

        # Boton para anular seleccion de origen de datos EEG
        self.botonDescartarDatos.bind("<Button-1>", controller.botonDescartarDatos_Click)

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

        # Clic en los campos
        self.campoNombre.bind("<FocusIn>", controller.campoNombre_Focus)
        self.campoContrasena.bind("<FocusIn>", controller.campoContrasena_Focus)
        self.campoConfirmarContrasena.bind("<FocusIn>", controller.campoConfirmarContrasena_Focus)

        # Perdida de foco en los campos
        self.campoNombre.bind("<FocusOut>", controller.campoNombre_LostFocus)
        self.campoContrasena.bind("<FocusOut>", controller.campoContrasena_LostFocus)
        self.campoConfirmarContrasena.bind("<FocusOut>", controller.campoConfirmarContrasena_LostFocus)

        # Presionar una tecla en los campos
        self.campoNombre.bind("<KeyRelease>", controller.campoNombre_KeyRelease)
        self.campoContrasena.bind("<KeyRelease>", controller.campoContrasena_KeyRelease)
        self.campoConfirmarContrasena.bind("<KeyRelease>", controller.campoConfirmarContrasena_KeyRelease)