from PIL import Image, ImageDraw
import numpy as np

# La clase ofrece metodos auxiliares estaticos 
# para construir interfaces
class ViewAuxiliar:

    @staticmethod
    def obtenerColor(R,G,B):
        return '#%02x%02x%02x' % (R, G, B)

    @staticmethod
    def recortarImagenUsuario(ubicacion, rutaSalida):

        # Abrir imagen 
        imagen = Image.open(ubicacion).convert("RGB")
        dimension1 , dimension2 = imagen.size
        tamano = min(dimension1, dimension2)
        npImage=np.array(imagen)[:tamano,:tamano]

        # Crear imagen circular
        alpha = Image.new('L', (tamano,tamano),0)
        dibujo = ImageDraw.Draw(alpha)
        dibujo.pieslice([0,0,tamano,tamano],0,360,fill=255)

        # Convert alpha Image to numpy array
        npAlpha=np.array(alpha)
        npImage=np.dstack((npImage,npAlpha))

        # Guardar imagen resultante
        Image.fromarray(npImage).save(rutaSalida)