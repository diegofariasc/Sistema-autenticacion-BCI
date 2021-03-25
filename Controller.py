class Controller():

    def __init__(self, view):
        self._view = view 

    def inicializarView(self):
        self._view.construirView()
        self._view.establecerListeners(self)
        self._view.ventana.mainloop()
