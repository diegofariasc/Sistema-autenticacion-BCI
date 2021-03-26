from Controller import Controller
from tkinter.filedialog import askopenfilename
from View import View
from ViewAuxiliar import ViewAuxiliar
from PIL import ImageTk
from Model import Model
from tkinter import messagebox as MessageBox
import tkinter as Tkinter
import os

class ControllerCrearUsuario(Controller):

    # Variables estaticas para identificar
    # las opciones de seguridad en el view 
    SEGURIDAD_BAJA = 75
    SEGURIDAD_MEDIA = 215
    SEGURIDAD_ALTA = 355      

    def __init__(self, view, model):
        super().__init__(view, model)
        self.__seguridadSeleccionada = Model.SEGURIDAD_MEDIA
        self.__aprobadoNombre = False
        self.__aprobadaContrasena = False
        self.__aprobadaConfirmacionContrasena = False
        self.__aprobadoOrigenDatosEEG = False
        self.__origenArchivo = ''
        self.__imagenSeleccionada = None

    """
    El metodo es invocado cuando se hace clic en el boton de
    cargar registro en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def botonCargarArchivo_Click(self, evento):

        # Lanzar cuadro para seleccion de imagen
        self.__origenArchivo = askopenfilename(filetypes=[("Registros EEG en formato GDF", ".gdf")]) 

        # Ver si el usuario selecciono algo
        if self.__origenArchivo != '':

            # Cambiar view para denotar validacion
            self._view.etiquetaSeccionEEG.config(
                text='Datos de entrenamiento EEG: ' + os.path.basename(self.__origenArchivo) 
            ) # End config

            self._view.etiquetaImagenValidacionDatosEEG.config(  
                image=self._view.renderValidacionCorrecta
            ) # End config

            # Desaparecer botones para seleccionar origen de datos
            self._view.botonDescartarDatos.place(x=170, y=211, height=28, width=115)
            self._view.botonEscaneoEEG.place_forget()
            self._view.botonCargarArchivo.place_forget()

            self.__aprobadoOrigenDatosEEG = True

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
        self.__origenArchivo = ''
        self.__aprobadoOrigenDatosEEG = False

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
            3.15,
            4.2,
            5.5,
            9.03,
            Model.SEGURIDAD_ALTA,
            imagen=self.__imagenSeleccionada ):

            MessageBox.showinfo(
                "Usuario registrado",
                "El usuario se ha registrado exitosamente"
            ) # End showinfo
            self.__cerrarVentana()

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
        self.__cerrarVentana()

    """
    El metodo permite cerrar la ventana actual y destruir el 
    controller asociado
    Input:  None
    Output: None
    """
    def __cerrarVentana(self):
        self._view.ventana.destroy()
        del self._view
        del self

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
            ubicacionImagen = askopenfilename(filetypes=[("Imagenes", ".jpg")]) 

            # Seleccionar imagen, cargarla y recortarla. Mantener en memoria
            self.__imagenSeleccionada = ViewAuxiliar.recortarImagenUsuario(ubicacionImagen)
            self.__imagenSeleccionada = self.__imagenSeleccionada.resize((80,80))
            self.__renderImagenSeleccionada = ImageTk.PhotoImage(self.__imagenSeleccionada, master=self._view.ventana)

            # Reflejar imagen en view
            self._view.etiquetaImagenUsuario.config(image=self.__renderImagenSeleccionada)

        # En caso que el usuario cancele la operacion
        except AttributeError:
            pass

    """
    El metodo es invocado cuando se hace clic en cualquier elemento
    que constituye la opcion de seguridad alta en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def opcionSeguridadAlta_Click(self, evento):

        # Revisar en que opcion de seguridad se encuentra posicionado el usuario
        opcionSeleccionada = self._view.canvas.coords(self._view.selector)[0]

        # Establecer la nueva seleccion en la seguridad alta
        self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_ALTA, True)

        # Revisar la opcion de seguridad seleccionada y deseleccionarla
        if opcionSeleccionada == ControllerCrearUsuario.SEGURIDAD_MEDIA:
            self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_MEDIA, False)
            self._view.canvas.move(self._view.selector, 140,0)

        if opcionSeleccionada == ControllerCrearUsuario.SEGURIDAD_BAJA:
            self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_BAJA, False)
            self._view.canvas.move(self._view.selector, 280,0)

        self.__seguridadSeleccionada = Model.SEGURIDAD_ALTA
    
    """
    El metodo es invocado cuando se hace clic en cualquier elemento
    que constituye la opcion de seguridad media en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def opcionSeguridadMedia_Click(self, evento):

        # Revisar en que opcion de seguridad se encuentra posicionado el usuario
        opcionSeleccionada = self._view.canvas.coords(self._view.selector)[0]

        # Establecer la nueva seleccion en la seguridad media
        self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_MEDIA, True)

        # Revisar la opcion de seguridad seleccionada y deseleccionarla
        if opcionSeleccionada == ControllerCrearUsuario.SEGURIDAD_BAJA:
            self._view.canvas.move(self._view.selector, 140,0)
            self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_BAJA, False)

        if opcionSeleccionada == ControllerCrearUsuario.SEGURIDAD_ALTA:
            self._view.canvas.move(self._view.selector, -140,0)
            self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_ALTA, False)

        self.__seguridadSeleccionada = Model.SEGURIDAD_MEDIA

    """
    El metodo es invocado cuando se hace clic en cualquier elemento
    que constituye la opcion de seguridad baja en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def opcionSeguridadBaja_Click(self, evento):

        # Revisar en que opcion de seguridad se encuentra posicionado el usuario
        opcionSeleccionada = self._view.canvas.coords(self._view.selector)[0]

        # Establecer la nueva seleccion en la seguridad baja
        self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_BAJA, True)

        # Revisar la opcion de seguridad seleccionada y deseleccionarla
        if opcionSeleccionada == ControllerCrearUsuario.SEGURIDAD_MEDIA:
            self._view.canvas.move(self._view.selector, -140,0)
            self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_MEDIA, False)

        if opcionSeleccionada == ControllerCrearUsuario.SEGURIDAD_ALTA:
            self._view.canvas.move(self._view.selector, -280,0)
            self.__cambiarSeleccionOpcion(ControllerCrearUsuario.SEGURIDAD_ALTA, False)
    
        self.__seguridadSeleccionada = Model.SEGURIDAD_BAJA

    """
    El metodo permite visualmente cambiar la seleccion de las 
    opciones de seguridad
    Input:  opcion - el nivel de seguridad a modificar
            seleccionado - booleano indicando si modificarlo 
            como seleccionado o deseleccionado
    Output: None
    """
    def __cambiarSeleccionOpcion( self, opcion, seleccionado ):

        # Verificar el color a aplicar a la opcion dependiendo de si
        # se pretende seleccionar o deseleccionar
        color = (View.COLOR_SELECTOR if seleccionado else View.COLOR_FONDO)

        # Identificar la opcion de seguridad que recibira el efecto
        # y aplicarlo
        if opcion == ControllerCrearUsuario.SEGURIDAD_ALTA:
            self._view.etiquetaImagenSeguridadAlta.config( bg = color )
            self._view.etiquetaTituloSeguridadAlta.config( bg = color )
            self._view.etiquetaDescripcionSeguridadAlta.config( bg = color )

        elif opcion == ControllerCrearUsuario.SEGURIDAD_MEDIA:
            self._view.etiquetaImagenSeguridadMedia.config( bg = color )
            self._view.etiquetaTituloSeguridadMedia.config( bg = color )
            self._view.etiquetaDescripcionSeguridadMedia.config( bg = color )

        elif opcion == ControllerCrearUsuario.SEGURIDAD_BAJA:
            self._view.etiquetaImagenSeguridadBaja.config( bg = color )
            self._view.etiquetaTituloSeguridadBaja.config( bg = color )
            self._view.etiquetaDescripcionSeguridadBaja.config( bg = color )
        
        
    """
    El metodo permite validar que todos los campos se han llenado
    satisfactoriamente y, de ser asi activar la opcion de registro
    Input:  None
    Output: None
    """
    def __validarTodosCampos(self):

        # Revisar si todos los campos han sido aprobados
        if  self.__aprobadoNombre and self.__aprobadaContrasena and \
            self.__aprobadaConfirmacionContrasena and self.__aprobadoOrigenDatosEEG:

            self._view.botonRegistrar["state"] = 'normal'
        else:
            self._view.botonRegistrar["state"] = 'disable'