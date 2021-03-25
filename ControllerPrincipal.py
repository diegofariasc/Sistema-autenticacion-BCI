from Controller import Controller
from ViewCrearUsuario import ViewCrearUsuario
from ControllerCrearUsuario import ControllerCrearUsuario

class ControllerPrincipal(Controller):

    @staticmethod
    def etiquetaImagenNuevoUsuario_Click(evento):

        # Crear un nuevo view de crear usuario y relacionarlo con un controller
        viewCrearUsuario = ViewCrearUsuario()
        controllerCrearUsuario = ControllerCrearUsuario(viewCrearUsuario)
        controllerCrearUsuario.inicializarView()
