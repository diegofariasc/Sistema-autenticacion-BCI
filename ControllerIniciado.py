from ViewIniciado import ViewIniciado

SEGURIDAD_BAJA = 0
SEGURIDAD_MEDIA = 1
SEGURIDAD_ALTA = 2

# La clase representa el controlador de la vista cuando el usuario ha accedido
class ViewIniciado():

    def __init__(vista):
        self.__view = vista

    @staticmethod
    def seleccionarSeguridad(nivel):

        if nivel == SEGURIDAD_BAJA:
            print()
