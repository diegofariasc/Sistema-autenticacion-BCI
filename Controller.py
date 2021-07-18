class Controller():

    def __init__(self, view, model):
        self._view = view 
        self._model = model

    def inicializarView(self):
        self._view.construirView()
        self._view.establecerListeners(self)
        self._view.ventana.mainloop()


    """
    El metodo permite cerrar la ventana actual y destruir el 
    controller asociado
    Input:  None
    Output: None
    """
    def _cerrarVentana(self):
        self._view.ventana.destroy()
        del self._view
        del self