from ViewPrincipal import ViewPrincipal
from ControllerPrincipal import ControllerPrincipal

def main():

    # Construir interfaz principal
    viewPrincipal = ViewPrincipal()

    # Relacionar interfaz principal con el controller e inicializarla
    controllerViewPrincipal = ControllerPrincipal( viewPrincipal )
    controllerViewPrincipal.inicializarView()

main()