from numpy import median
import abc

class Funciones(metaclass=abc.ABCMeta):
    
    # Median absolute distribution 
    def mad(datos):
        mediana = median(datos)
        return median([abs(x-mediana) for x in datos])
        