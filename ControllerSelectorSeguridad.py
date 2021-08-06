from Controller import Controller   
from Model      import Model
from View       import View

class ControllerSelectorSeguridad(Controller):

    # Variables estaticas para identificar
    # las opciones de seguridad en el view 
    SEGURIDAD_BAJA = 75
    SEGURIDAD_MEDIA = 215
    SEGURIDAD_ALTA = 355   

    def __init__(self, view, model):
        super().__init__(view,model)
        self._seguridadSeleccionada = Model.SEGURIDAD_MEDIA

    """
    El metodo es invocado cuando se hace clic en cualquier elemento
    que constituye la opcion de seguridad alta en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def opcionSeguridadAlta_Click(self, _):

        # Revisar en que opcion de seguridad se encuentra posicionado el usuario
        opcionSeleccionada = self._view.canvas.coords(self._view.selector)[0]

        # Establecer la nueva seleccion en la seguridad alta
        self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_ALTA, True)

        # Revisar la opcion de seguridad seleccionada y deseleccionarla
        if opcionSeleccionada == ControllerSelectorSeguridad.SEGURIDAD_MEDIA:
            self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_MEDIA, False)
            self._view.canvas.move(self._view.selector, 140,0)

        if opcionSeleccionada == ControllerSelectorSeguridad.SEGURIDAD_BAJA:
            self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_BAJA, False)
            self._view.canvas.move(self._view.selector, 280,0)

        self._seguridadSeleccionada = Model.SEGURIDAD_ALTA
    
    """
    El metodo es invocado cuando se hace clic en cualquier elemento
    que constituye la opcion de seguridad media en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def opcionSeguridadMedia_Click(self, _):

        # Revisar en que opcion de seguridad se encuentra posicionado el usuario
        opcionSeleccionada = self._view.canvas.coords(self._view.selector)[0]

        # Establecer la nueva seleccion en la seguridad media
        self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_MEDIA, True)

        # Revisar la opcion de seguridad seleccionada y deseleccionarla
        if opcionSeleccionada == ControllerSelectorSeguridad.SEGURIDAD_BAJA:
            self._view.canvas.move(self._view.selector, 140,0)
            self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_BAJA, False)

        if opcionSeleccionada == ControllerSelectorSeguridad.SEGURIDAD_ALTA:
            self._view.canvas.move(self._view.selector, -140,0)
            self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_ALTA, False)

        self._seguridadSeleccionada = Model.SEGURIDAD_MEDIA

    """
    El metodo es invocado cuando se hace clic en cualquier elemento
    que constituye la opcion de seguridad baja en el view
    Input:  evento - con la descripcion del evento que la invoco
    Output: None
    """
    def opcionSeguridadBaja_Click(self, _):

        # Revisar en que opcion de seguridad se encuentra posicionado el usuario
        opcionSeleccionada = self._view.canvas.coords(self._view.selector)[0]

        # Establecer la nueva seleccion en la seguridad baja
        self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_BAJA, True)

        # Revisar la opcion de seguridad seleccionada y deseleccionarla
        if opcionSeleccionada == ControllerSelectorSeguridad.SEGURIDAD_MEDIA:
            self._view.canvas.move(self._view.selector, -140,0)
            self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_MEDIA, False)

        if opcionSeleccionada == ControllerSelectorSeguridad.SEGURIDAD_ALTA:
            self._view.canvas.move(self._view.selector, -280,0)
            self.__cambiarSeleccionOpcion(ControllerSelectorSeguridad.SEGURIDAD_ALTA, False)
    
        self._seguridadSeleccionada = Model.SEGURIDAD_BAJA

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
        if opcion == ControllerSelectorSeguridad.SEGURIDAD_ALTA:
            self._view.etiquetaImagenSeguridadAlta.config( bg = color )
            self._view.etiquetaTituloSeguridadAlta.config( bg = color )
            self._view.etiquetaDescripcionSeguridadAlta.config( bg = color )

        elif opcion == ControllerSelectorSeguridad.SEGURIDAD_MEDIA:
            self._view.etiquetaImagenSeguridadMedia.config( bg = color )
            self._view.etiquetaTituloSeguridadMedia.config( bg = color )
            self._view.etiquetaDescripcionSeguridadMedia.config( bg = color )

        elif opcion == ControllerSelectorSeguridad.SEGURIDAD_BAJA:
            self._view.etiquetaImagenSeguridadBaja.config( bg = color )
            self._view.etiquetaTituloSeguridadBaja.config( bg = color )
            self._view.etiquetaDescripcionSeguridadBaja.config( bg = color )
        