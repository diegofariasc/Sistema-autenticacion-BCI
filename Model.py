import mysql.connector
import io

from PIL            import Image
from numpy          import array, transpose, shape, std, mean
from scipy.signal   import butter, lfilter

class Model():

    SEGURIDAD_ALTA      = 'maximo' 
    SEGURIDAD_MEDIA     = 'intermedio' 
    SEGURIDAD_BAJA      = 'reducido' 
    BANDAS_GENERALES_C1 = [(36, 43), (4,8), (23, 35), (20, 23), (18, 22)]
    BANDAS_GENERALES_C2 = [(36, 43), (4,8), (23, 35), (20, 23), (18, 22)]
    FUNCIONES           = [std, mean]

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
            print(e)
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
        print("C1:", shape(senal_C1), "C2:", shape(senal_C2))
        senalTranspuesta_C1 = transpose(senal_C1, (1, 2, 0))
        senalTranspuesta_C2 = transpose(senal_C2, (1, 2, 0))
        print("C1:", shape(senalTranspuesta_C1), "C2:", shape(senalTranspuesta_C2))

        # Filtrar en las bandas generales
        senalFiltrada_C1 = self.__filtrar(senalTranspuesta_C1, Model.BANDAS_GENERALES_C1)
        senalFiltrada_C2 = self.__filtrar(senalTranspuesta_C2, Model.BANDAS_GENERALES_C2)
        print("C1:", shape(senalFiltrada_C1), "C2:", shape(senalFiltrada_C2))

        # Extraer caracteristicas
        caracteristicas_C1 = self.__extraerCaracteristicas(senalFiltrada_C1, Model.FUNCIONES)
        caracteristicas_C2 = self.__extraerCaracteristicas(senalFiltrada_C2, Model.FUNCIONES)
        print("C1:", shape(caracteristicas_C1), "C2:", shape(caracteristicas_C2))
        

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
                for canal in canales] for funcion in funciones])