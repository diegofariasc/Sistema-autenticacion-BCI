from threading                      import Thread
from Controller                     import Controller
from tkinter.filedialog             import askopenfilenames, askdirectory
from View                           import View
from ViewAuxiliar                   import ViewAuxiliar
from PIL                            import ImageTk
from Model                          import Model
from tkinter                        import messagebox as MessageBox
from ControllerSelectorSeguridad    import ControllerSelectorSeguridad
from ControllerRecopilador          import ControllerRecopilador
from ViewRecopilador                import ViewRecopilador
from Movimiento                     import Movimiento

import tkinter as Tkinter
import os

class ControllerCrearUsuario(ControllerSelectorSeguridad):

    def __init__(self, view, model):
        super().__init__(view, model)
        self.__aprobadoNombre = False
        self.__aprobadaContrasena = False
        self.__aprobadaConfirmacionContrasena = False
        self.aprobadoOrigenDatosEEG = False
        self.__archivosOrigen = []
        self.__imagenSeleccionada = None

        # Arreglos para almacenar la informacion
        # recopilada
        self.datos_C1 = None
        self.datos_C2 = None
        self.hayDatosEEG = False

    """
    El metodo es invocado cuando se hace clic en el boton de
    registrar EEG en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def botonRegistrarEEG_Click(self, evento):

        # Solicitar la confirmacion antes de iniciar
        iniciar = MessageBox.askyesno(title='Iniciar grabación',
                    message='Se iniciará una recopilación de datos EEG\n' +\
                            'Deberá tener su casco conectado antes de iniciar\n'
                            '¿Está seguro de que desea continuar?')

        # Si se ha dado permiso para iniciar
        if iniciar:
            viewRecopilador = ViewRecopilador()
            controllerViewRecopilador = ControllerRecopilador( viewRecopilador, self._model, self._view, self )
            
            # Lanzar el recopilador
            Thread(
                target=controllerViewRecopilador.inicializarView()
            ).start()
            

    """
    El metodo es invocado cuando se hace clic en el boton de
    cargar registro en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def botonCargarArchivo_Click(self, evento):

        # Lanzar cuadro para seleccion de imagen
        self.__archivosOrigen = list(askopenfilenames(
            title = 'Choose a file',
            filetypes = [("Registros EEG en formato GDF", ".gdf")]
        )) # End askopenfilename 

        # Ver si el usuario selecciono algo valido
        if len(self.__archivosOrigen) >= 2 :

            # Construir etiqueta con los nombres de archivos
            # cargados
            textoArchivos = 'Datos de entrenamiento EEG: '

            for i in range( len(self.__archivosOrigen) ):

                textoArchivos += os.path.basename(self.__archivosOrigen[i])

                if i < len(self.__archivosOrigen) - 1:
                    textoArchivos += ", "

            # Cambiar view para denotar validacion
            self._view.etiquetaSeccionEEG.config(
                text = textoArchivos 
            ) # End config

            self._view.etiquetaImagenValidacionDatosEEG.config(  
                image=self._view.renderValidacionCorrecta
            ) # End config

            # Desaparecer botones para seleccionar origen de datos
            self._view.botonDescartarDatos.place(x=170, y=211, height=28, width=115)
            self._view.botonEscaneoEEG.place_forget()
            self._view.botonCargarArchivo.place_forget()

            self.aprobadoOrigenDatosEEG = True

        # Ver si tras seleccionar el archivo ya es posible
        # registrar al sujeto
        self.__validarTodosCampos()


    """
    El metodo es invocado cuando se hace clic en el boton de
    descartar datos en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def botonDescartarDatos_Click(self, evento):

        # Quitar validacion
        self.__archivosOrigen = []
        self.aprobadoOrigenDatosEEG = False
        self.hayDatosEEG = False
        self.datos_C1 = None
        self.datos_C1 = None

        # Reflejar la desaprobacion en el view
        self._view.etiquetaSeccionEEG.config(
            text='Datos de entrenamiento EEG: No seleccionados' 
        ) # End config

        self._view.etiquetaImagenValidacionDatosEEG.config(  
            image=self._view.renderValidacionError
        ) # End config

        # Aparecer botones para seleccionar origen de datos
        self._view.botonDescartarDatos.place_forget()
        self._view.botonEscaneoEEG.place(x=170, y=211, height=28, width=115)
        self._view.botonCargarArchivo.place(x=290, y=211, height=28, width=115)

        # Desaparecer boton de registrar
        self.__validarTodosCampos()


    """
    El metodo es invocado cuando se hace clic en el boton de
    registrar en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def botonRegistrar_Click(self, evento):

        # Registrar en el model
        if  self._model.insertarUsuario(
            self._view.campoNombre.get(),
            self._view.campoContrasena.get(),
            self._seguridadSeleccionada,
            imagen=self.__imagenSeleccionada ):

            # Obtener el identificador del usuario insertado
            usuario = self._model.obtenerUltimoUsuarioInsertado()

            # Revisar si los datos son recopilados
            if self.hayDatosEEG:
                self._model.insertarExperimentos(self.datos_C1, Movimiento.TIPO_C1, usuario)
                self._model.insertarExperimentos(self.datos_C2, Movimiento.TIPO_C2, usuario)
                self._model.notificarGrabacionSesion(usuario)

            MessageBox.showinfo(
                "Usuario registrado",
                "El usuario se ha registrado exitosamente"
            ) # End showinfo

            from ControllerPrincipal import ControllerPrincipal
            from ViewPrincipal import ViewPrincipal

            # Crear un nuevo view de crear usuario y relacionarlo con un controller
            viewPrincipal = ViewPrincipal()
            controllerPrincipal = ControllerPrincipal( 
                viewPrincipal, 
                self._model
            ) # End construct

            try:
                self._cerrarVentana()
            except:
                Tkinter.TclError

            controllerPrincipal.inicializarView()

        else:
            MessageBox.showerror(
                "Error al crear el usuario",
                "Se ha producido un error al crear el usuario"
            ) # End showerror


    """
    El metodo es invocado cuando se hace clic en el boton cancelar
    en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def botonCancelar_Click(self,evento):

        from ControllerPrincipal import ControllerPrincipal
        from ViewPrincipal import ViewPrincipal

        # Crear un nuevo view de crear usuario y relacionarlo con un controller
        viewPrincipal = ViewPrincipal()
        controllerPrincipal = ControllerPrincipal( 
            viewPrincipal, 
            self._model
        ) # End construct

        try:
            self._cerrarVentana()
        except:
            Tkinter.TclError

        controllerPrincipal.inicializarView()

    """
    El metodo es invocado cuando se adquiere el foco en el 
    campo de nombre en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoNombre_Focus(self,evento):
        if self._view.campoNombre.get() == 'Nombre de usuario':
            self._view.campoNombre.delete(0,Tkinter.END)
            self._view.campoNombre.config(
                fg=View.COLOR_CONTRASTE,
                font="SegoeUI 10 normal"
            ) # End config

    """
    El metodo es invocado cuando se adquiere el foco en el campo de 
    contrasena en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoContrasena_Focus(self,evento):
        if self._view.campoContrasena.get() == 'Contraseña auxiliar':
            self._view.campoContrasena.delete(0,Tkinter.END)
            self._view.campoContrasena.config(  
                show="●",
                fg=View.COLOR_CONTRASTE,
                font="SegoeUI 10 normal"
            ) # End config

    """
    El metodo es invocado cuando se adquiere el foco en el campo de
    confirmar contrasena en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoConfirmarContrasena_Focus(self,evento):
        if self._view.campoConfirmarContrasena.get() == 'Confirmar contraseña':
            self._view.campoConfirmarContrasena.delete(0,Tkinter.END)
            self._view.campoConfirmarContrasena.config( 
                show="●",
                fg=View.COLOR_CONTRASTE,
                font="SegoeUI 10 normal"
            ) # End config

    """
    El metodo es invocado cuando se pierde el foco en el campo de
    nombre en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoNombre_LostFocus(self,evento):
        if self._view.campoNombre.get() == '':
            self._view.campoNombre.insert(0,'Nombre de usuario')
            self._view.campoNombre.config(  
                fg=ViewAuxiliar.obtenerColor(124,124,124),
                font="SegoeUI 10 italic"
            ) # End config

    """
    El metodo es invocado cuando se pierde el foco en el campo de
    contrasena en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoContrasena_LostFocus(self,evento):
        if self._view.campoContrasena.get() == '':
            self._view.campoContrasena.insert(0,'Contraseña auxiliar')
            self._view.campoContrasena.config(  
                show='',
                fg=ViewAuxiliar.obtenerColor(124,124,124),
                font="SegoeUI 10 italic"
            ) # End config

    """
    El metodo es invocado cuando se pierde el foco en el campo de
    confirmar contrasena en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoConfirmarContrasena_LostFocus(self,evento):
        if self._view.campoConfirmarContrasena.get() == '':
            self._view.campoConfirmarContrasena.insert(0,'Confirmar contraseña')
            self._view.campoConfirmarContrasena.config(  
                show='',
                fg=ViewAuxiliar.obtenerColor(124,124,124),
                font="SegoeUI 10 italic"
            ) # End config


    """
    El metodo es invocado cuando se presiona una tecla en el campo de
    nombre de usuario en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoNombre_KeyRelease(self,evento):

        nombre = self._view.campoNombre.get() 

        if  nombre == '' or nombre == 'Nombre de usuario':

            self._view.etiquetaImagenValidacionNombreUsuario.config(  
                image=self._view.renderValidacionError
            ) # End config
            self.__aprobadoNombre = False

        else:
            self._view.etiquetaImagenValidacionNombreUsuario.config(  
                image=self._view.renderValidacionCorrecta
            ) # End config

            self.__aprobadoNombre = True

        # Revisar si ya se han pasado todas las condiciones 
        # para registrar al usuario
        self.__validarTodosCampos()

    """
    El metodo es invocado cuando se presiona una tecla en el campo de
    contrasena en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoContrasena_KeyRelease(self,evento):

        contrasena = self._view.campoContrasena.get()

        if  contrasena == '' or \
            contrasena == 'Contraseña auxiliar' or \
            len(contrasena) < 8 or \
            not any(letra.islower() for letra in contrasena) or \
            not any(letra.isupper() for letra in contrasena) or \
            not any(letra.isdigit() for letra in contrasena) or \
            not any(not letra.isalnum() for letra in contrasena):

            self._view.etiquetaImagenValidacionContrasena.config(  
                image=self._view.renderValidacionError
            ) # End config

            self.__aprobadaContrasena= False

        else:
            self._view.etiquetaImagenValidacionContrasena.config(  
                image=self._view.renderValidacionCorrecta
            ) # End config

            self.__aprobadaContrasena = True

        # Revisar si ya se han pasado todas las condiciones 
        # para registrar al usuario
        self.__validarTodosCampos()

    """
    El metodo es invocado cuando se presiona una tecla en el campo de
    confirmar contrasena en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoConfirmarContrasena_KeyRelease(self,evento):

        confirmacion = self._view.campoConfirmarContrasena.get()

        if  confirmacion == '' or confirmacion == 'Confirmar contraseña' or \
            confirmacion != self._view.campoContrasena.get():

            self._view.etiquetaImagenValidacionConfirmarContrasena.config(  
                image=self._view.renderValidacionError
            ) # End config

            self.__aprobadaConfirmacionContrasena = False

        else:
            self._view.etiquetaImagenValidacionConfirmarContrasena.config(  
                image=self._view.renderValidacionCorrecta
            ) # End config

            self.__aprobadaConfirmacionContrasena = True

        # Revisar si ya se han pasado todas las condiciones 
        # para registrar al usuario
        self.__validarTodosCampos()
        


    """
    El metodo es invocado cuando se hace clic en la etiqueta
    de seleccionar imagen en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def etiquetaSeleccionarImagen_Click(self,evento):

        try:
            # Lanzar cuadro para seleccion de imagen
            ubicacionImagen = askopenfilenames(filetypes=[("Imagenes", ".jpg")]) 

            # Seleccionar imagen, cargarla y recortarla. Mantener en memoria
            self.__imagenSeleccionada = ViewAuxiliar.recortarImagenUsuario(ubicacionImagen)
            self.__imagenSeleccionada = self.__imagenSeleccionada.resize((147,147))
            self.__renderImagenSeleccionada = ImageTk.PhotoImage(self.__imagenSeleccionada.resize((80,80)), master=self._view.ventana)

            # Reflejar imagen en view
            self._view.etiquetaImagenUsuario.config(image=self.__renderImagenSeleccionada)

        # En caso que el usuario cancele la operacion
        except AttributeError:
            pass
        
    """
    El metodo permite validar que todos los campos se han llenado
    satisfactoriamente y, de ser asi activar la opcion de registro
    Input:  None
    Output: None
    """
    def __validarTodosCampos(self):

        # Revisar si todos los campos han sido aprobados
        if  self.__aprobadoNombre and self.__aprobadaContrasena and \
            self.__aprobadaConfirmacionContrasena and self.aprobadoOrigenDatosEEG:

            self._view.botonRegistrar["state"] = 'normal'
        else:
            self._view.botonRegistrar["state"] = 'disable'