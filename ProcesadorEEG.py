from mne.io     import  read_raw_gdf
from warnings   import  filterwarnings
from numpy      import  mean, std, shape, array, append, transpose

class ProcesadorEEG():

    """
    El metodo carga un archivo GDF empleando la libreria mne
    Input:  nombreArchivo = Nombre del GDF a cargar
    Output: archivo crudo GDF cargado
    """
    @staticmethod
    def __cargarGDFcrudo( nombreArchivo ):
        
        # Suprimir alertas de la libreria MNE
        filterwarnings("ignore", category=Warning)
        return read_raw_gdf( nombreArchivo , preload=True, verbose='ERROR')

    @staticmethod
    def cargarGDFMultiplesSesiones( ubicaciones ):
        return [ ProcesadorEEG.__cargarGDFcrudo( ubicacion ) for ubicacion in ubicaciones ]

    """
    El metodo invierte las llaves y valores de un diccionario
    Input:  diccionario (dict)
    Output: diccionario con llaves y valores revertidos 
    """
    @staticmethod
    def __invertirDiccionario( diccionario ):
        return { valor: llave for llave, valor in diccionario.items() }

    """
    El metodo extrae los experimentos de una senal cruda continua
    Nota: Se asume que los datos siguen la codificacion del dataset 2b
    Nota: Se usa el diccionario de codificacion para mantener coherencia con
    el documento anexo a la base de datos, aunque es innecesario. 
    """
    @staticmethod
    def __extraerExperimentos ( senal, puntosCorte, codificacionCorte, tiempo, Fs = 250,
                              duracionTotalExperimento = 4.5):

        # Calcular muestras a desplazar a la izquierda
        # El documento indica que la duracion de un experimento es 4.5 seg
        desplazamientoTiempo = int ( ( duracionTotalExperimento - tiempo ) / 2 ) * Fs

        # Indicador para rechazar proximo experimento
        rechazar    = False

        # Almacenar muestras recortadas
        muestras_C1 = []
        muestras_C2 = []

        # Recorrer puntos de corte
        for puntoCorte in puntosCorte:

            # Sustraer datos del punto de corte
            muestra, _, codigo = puntoCorte

            # En caso de encontrar un codigo de flecha a la izquierda
            if codificacionCorte[ codigo ] == '769':
                if not rechazar:
                    muestras_C1.append( senal[ : , muestra + desplazamientoTiempo : muestra + desplazamientoTiempo + int(tiempo * Fs) ] )
                rechazar = False

            # En caso de encontrar un codigo de flecha a la izquierda
            if codificacionCorte[ codigo ] == '770':
                if not rechazar:
                    muestras_C2.append( senal[ : , muestra + desplazamientoTiempo : muestra + desplazamientoTiempo + int(tiempo * Fs) ] )
                rechazar = False

            # En caso de encontrar un codigo de Reject
            # Notificar a la siguiente iteracion para evitar su agregacion
            elif codificacionCorte[ codigo ] == '1023':
                rechazar = True

        # Convertir a np arrays
        muestras_C1 = array(muestras_C1)
        muestras_C2 = array(muestras_C2)

        muestras_C1 = transpose(muestras_C1, (1, 2, 0))
        muestras_C2 = transpose(muestras_C2, (1, 2, 0))

        # Los datos estan en forma ( muestra, canal, experimento )
        # Transponer al orden convencional ( canal, muestra, experimento )
        return ( muestras_C1, muestras_C2 )