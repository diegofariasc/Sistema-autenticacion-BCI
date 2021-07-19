import abc

class Movimiento(metaclass=abc.ABCMeta):
    
    # Constantes de movimientos 
    ESPERA          = 0
    PREPARACION     = 1
    REPOSO          = 2
    MANO_IZQUIERDA  = 3
    MANO_DERECHA    = 4
    PIE_IZQUIERDO   = 5
    PIE_DERECHO     = 6
    FINALIZADO      = 7

    TIPO_C1         = 'mano izquierda'
    TIPO_C2         = 'mano derecha'
    TIPO_C3         = 'pie izquierdo'
    TIPO_C4         = 'pie derecho'