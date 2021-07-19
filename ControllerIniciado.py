from ControllerSelectorSeguridad    import ControllerSelectorSeguridad
from Model                          import Model
from View                           import View
from PIL                            import ImageTk, Image
from tkinter.messagebox             import askquestion, showinfo, showerror

import locale
import tkinter as Tkinter

class ControllerIniciado(ControllerSelectorSeguridad):

    def __init__(self, view, model, id):

        super().__init__(view, model)
        self.__idUsuario = id

        
    def inicializarView(self):

        self._view.construirView()
        
        # Recuperar datos del usuario seleccionado en el model
        datosUsuario = self._model.obtenerDatosUsuario(self.__idUsuario, False)

        # Ajustar imagen a tamano del contenedor 
        datosUsuario[5] = datosUsuario[5].resize((45,45))

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
        
        # Mostrar el nivel de seguridad seleccionado
        if datosUsuario[4] == Model.SEGURIDAD_ALTA:
            super().opcionSeguridadBaja_Click(None)
        elif datosUsuario[4] == Model.SEGURIDAD_MEDIA:
            super().opcionSeguridadMedia_Click(None)
        elif datosUsuario[4] == Model.SEGURIDAD_BAJA:
            super().opcionSeguridadBaja_Click(None)

        self._view.establecerListeners(self)
        self._view.ventana.mainloop()


    def opcionSeguridadBaja_Click(self, evento):
        super().opcionSeguridadBaja_Click(evento)
        self._model.establecerNivelSeguridad(self.__idUsuario, self._seguridadSeleccionada)

    def opcionSeguridadMedia_Click(self, evento):
        super().opcionSeguridadMedia_Click(evento)
        self._model.establecerNivelSeguridad(self.__idUsuario, self._seguridadSeleccionada)

    def opcionSeguridadAlta_Click(self, evento):
        super().opcionSeguridadAlta_Click(evento)
        self._model.establecerNivelSeguridad(self.__idUsuario, self._seguridadSeleccionada)

    def etiquetaImagenEliminarUsuario_Click(self, evento):

        if askquestion (
            'Eliminar perfil',
            '¿Esta seguro que desea eliminar su perfil en el sistema?\n' +
            'Esta accion es irreversible y afectará a todas las aplicaciones' + 
            'que empleen su perfil EEG para autenticarlo',icon = 'warning') == 'yes':

            if self._model.eliminarUsuario(self.__idUsuario):

                showinfo(
                    "Perfil eliminado",
                    "Su perfil de autenticación en el sistema EEG ha sido eliminado con éxito"
                ) # End showinfo
                self.__cerrarSesion()

            else:
                showerror(
                    "Error al eliminar su perfil",
                    "Se ha producido un error desconocido al eliminar su perfil en el sistema"
                ) # End showerror

    def etiquetaImagenCerrarSesion_Click(self, evento):
        self.__cerrarSesion()

    def __cerrarSesion(self):

        from ViewPrincipal          import ViewPrincipal
        from ControllerPrincipal    import ControllerPrincipal

        # Crear un nuevo view de perfil y relacionarlo con un controller
        viewPrincipal = ViewPrincipal()
        controllerPrincipal = ControllerPrincipal( 
            viewPrincipal, 
            self._model
        ) # End construct

        # Transicionar al nuevo view
        try:
            self._cerrarVentana()
        except:
            Tkinter.TclError
        controllerPrincipal.inicializarView()