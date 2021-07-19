import abc

metaclass=abc.ABCMeta
class Movimiento:
    
    # Constantes de movimientos 
    ESPERA          = 0
    PREPARACION     = 1
    REPOSO          = 2
    MANO_IZQUIERDA  = 3
    MANO_DERECHA    = 4
    PIE_IZQUIERDO   = 5
    PIE_DERECHO     = 6
    FINALIZADO      = 7