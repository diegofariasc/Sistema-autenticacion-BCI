from threading                  import Thread
from Controller                 import Controller
from ViewIniciado               import ViewIniciado
from ControllerIniciado         import ControllerIniciado
from ViewCrearUsuario           import ViewCrearUsuario
from ControllerCrearUsuario     import ControllerCrearUsuario
from PIL                        import Image, ImageTk
from View                       import View
from ViewAuxiliar               import ViewAuxiliar
from ControllerRecopilador      import ControllerRecopilador
from ViewRecopilador            import ViewRecopilador
from tkinter                    import messagebox as MessageBox

import tkinter as Tkinter
import locale

class ControllerPrincipal(Controller):

    def __init__(self, view, model, seleccionado=None):

        super().__init__(view,model)
        self.__usuarioSeleccionado = 0
        self.idUsuarioSeleccionado = None
        self.resultadoRecopilador = None
        self.hayUsuarioPreseleccionado = (seleccionado != None)
        self.__bloquearBotonesDerechaIzquierda = False

        if seleccionado != None:
            self.__usuarioSeleccionado = seleccionado

    def etiquetaImagenAbortarInicio_Click(self, evento):    
        print('100')
        exit(0)

    def etiquetaImagenNuevoUsuario_Click(self, _):

        # Crear un nuevo view de crear usuario y relacionarlo con un controller
        viewCrearUsuario = ViewCrearUsuario()
        controllerCrearUsuario = ControllerCrearUsuario( 
            viewCrearUsuario, 
            self._model
        ) # End construct

        try:
            self._cerrarVentana()
        except:
            Tkinter.TclError

        controllerCrearUsuario.inicializarView()


    def etiquetaImagenDerecha_Click(self, _):

        # Mover en 1 el indicador usuarioSeleccionado y reflejarlo
        # en el view
        if  self.__usuarioSeleccionado < self._model.obtenerNumeroUsuarios() - 1 \
            and not self.__bloquearBotonesDerechaIzquierda:
            self.__usuarioSeleccionado += 1
            self.__mostrarUsuarioSeleccionado()

    def etiquetaImagenIzquierda_Click(self, _):

        # Mover en 1 el indicador usuarioSeleccionado y reflejarlo
        # en el view
        if self.__usuarioSeleccionado > 0 \
            and not self.__bloquearBotonesDerechaIzquierda:
            self.__usuarioSeleccionado -= 1
            self.__mostrarUsuarioSeleccionado()

    def botonContrasena_Click(self,_):        

        # Desaparecer botones de metodos de ingreso 
        self._view.botonContrasena.place_forget()
        self._view.botonEscaneoEEG.place_forget()

        # Mostrar campo y opciones para ingresar por contrasena
        self._view.campoContrasena.place(x=165, y=345, height=28, width=170)
        self._view.etiquetaImagenIngresar.place(x=366, y=345, height=27, width=27)
        self._view.etiquetaVolverMetodoIngreso.place(x=338, y=345, height=27, width=27)
        
        # Bloquear controles a izquierda y derecha
        self._view.etiquetaImagenIzquierda.config(
            image=self._view.renderIzquierdaDesactivado,
            cursor = 'arrow' 
        ) # End config

        self._view.etiquetaImagenDerecha.config(
            image=self._view.renderDerechaDesactivado,
            cursor = 'arrow' 
        ) # End config

        self.__bloquearBotonesDerechaIzquierda = True

        # Cambiar titulo de la ventana
        self._view.etiquetaDescripcionVentana.config(text='Especifique la contraseña para')

        # Seleccionar el campo de contrasena
        self._view.campoContrasena.focus()
        self._view.campoContrasena.select_clear()
        self._view.campoContrasena.select_range(0,'end')

    def etiquetaVolverMetodoIngreso_Click(self,_):

        # Reaparecer botones de metodos de autenticacion
        self._view.botonEscaneoEEG.place(x=135, y=345, height=28, width=135)
        self._view.botonContrasena.place(x=280, y=345, height=28, width=135)

        # Reaparecer opciones de autenticacion por contrasena    
        self._view.campoContrasena.place_forget()
        self._view.etiquetaImagenIngresar.place_forget()
        self._view.etiquetaVolverMetodoIngreso.place_forget()

        # Desbloquear botones de izquierda y derecha
        self.__mostrarUsuarioSeleccionado()
        self.__bloquearBotonesDerechaIzquierda = False

        # Cambiar titulo de la ventana
        self._view.etiquetaDescripcionVentana.config(text='Seleccionar un usuario para acceder')

        # Reestablecer campo de contrasena
        self._view.campoContrasena.delete(0,Tkinter.END)
        self._view.campoContrasena.insert(0,'Contraseña')
        self._view.campoContrasena.config(  
            show='',
            fg=ViewAuxiliar.obtenerColor(124,124,124),
            font="SegoeUI 10 italic"
        ) # End config

        self._view.canvas.focus_set()

    def etiquetaImagenIngresar_Click(self,_):

        if  self._model.autenticar(self.idUsuarioSeleccionado, 
            self._view.campoContrasena.get()):

            if self.hayUsuarioPreseleccionado:
                print('200')
                exit(0)
            else:
                # Crear un nuevo view de perfil y relacionarlo con un controller
                viewIniciado = ViewIniciado()
                controllerIniciado = ControllerIniciado( 
                    viewIniciado, 
                    self._model, 
                    self.idUsuarioSeleccionado
                ) # End construct

                try:
                    self._cerrarVentana()
                except:
                    Tkinter.TclError

                controllerIniciado.inicializarView()

        else:
            MessageBox.showinfo(
                "Error al autenticar",
                "La contraseña especificada es incorrecta"
            ) # End showinfo



    """
    El metodo es invocado cuando se adquiere el foco en el campo de 
    contrasena en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoContrasena_Focus(self,_):
        if self._view.campoContrasena.get() == 'Contraseña':
            self._view.campoContrasena.delete(0,Tkinter.END)
            self._view.campoContrasena.config(  
                show="●",
                fg=View.COLOR_CONTRASTE,
                font="SegoeUI 10 normal"
            ) # End config


    """
    El metodo es invocado cuando se pierde el foco en el campo de
    contrasena en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def campoContrasena_LostFocus(self,_):
        if self._view.campoContrasena.get() == '':
            self._view.campoContrasena.insert(0,'Contraseña')
            self._view.campoContrasena.config(  
                show='',
                fg=ViewAuxiliar.obtenerColor(124,124,124),
                font="SegoeUI 10 italic"
            ) # End config



    def __mostrarUsuarioSeleccionado(self, porIndice=True):

        # Recuperar datos del usuario seleccionado en el model
        datosUsuario = self._model.obtenerDatosUsuario(self.__usuarioSeleccionado, porIndice)

        # Ajustar imagen a tamano del contenedor 
        datosUsuario[5] = datosUsuario[5].resize((147,147))

        # Desplegar imagen en view
        self.renderUsuario = ImageTk.PhotoImage(datosUsuario[5], master= self._view.ventana)
        self._view.etiquetaImagenUsuario.config(image=self.renderUsuario)
        self._view.etiquetaNombreUsuario.config(text=datosUsuario[1])

        # Leer fecha y mostrarla en el view
        fechaRegistro = datosUsuario[3]
        locale.setlocale(locale.LC_TIME, "es_ES") 
        self._view.etiquetaFechaRegistro.config(
            text= 'Registrado el: ' + str(fechaRegistro.strftime("%d de %B de %Y")) 
        ) # End config
        
        # Establecer id del usuario seleccionado
        self.idUsuarioSeleccionado = datosUsuario[0]

        # Alterar la apariencia de los controles de derecha e izquierda
        # dependiendo de si se ha llegado a los limites de la 
        # coleccion de usuarios
        if self.__usuarioSeleccionado > 0:
            self._view.etiquetaImagenIzquierda.config(
                image=self._view.renderIzquierda,
                cursor='hand2'
            ) # End config
        else:
            self._view.etiquetaImagenIzquierda.config(
                image = self._view.renderIzquierdaDesactivado,
                cursor = 'arrow' 
            ) #End config

        if self.__usuarioSeleccionado < self._model.obtenerNumeroUsuarios() - 1:
            self._view.etiquetaImagenDerecha.config(
                image=self._view.renderDerecha,
                cursor='hand2'
            ) 
        else:
            self._view.etiquetaImagenDerecha.config(
                image=self._view.renderDerechaDesactivado,
                cursor = 'arrow' 
            ) # End config

    def botonUsarEscaneoEEG_Click(self, _):

        # Solicitar la confirmacion antes de iniciar
        iniciar = MessageBox.askyesno(title='Iniciar grabación',
                    message='Se iniciará una recopilación de datos EEG\n' +\
                            'Deberá tener su casco conectado antes de iniciar\n'
                            '¿Está seguro de que desea continuar?')

        # Si se ha dado permiso para iniciar
        if iniciar:
            
            viewRecopilador = ViewRecopilador()
            controllerViewRecopilador = ControllerRecopilador( viewRecopilador, self._model, self._view, self )

            # Ocultar la ventana principal para prevenir modificaciones
            self._view.ventana.withdraw()
            
            # Lanzar el recopilador
            thread = Thread(target=controllerViewRecopilador.inicializarView())
            thread.start()

            # Hacer join en los threads 
            # para volver al principal
            thread.join()

            # Tomar una decision dependiendo de los valores de acceso dados
            if self.resultadoRecopilador:

                if self.hayUsuarioPreseleccionado:
                    print('200')
                    exit(0)
                else:

                    # Crear un nuevo view de perfil y relacionarlo con un controller
                    viewIniciado = ViewIniciado()
                    controllerIniciado = ControllerIniciado( 
                        viewIniciado, 
                        self._model, 
                        self.idUsuarioSeleccionado
                    ) # End construct
                    
                    # Cerrar ventana principal
                    self._view.ventana.destroy()
                    self._view.ventana.quit()
                    
                    controllerIniciado.inicializarView()

            else:
                MessageBox.showinfo(
                    "Error al autenticar",
                    "Sus señales no han podido probar su identidad"
                ) # End showinfo
                
                # Restaurar el view principal
                self._view.ventana.deiconify()


    def inicializarView(self):
        self._view.construirView()

        if self.hayUsuarioPreseleccionado:
            self.__mostrarUsuarioSeleccionado(porIndice=False)
            self._view.etiquetaImagenIzquierda.place_forget()
            self._view.etiquetaImagenDerecha.place_forget()
            self._view.etiquetaImagenNuevoUsuario.place_forget()
            self._view.etiquetaDescripcionNuevoUsuario.place_forget()
            self._view.etiquetaDescripcionVentana.config(
                text = "Una aplicación necesita autenticarlo como:"
            ) # End config
        else:
            self.__mostrarUsuarioSeleccionado()
            self._view.etiquetaImagenAbortarInicio.place_forget()
            self._view.etiquetaDescripcionAbortarInicio.place_forget()

        self._view.establecerListeners(self)
        self._view.ventana.mainloop()