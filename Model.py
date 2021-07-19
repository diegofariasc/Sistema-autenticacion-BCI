from pickle import TRUE
from random import randint
import mysql.connector
import io

from PIL            import  Image
from numpy          import  array, transpose, shape, std, \
                            mean, delete, median, add, subtract, \
                            where, logical_and, append, vstack, prod, min
from scipy.signal   import  butter, lfilter
from scipy.stats    import  iqr, pearsonr, norm, median_absolute_deviation as mad

class Model():

    SEGURIDAD_ALTA      = 'maximo' 
    SEGURIDAD_MEDIA     = 'intermedio' 
    SEGURIDAD_BAJA      = 'reducido' 
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
        query = ("SELECT MAX(canal) + 1 from EXPERIMENTO " +\
                "WHERE tipo='%s' AND usuario=%s") % (tipo, usuario)
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

    def procesarSenal(self, senal_C1, senal_C2):

        # Convertir a numpy array y transponer
        # para adquirir la forma estandar de la senal
        senal_C1 = array(senal_C1)
        senal_C2 = array(senal_C2)
        print("Inicial\t\t\t(exp, canales, muestras)\t=> C1:", shape(senal_C1), "\tC2:", shape(senal_C2))
        senalTranspuesta_C1 = transpose(senal_C1, (1, 2, 0))
        senalTranspuesta_C2 = transpose(senal_C2, (1, 2, 0))
        print("Transpuesta\t\t(canales, muestras, exp)\t=> C1:", shape(senalTranspuesta_C1), "\tC2:", shape(senalTranspuesta_C2))

        # Filtrar en las bandas generales
        senalFiltrada_C1 = self.__filtrar(senalTranspuesta_C1, Model.BANDAS_GENERALES_C1)
        senalFiltrada_C2 = self.__filtrar(senalTranspuesta_C2, Model.BANDAS_GENERALES_C2)
        print("Filtrado\t\t(canales, muestras, exp)\t=> C1:", shape(senalFiltrada_C1), "\tC2:", shape(senalFiltrada_C2))

        # Extraer caracteristicas
        caracteristicas_C1 = self.__extraerCaracteristicas(senalFiltrada_C1, Model.FUNCIONES)
        caracteristicas_C2 = self.__extraerCaracteristicas(senalFiltrada_C2, Model.FUNCIONES)
        print("Extraccion\t\t(funciones, canales, exp)\t=> C1:", shape(caracteristicas_C1), "\tC2:", shape(caracteristicas_C2))

        # Remocion de outliers
        sinOutliers_C1 = self.__removerOutliers(caracteristicas_C1, 3.5)
        sinOutliers_C2 = self.__removerOutliers(caracteristicas_C2, 3.5)
        print("Remocion + aplanado\t('caracteristicas', exp)\t=> C1:", shape(sinOutliers_C1), "\t\tC2:", shape(sinOutliers_C2))
        
        return (sinOutliers_C1, sinOutliers_C2)

    def insertarExperimentos(self, experimentos, tipo):

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
                    nuevaTupla = (1, n_exp, n_dim, experimentos[n_dim, n_exp], tipo)
                    cursor.execute( instruction, nuevaTupla )

            # Si se tiene exito lanzar commit
            self.__connection.commit()

            # Operacion exitosa
            cursor.close()
            return True

        except Exception as e:

            # Operacion fallida -> rollback
            print(e)
            self.__connection.rollback()
            cursor.close()
            return False

    def __filtrar (self, datos, frecuencias, Fs=250):

        # Iterar sobre cada frecuencia
        for f_inf, f_sup in frecuencias:
            
            # Diseno del filtro
            b, a = butter(4, [f_inf / (Fs / 2), f_sup / (Fs / 2)], btype='bandpass')
            datos = lfilter(b, a, datos, 1)

        return datos

    def __extraerCaracteristicas (self, datos, funciones, canales=[1,2,3]):
        
        # Extraer cada caracteristica en funciones sobre la segunda dimension
        return array( [[[ 
            funcion( [datos[canal - 1][j][k] 
                for j in range( shape(datos)[1])])
                for k in range( shape(datos)[2])]
                for canal in canales] 
                for funcion in funciones])


    def __removerOutliers (self, datos, desplazamiento):

        # Calcular umbrales de filtrado
        umbrales_sup = add(median(datos, axis=2),mad(datos, axis=2) * desplazamiento)
        umbrales_inf = subtract(median(datos, axis=2),mad(datos, axis=2) * desplazamiento)

        # Iniciar parametros (salida y limites)
        sinOutliers = None
        inicializado = False
        n_funciones, n_canales, _ = shape(datos)

        # Remover 
        for n_funcion in range(n_funciones):
            for n_canal in range(n_canales):
                
                # Extraer valores en la funcion dada y el experimento
                # dado, todos los canales
                valores = datos[n_funcion, n_canal, :]
                umbral_sup = umbrales_sup[n_funcion, n_canal]
                umbral_inf = umbrales_inf[n_funcion, n_canal]

                # Determinar si todos los valores estan en 
                # el ragno comprendido entre los umbrales
                if logical_and(valores >= umbral_inf, valores <= umbral_sup).all():

                    # Ver si el arreglo de retorno i.e., sinOutliers
                    # ya se encuentra inicializado
                    if not inicializado:
                        sinOutliers = valores
                        inicializado = True
                    else:
                        sinOutliers = vstack((sinOutliers, valores))

        return sinOutliers

