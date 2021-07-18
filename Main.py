from ViewPrincipal import ViewPrincipal
from ControllerPrincipal import ControllerPrincipal
from Model import Model
from os import remove, path
import sys

def main():

    # Eliminar el codigo fuente una vez en memoria
    # remove(path.basename(__file__))

    # Construir interfaz principal
    viewPrincipal = ViewPrincipal()

    # Construir model
    model = Model()

    # Relacionar interfaz principal con el controller y el model e inicializarla
    if len(sys.argv) == 3 and sys.argv[1] == 'aut':
        
        # Si el view debe tener un usuario seleccionado de antemano
        controllerViewPrincipal = ControllerPrincipal( viewPrincipal,model, seleccionado=int(sys.argv[2]) )
    else:
        controllerViewPrincipal = ControllerPrincipal( viewPrincipal,model)

    controllerViewPrincipal.inicializarView()

main()