from ViewPrincipal import ViewPrincipal
from ControllerPrincipal import ControllerPrincipal
from Model import Model

def main():

    # Construir interfaz principal
    viewPrincipal = ViewPrincipal()

    # Construir model
    model = Model()

    # Relacionar interfaz principal con el controller y el model e inicializarla
    controllerViewPrincipal = ControllerPrincipal( viewPrincipal,model )
    controllerViewPrincipal.inicializarView()

main()