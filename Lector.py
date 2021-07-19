from brainflow.board_shim   import BoardShim, BrainFlowInputParams
from time                   import sleep
from numpy                  import shape

class Lector:

    # Constantes para diferentes tipos de casco
    CYTON = 0
    SIMULADOR = -1

    """
    Metodo constructor de objetos de clase Lector
    Input:  tipoCasco (int)         : Constante indicando el tipo de casco que se utilizara
            canales (list)          : Lista de los canales requeridos del casco
            fs (int)                : Frecuencia de muestreo
            puerto (str)            : Puerto en que se recopilaran datos
    Output: nuevo Lector
    """
    def __init__(self, tipoCasco, canales, fs = 250, puerto = ""):

        # Validar que si el casco es cyton no se deje el puerto en blanco
        if tipoCasco == Lector.CYTON and puerto == "":
            raise AttributeError("Debe especificar el puerto serial en que se ubica el casco")
        
        # Validar que se haya dado un casco apropiado
        if tipoCasco != Lector.CYTON and tipoCasco != Lector.SIMULADOR:
            raise AttributeError("El casco especificado no es valido")

        # Restar 1 a cada numero de canal para poder expresarlos 
        # sin iniciar en 0 fuera de la clase 
        self.__canales = [numero -1 for numero in canales]

        # Construccion y establecimiento de parametros
        BoardShim.disable_board_logger()                        # Desactivar log de BrainFlow
        self.__parametros = BrainFlowInputParams()              # Construir objeto de parametros de BrainFlow
        self.__parametros.serial_port = puerto                  # Establecer puerto
        self.__fs = fs                                          # Establecer frecuencia de muestreo
        self.__casco = BoardShim(tipoCasco, self.__parametros)  # Generar instancia del casco


    """
    El metodo permite ejecutar un experimento de una determinada duracion
    mientras se recopilan los datos EEG. Al terminar, se devuelve la informacion recopilada
    Input:  duracion (int)              : Numero de segundos que dura el experimento
            callbackIniciar (function)  : Funcion anonima llamada en cuanto se inicia el experimento (opcional)
    Output: numpy array                 : Datos recopilados
    """
    def recopilarDatosExperimento(self, duracion, segundosRemover=1, callbackIniciar = lambda :True ):

        # Preparar e iniciar lectura
        self.__casco.prepare_session()              # Preparar sesion 
        self.__casco.start_stream()                 # Iniciar flujo de los datos
        callbackIniciar()                           # Llamar la funcion del usuario e.g. cambiar interfaz
        sleep(duracion + 1)                         # Detener ejecucion hasta n segundos para recopilar

        # Lectura finalizada, leer datos
        datos = self.__casco.get_board_data()       # Obtener la totalidad de datos y sacarlos del buffer
        self.__casco.stop_stream()                  # Frenar flujo
        self.__casco.release_session()              # Liberar sesion

        # Devolver datos de acuerdo a fs y canales
        return datos[self.__canales, (self.__fs * segundosRemover) : self.__fs * duracion - (self.__fs * segundosRemover)]



# # Prueba de la clase con exp de 2 segundos
# # con canales 1-3
# def main():

#     lector = Lector(Lector.SIMULADOR, [1,2,3], puerto="")
#     datos = lector.recopilarDatosExperimento(5)
#     print("Forma:", shape(datos))
#     print(datos)

# if __name__ == "__main__":
#     main()