import mysql.connector
import io

class Model():

    SEGURIDAD_ALTA = 'maximo' 
    SEGURIDAD_MEDIA = 'intermedio' 
    SEGURIDAD_BAJA = 'reducido' 

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
    def insertarUsuario( self, nombre, contrasena, media, desviacion, 
                        fronteraCorrelacion, fronteraGaussiana, nivelSeguridad, imagen=None):

        # try:

        # Revisar si hay que cargar una imagen 
        if imagen != None:

            bytesImagen = io.BytesIO()
            imagen = imagen.convert("RGB")
            imagen.save(bytesImagen, format='JPEG')
            imagen = bytesImagen.getvalue()


        # Preparar instruccion y tupla
        instruction =   "INSERT INTO USUARIO ( " + \
                        "nombre, contrasena, media, desviacion, " + \
                        "fronteraCorrelacion, fronteraGaussiana, nivelSeguridad, imagen) " + \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        nuevaTupla = (  nombre, contrasena, media, desviacion, 
                        fronteraCorrelacion, fronteraGaussiana, nivelSeguridad, imagen )

        # Ejecutar y hacer commit
        cursor  = self.__connection.cursor()
        cursor.execute( instruction, nuevaTupla )
        self.__connection.commit()

        # Operacion exitosa
        cursor.close()
        return True

        # except:

        #     # Operacion fallida -> rollback
        #     self.__connection.rollback()
        #     cursor.close()
        #     return False

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
