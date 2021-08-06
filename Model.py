from math import sin
from pickle import TRUE
from random import randint, shuffle
import mysql.connector
import io

from PIL            import  Image
from numpy          import  array, transpose, shape, std, \
                            mean, delete, median, add, subtract, \
                            where, logical_and, append, vstack, \
                            prod, min, reshape
from numpy.random   import  rand
from scipy.signal   import  butter, lfilter
from scipy.stats    import  iqr, pearsonr, norm, median_absolute_deviation as mad

class Model():

    SEGURIDAD_ALTA      = 'maximo' 
    SEGURIDAD_MEDIA     = 'intermedio' 
    SEGURIDAD_BAJA      = 'reducido' 
    CASOS_APROBAR       = {'reducido' : 1, 'intermedio' : 3, 'maximo' : 5}
    BANDAS_GENERALES_C1 = [(36, 43), (4,8), (23, 35), (20, 23), (18, 22)]
    BANDAS_GENERALES_C2 = [(36, 43), (4,8), (23, 35), (20, 23), (18, 22)]
    FUNCIONES           = [std, mad, iqr]


    # Constructor
    def __init__( self ):

        # Establecer conexion con la BD 
        self.__connection = mysql.connector.connect(    
            user="root", 
            password="password", 
            host="127.0.0.1",
            database="AutenticadorEEG" 
        ) # End connect


    """
    El metodo permite insertar un usuario en la base de datos
    Input:  nombre, contrasena, media, desviacion, nivelSeguridad, imagen
            con los datos del usuario a insertar
    Output: bool indicando si el proceso se desarrollo sin fallos
    """
    def insertarUsuario( self, nombre, contrasena, nivelSeguridad, imagen=None):

        try:

            # Revisar si hay que cargar una imagen 
            if imagen != None:

                bytesImagen = io.BytesIO()
                imagen = imagen.convert("RGBA")
                imagen.save(bytesImagen, format='PNG')
                imagen = bytesImagen.getvalue()


            # Preparar instruccion y tupla
            instruction =   "INSERT INTO USUARIO (nombre, contrasena, nivelSeguridad, imagen) " + \
                            "VALUES (%s, %s, %s, %s)"
            nuevaTupla = ( nombre, contrasena, nivelSeguridad, imagen )

            # Ejecutar y hacer commit
            cursor  = self.__connection.cursor()
            cursor.execute( instruction, nuevaTupla )
            self.__connection.commit()

            # Operacion exitosa
            cursor.close()
            return True

        except Exception as e:

            # Operacion fallida -> rollback
            self.__connection.rollback()
            cursor.close()
            return False


    """
    El metodo permite modificar el nivel de seguridad
    de un usuario en la base de datos
    Input:  id - identificador del usuario
            nivelSeguridad - constante indicando el nivel de seguridad
    Output: bool indicando si el proceso se desarrollo sin fallos
    """
    def establecerNivelSeguridad( self, id, nivelSeguridad):

        try:

            # Preparar instruccion y tupla
            instruction =   ("UPDATE USUARIO SET nivelSeguridad = '%s' " + \
                            "WHERE id = %s") % (nivelSeguridad,id)

            # Ejecutar y hacer commit
            cursor  = self.__connection.cursor()
            cursor.execute( instruction )
            self.__connection.commit()

            # Operacion exitosa
            cursor.close()
            return True

        except:
            # Operacion fallida -> rollback
            self.__connection.rollback()
            cursor.close()
            return False

    """
    El metodo permite eliminar un usuario de la base de datos
    Input:  id - identificador del usuario
    Output: bool indicando si el proceso se desarrollo sin fallos
    """
    def eliminarUsuario( self, id ):

        try:

            # Preparar instruccion y tupla
            instruction =   ("DELETE FROM USUARIO WHERE id = %s") % (id)

            # Ejecutar y hacer commit
            cursor  = self.__connection.cursor()
            cursor.execute( instruction )
            self.__connection.commit()

            # Operacion exitosa
            cursor.close()
            return True

        except:
            # Operacion fallida -> rollback
            self.__connection.rollback()
            cursor.close()
            return False

    """
    El metodo permite recuperar el numero de usuarios
    registrados en el sistema
    Input:  None
    Output: int con el numero de usuarios en la BD
    """
    def obtenerNumeroUsuarios(self):

        # Preparar query con count
        cursor = self.__connection.cursor()
        query = "SELECT COUNT(*) FROM USUARIO"

        # Lanzarla y devolver resultado
        cursor.execute( query )
        result = cursor.fetchall()

        return result[0][0]

    """
    El metodo permite recuperar el numero de usuarios
    registrados en el sistema
    Input:  None
    Output: int con el numero de usuarios en la BD
    """
    def obtenerExperimentos(self, usuario, tipo):

        # Recuperar el numero de dimensiones
        cursor = self.__connection.cursor()
        query = "SELECT MAX(canal) + 1 FROM EXPERIMENTO " +\
                "WHERE tipo LIKE '%" + tipo + "%' AND usuario=" + str(usuario)

        cursor.execute( query )
        n_dimensiones = cursor.fetchall()[0][0]

        # Arreglo para almacenar el contenido de todas 
        # las dimensiones
        resultado = []

        # Obtener cada dimension (canal)
        for n_dim in range(n_dimensiones):

            cursor = self.__connection.cursor()
            query = ("SELECT valor from EXPERIMENTO " +\
                    "WHERE tipo='%s' AND " +\
                    "usuario=%s AND canal=%s " +\
                    "ORDER BY numeroExperimento ASC") % (tipo, usuario, n_dim)

            # Lanzarla y devolver resultado
            cursor.execute( query )
            dimension = array(cursor.fetchall()).flatten()
            resultado.append(dimension)

        return array(resultado)
            
    def obtenerParametrosAutenticacion(self, datos):
        
        # Calcular medias y desviaciones para cada dimension
        medias = mean(datos, axis=1)
        desviaciones = std(datos, axis=1)

        # Extraer el numero de dimensiones y experimentos
        n_dimensiones, n_experimentos = shape(datos)

        # Calcular las alturas de la curva dado cada elemento
        # en el conjunto de datos como x
        alturas = array([[norm.pdf(datos[n_dim,n_exp], medias[n_dim], desviaciones[n_dim])
                        for n_exp in range(n_experimentos)] 
                        for n_dim in range(n_dimensiones)])

        # Multiplicar las probabilidades sobre el eje 0 i.e., todas 
        # las dimensiones del vector caracteristico y finalmente obtener el menor
        # para obtener la frontera de la curva gaussiana
        frontera_alt = min(prod(alturas, axis=0))

        # Obtener las correlaciones entre cada vector de entrenamiento y el medio,
        # despues buscar el menor para obtener la frontera de correlacion
        correlaciones = array([pearsonr(datos[:,n_exp], medias)[0] 
                            for n_exp in range(n_experimentos)])
        frontera_correl = min(correlaciones)

        # Devolver medias, desviaciones y fronteras
        return (medias, desviaciones, frontera_alt, frontera_correl)

    def obtenerAprobados(self, parametros, datos):

        # Desempaquetar parametros
        medias, desviaciones, frontera_alt, frontera_correl = parametros

        # Extraer el numero de dimensiones y experimentos
        n_dimensiones, n_experimentos = shape(datos)

        # Calcular las alturas contra los valores de entrenamiento 
        alturas = prod(array([[norm.pdf(datos[n_dim,n_exp], medias[n_dim], desviaciones[n_dim])
                    for n_exp in range(n_experimentos)] 
                    for n_dim in range(n_dimensiones)]), axis=0)
        correlaciones = array([pearsonr(datos[:,n_exp], medias)[0] 
                            for n_exp in range(n_experimentos)])

        # Usando fronteras y datos de clasificacion contabilizar cuantos 
        # experimentos se aprueban
        resultadosAprobacion = [altura >= frontera_alt and correl >= frontera_correl 
                                for altura, correl in zip(alturas, correlaciones)]

        return resultadosAprobacion

    def determinarEstadoAutenticacion(self, usuario, resultados_C1, resultados_C2):

        # Recuperar el numero de casos necesarios para aprobar
        # segun el perfil de seguridad del usuario
        cursor = self.__connection.cursor()
        query = ("SELECT nivelSeguridad FROM USUARIO WHERE id=%s") % (usuario)
        cursor.execute( query )
        nivelSeguridad = cursor.fetchall()[0][0]
        casosNecesarios = Model.CASOS_APROBAR[nivelSeguridad]

        # Calcular cuantos casos se han pasado
        casosAprobados = len([True for resultado_C1, resultado_C2 in zip(resultados_C1, resultados_C2) 
                            if resultado_C1 and resultado_C2])
        
        # Determinar si pasa dependiendo de si cumplio
        # con los casos necesarios
        return casosAprobados >= casosNecesarios


    def obtenerDatosUsuario(self, id, buscarPorPosicion):

        # Inicializar variables
        result = None
        cursor = self.__connection.cursor()

        # Determinar si el usuario se recuperara
        # por su indice o por su id
        if buscarPorPosicion:

            # Preparar query
            query = ("SELECT * FROM USUARIO ORDER BY id")

            # Lanzarla y devolver resultado
            cursor.execute( query )
            result = cursor.fetchall()[id]

        else:

            # Preparar query
            query = ("SELECT * FROM USUARIO WHERE id = %s") % (id)

            # Lanzarla y devolver resultado
            cursor.execute( query )
            result = cursor.fetchall()[0]

        # Convertir tupla en lista para editarla
        result = list(result)

        # Verificar si el usuario no tiene imagen
        if result[5] == None:
            
            # Cargar BLOB de imagen predeterminada
            with open("assets/ViewPrincipal/imagenUsuarioDefault.png", "rb") as image:
                f = image.read()
                b = bytearray(f)
                result[5] = b

        # Convertir BLOB de imagen en objeto PIL Image
        result[5] = Image.open(io.BytesIO(result[5]))

        return result

    def autenticar(self, id, contrasena):

        # Preparar query
        cursor = self.__connection.cursor()
        query = ("SELECT * FROM USUARIO WHERE id = %s AND contrasena = '%s'") % \
                (id, contrasena)

        # Lanzarla y devolver resultado
        cursor.execute( query )
        result = cursor.fetchall()
        return len(result) == 1

    def procesarSenal(self, senal_C1, senal_C2, exp_conservar):

        # Convertir a numpy array y transponer
        # para adquirir la forma estandar de la senal
        senal_C1 = array(senal_C1)
        senal_C2 = array(senal_C2)

        print("Inicial\t\t\t(exp, canales, muestras)\t\t=> C1:", shape(senal_C1), "\tC2:", shape(senal_C2))
        senalTranspuesta_C1 = transpose(senal_C1, (1, 2, 0))
        senalTranspuesta_C2 = transpose(senal_C2, (1, 2, 0))
        print("Transpuesta\t\t(canales, muestras, exp)\t\t=> C1:", shape(senalTranspuesta_C1), "\tC2:", shape(senalTranspuesta_C2))

        # Filtrar en las bandas generales
        senalFiltrada_C1 = self.__filtrar(senalTranspuesta_C1, Model.BANDAS_GENERALES_C1)
        senalFiltrada_C2 = self.__filtrar(senalTranspuesta_C2, Model.BANDAS_GENERALES_C2)
        print("Filtrado\t\t(bandas, canales, muestras, exp)\t=> C1:", shape(senalFiltrada_C1), "\tC2:", shape(senalFiltrada_C2))

        # Extraer caracteristicas
        caracteristicas_C1 = self.__extraerCaracteristicas(senalFiltrada_C1, Model.FUNCIONES)
        caracteristicas_C2 = self.__extraerCaracteristicas(senalFiltrada_C2, Model.FUNCIONES)
        print("Extraccion\t\t(funciones, bandas canales, exp)\t=> C1:", shape(caracteristicas_C1), "\tC2:", shape(caracteristicas_C2))

        # Remocion de outliers
        sinOutliers_C1 = self.__removerOutliers(caracteristicas_C1, 3.5, exp_conservar)
        sinOutliers_C2 = self.__removerOutliers(caracteristicas_C2, 3.5, exp_conservar)
        print("Remocion\t\t(funciones, bandas, canales, exp)\t=> C1:", shape(sinOutliers_C1), "\tC2:", shape(sinOutliers_C2))
        
        # Aplanado de datos
        aplanados_C1 = self.__aplanarDatos(sinOutliers_C1)
        aplanados_C2 = self.__aplanarDatos(sinOutliers_C2)
        print("Aplanado\t\t('caracteristicas', exp)\t\t=> C1:", shape(aplanados_C1), "\t\tC2:", shape(aplanados_C2))
        
        return (aplanados_C1, aplanados_C2)

    def obtenerUltimoUsuarioInsertado(self):

        # Obtener el numero de usuario agregado
        cursor = self.__connection.cursor()
        query = "SELECT MAX(id) FROM USUARIO"
        cursor.execute( query )
        return cursor.fetchall()[0][0]

    def obtenerMuestrasDisponibles(self, usuario):

        # Obtener el numero de usuario agregado
        cursor = self.__connection.cursor()
        query = "SELECT sesionesRegistradas FROM USUARIO WHERE id=%s" % usuario
        cursor.execute( query )
        return cursor.fetchall()[0][0]

    def obtenerCalidadSenales(self, usuario):

        datos = self.obtenerExperimentos(usuario,'')

        # Calcular medias para cada dimension
        medias = mean(datos, axis=1)

        # Extraer el numero de dimensiones y experimentos
        _, n_experimentos = shape(datos)

        correlaciones = array([pearsonr(datos[:,n_exp], medias)[0] 
                            for n_exp in range(n_experimentos)])
        return mean(correlaciones)

    def notificarGrabacionSesion(self, usuario):

        # Crear cursor
        cursor = self.__connection.cursor()

        try:
            # Indicar que se ha realizado una nueva recopilacion
            instruction =   "UPDATE USUARIO SET sesionesRegistradas=sesionesRegistradas + 1 " + \
                            "WHERE id =%s" % usuario
            cursor.execute( instruction )
            
            # Si se tiene exito lanzar commit
            self.__connection.commit()
            cursor.close()

        except Exception as e:

            # Operacion fallida -> rollback
            self.__connection.rollback()
            cursor.close()
            return False

    def insertarExperimentos(self, experimentos, tipo, usuario):

        # Obtener el numero maximo de experimentos insertados
        cursor = self.__connection.cursor()
        query = ("SELECT IFNULL(MAX(numeroExperimento) + 1,0)  FROM EXPERIMENTO " +\
                "WHERE usuario=%s AND tipo='%s'") % (usuario, tipo)
        cursor.execute( query )
        offset_exp = cursor.fetchall()[0][0]

        try:
            # Obtener un cursor
            cursor  = self.__connection.cursor()

            # Iterar sobre la estructura
            n_dimensiones, n_experimentos= shape(experimentos)
            for n_exp in range(n_experimentos):
                for n_dim in range(n_dimensiones):

                    # Preparar instruccion y tupla
                    instruction =   "INSERT INTO EXPERIMENTO (usuario, numeroExperimento, canal, valor, tipo) " + \
                                    "VALUES (%s, %s, %s, %s, %s)"
                    nuevaTupla = (usuario, n_exp + offset_exp, n_dim, experimentos[n_dim, n_exp], tipo)
                    cursor.execute( instruction, nuevaTupla )

            # Si se tiene exito lanzar commit
            self.__connection.commit()

            # Operacion exitosa
            cursor.close()
            return True

        except Exception as e:

            # Operacion fallida -> rollback
            self.__connection.rollback()
            cursor.close()
            return False

    def __filtrar (self, datos, frecuencias, Fs=250):

        # Inicializar arreglo con los datos filtrados
        datosFiltrados = []

        # Iterar sobre cada frecuencia
        for f_inf, f_sup in frecuencias:
            
            # Diseno del filtro
            b, a = butter(4, [f_inf / (Fs / 2), f_sup / (Fs / 2)], btype='bandpass')
            datosFiltrados.append(lfilter(b, a, datos, 1))

        return array(datosFiltrados)

    def __extraerCaracteristicas (self, datos, funciones):
        
        # Extraer cada caracteristica en funciones sobre la segunda dimension
        return array([funcion(datos, axis=2) for funcion in funciones])

    def __removerOutliers (self, datos, desplazamiento, exp_conservar):
        
        # Obtener la cantidad de funciones
        n_funciones, _, _, n_experimentos = shape(datos)

        # Establecer set de indices de experimentos a remover
        indicesRemover = set([])

        for n_funcion in range(n_funciones):
            indicesRemover = indicesRemover.union(
                self.__obtenerIndicesRemoverBandas(datos[n_funcion,:,:,:],desplazamiento)
            ) # End union

        # Si se remueven mas datos de los necesarios
        # minimizar el impacto del removedor
        indicesRemover = list(indicesRemover)
        shuffle(indicesRemover)
        indicesRemover = indicesRemover[:n_experimentos-exp_conservar]

        # Ya que se tiene el set de todos los indices a remover
        # suprimirlos
        return delete(datos,indicesRemover,axis=3)


    def __obtenerIndicesRemoverBandas(self, datos, desplazamiento):
        
        # Obtener la cantidad de bandas
        n_bandas, _, _ = shape(datos)

        # Establecer set de indices de experimentos a remover
        indicesRemover = set([])

        # Iterar sobre cada banda, identificando por cada una los indices
        # que se deben de suprimir
        for n_banda in range(n_bandas):
            indicesRemover = indicesRemover.union(
                self.__obtenerIndicesRemoverCanal(datos[n_banda,:,:],desplazamiento)
            ) # End union
        
        return indicesRemover

    """
    Input:  datos (canales, experimentos)
    """
    def __obtenerIndicesRemoverCanal(self, datos, desplazamiento):

        # Obtener la cantidad de datos
        n_canales, n_experimentos = shape(datos)

        # Calcular umbrales de filtrado
        umbrales_sup = add(median(datos, axis=1),mad(datos, axis=1) * desplazamiento)
        umbrales_inf = subtract(median(datos, axis=1),mad(datos, axis=1) * desplazamiento)

        # Obtener los indices de los experimentos en que al menos un canal
        # se sale de los umbrales
        return set([n_exp for n_exp in range(n_experimentos) for n_canal in range(n_canales) 
                    if  datos[n_canal][n_exp] < umbrales_inf[n_canal] or   
                        datos[n_canal][n_exp] > umbrales_sup[n_canal] ])
                
    def __aplanarDatos(self, datos):

        # Obtener la forma actual de los datos
        n_funciones, n_bandas, n_canales, n_experimentos = shape(datos)
        n_dimensiones = n_funciones * n_bandas * n_canales

        # Redimensionarlos para compactar las 3 primeras dimensiones
        return reshape(datos, (n_dimensiones, n_experimentos))
