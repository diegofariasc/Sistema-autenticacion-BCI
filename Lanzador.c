#include<stdio.h>
#include <string.h>
#include "Encriptador.h"

int main(int argc, char *argv[])
{

    // Declaracion de variables
    char    comando[512];
    char    mensaje[4];
    FILE*   tuberia;

    // Proceso de desencriptado
    encriptar("Main.py","Main.crypt",7);  
    encriptar("Main.crypt","Main.decrypt",-7);    

    // Invocacion por pipe de la interfaz
    if (argc == 3)
    {
        strncpy(comando,"python3 Main.decrypt ", 512);
        strcat(comando, argv[1]);
        strcat(comando, " ");
        strcat(comando, argv[2]);
        tuberia = popen(comando, "r");
        
    } // End if
    else
    {
        tuberia = popen("python3 Main.decrypt", "r");
    } // End else
        

    // Recuperar mensaje
    fgets( mensaje , sizeof( mensaje ), tuberia );
    printf("%s",mensaje);
    pclose(tuberia);

    return 0;


} // End main