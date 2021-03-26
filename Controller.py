class Controller():

    def __init__(self, view, model):
        self._view = view 
        self._model = model

    def inicializarView(self):
        self._view.construirView()
        self._view.establecerListeners(self)
        self._view.ventana.mainloop()
