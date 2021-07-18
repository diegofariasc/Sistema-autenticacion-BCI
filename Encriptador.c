#include "Encriptador.h"

void encriptar( const char* origen, const char* salida, unsigned char clave )
{
    FILE * archivoOrigen = fopen(origen, "r");
    FILE * archivoSalida = fopen(salida, "w");
    char caracter;

    // Verificar si alguno de los archivos no se pudieron abrir
    if (archivoOrigen == NULL || archivoSalida == NULL)
    {
        printf("Error al aplicar operacion de encriptacion");
        return;
    } // End if

    // Obtener caracter enesimo
    caracter = fgetc(archivoOrigen);

    // Mientras no se llegue al final de linea
    while(caracter != EOF)
    {
        caracter += clave;
        fputc(caracter, archivoSalida);
        caracter = fgetc(archivoOrigen);

    } // End while

    fclose(archivoOrigen);
    fclose(archivoSalida);

} // End encriptar