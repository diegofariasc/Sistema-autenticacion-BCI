import mysql.connector
import io
from PIL import Image

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

        try:

            # Revisar si hay que cargar una imagen 
            if imagen != None:

                bytesImagen = io.BytesIO()
                imagen = imagen.convert("RGBA")
                imagen.save(bytesImagen, format='PNG')
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

        except:
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
        if result[9] == None:
            
            # Cargar BLOB de imagen predeterminada
            with open("assets/ViewPrincipal/imagenUsuarioDefault.png", "rb") as image:
                f = image.read()
                b = bytearray(f)
                result[9] = b

        # Convertir BLOB de imagen en objeto PIL Image
        result[9] = Image.open(io.BytesIO(result[9]))

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

