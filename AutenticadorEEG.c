#include "AutenticadorEEG.h"

#define ACCION_AUTENTICAR       0
#define ACCION_LANZAR_INTERFAZ  1

bool autenticar( unsigned int id )
{
    // Variables
    char    mensaje[4];
    char    comando[512];
    char    stringId[10];
    short   codigo;
    FILE*   tuberia;

    // Agregar id de autenticacion al comando
    // del lanzador
    strncpy(comando, "./lanzador aut ", 512);
    sprintf(stringId, "%d", id);
    strcat(comando,stringId);

    // Invocacion por pipe de la interfaz
    tuberia = popen( comando , "r");

    // Recuperar mensaje
    fgets( mensaje , sizeof( mensaje ), tuberia );
    pclose(tuberia);

    // Traducir a entero
    codigo = atoi(mensaje);

    // Retorno segun salida
    if (codigo == 200)
        return true;
    else
        return false;

} // End autenticar



