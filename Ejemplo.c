#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include "AutenticadorEEG.h"

// Definicion de metodos para mostrar interfaz
void imprimirInterfazSeleccionUsuarios();
void imprimirInterfazMetodoAutenticacion(char*);
void imprimirInterfazIngresarClave(char*,bool,unsigned int);
void imprimirInterfazAutenticacion(char*,bool,unsigned int);
void imprimirInterfazRegistros();

// Metodo principal
int main(void)
{

    // Declaracion de variables
    char            seleccion;      // Registrar opcion seleccionada    
    char*           nombreUsuario;  // Nombre del usuario a iniciar
    char*           contrasena;     // Variable para capturar contrasena
    bool            mostrarError;   // Indica si mostrar mensaje de error
    bool            yaAutenticado;  // Indica si se ha autenticado por EEG correctamente
    unsigned int    intentos;       // Contador del numero de intentos
    unsigned int    idUsuario;      // Numero id del usuario en el sistema EEG

    // Definicion de etiqueta para salto
    seleccionarUsuario:

    // Inicializar seleccion en 0
    seleccion = 0;

    // Seguir solicitando hasta que la seleccion sea A o B
    while(seleccion != 'A' && seleccion != 'B')
    {
        // Imprimir interfaz
        system("clear");
        imprimirInterfazSeleccionUsuarios();

        // Solicitar seleccion y obtenerla
        printf("Seleccion: ");
        fflush(stdin);
        seleccion = getc(stdin);

    } // End while


    // Identificar seleccion
    switch (seleccion)
    {
        // Usuario juan
        case 'A':
            nombreUsuario = "Francisco";
            idUsuario = 5;
            break;
        
        // Usuario pedro
        case 'B':
            nombreUsuario = "Juan";
            idUsuario = 6;
            break;
    } // End switch

    // Mostrar interfaz para elegir metodo de autenticacion
    imprimirInterfazMetodoAutenticacion(nombreUsuario);

    // Reiniciar seleccion en 0
    seleccion = 0;

    // Seguir solicitando hasta que la seleccion sea A, B o C
    while(seleccion != 'A' && seleccion != 'B' && seleccion != 'C')
    {
        // Imprimir interfaz
        system("clear");
        imprimirInterfazMetodoAutenticacion(nombreUsuario);

        // Solicitar seleccion y obtenerla
        printf("Seleccion: ");
        fflush(stdin);
        seleccion = getc(stdin);

    } // End while

    // Inicializar variables para mostrar errores
    mostrarError = false;
    intentos = 0;

    // Identificar seleccion de metodo de autenticacion
    switch (seleccion)
    {
        // Por contrasena
        case 'A':

            // Solicitar clave hasta obtener una correcta
            while ( 
                contrasena == NULL || 
                (strcmp(nombreUsuario, "Juan") == 0 && strcmp(contrasena, "abc123") != 0) ||
                (strcmp(nombreUsuario, "Pedro") == 0 && strcmp(contrasena, "password") != 0))
            {

                // Mostrar interfaz para especificar clave
                system("clear");
                imprimirInterfazIngresarClave(nombreUsuario, mostrarError, intentos);

                // Obtener clave
                contrasena = (char*) getpass("Contrasena: ");

                // Establecer un intento mas
                // Solo se mostrara si el intento actual fue fallido
                mostrarError = true;
                intentos++;

            } // End while

            // Acceso concedido. Mostrar datos
            system("clear");
            imprimirInterfazRegistros();

            // Esperar una tecla para terminar el programa
            fflush(stdin);
            getc(stdin);
            return 0;
        
        // Por EEG
        case 'B':

            // Indicar que la autenticacion aun no procede
            yaAutenticado = false;

            // Mantenerse solicitando hasta
            // lograr la autenticacion
            while ( !yaAutenticado )
            {
                // Mostrar en consola interfaz de autenticacion
                system("clear");
                imprimirInterfazAutenticacion(nombreUsuario, mostrarError, intentos);

                // Si hubo error, esperar antes de otro lanzamiento
                // del autenticador EEG
                if (mostrarError)
                    fflush(stdin);
                    getc(stdin);

                // Intentar autenticar
                yaAutenticado = autenticar(idUsuario);

                // Contabilizar un intento
                mostrarError = true;
                intentos++;

            } // End while

            // Acceso concedido. Mostrar datos
            system("clear");
            imprimirInterfazRegistros();

            // Esperar una tecla para terminar el programa
            fflush(stdin);
            getc(stdin);
            return 0;

        // Opcion de cancelar
        case 'C':

            // Regresar a la seleccion de usuario
            goto seleccionarUsuario;
            break;

    } // End switch


} // End main

void imprimirInterfazSeleccionUsuarios()
{
    printf("            ╔═══════════════════════════════╗            \n");
    printf("╔═══════════╣ Sistema de registro de ventas ╠═══════════╗\n");
    printf("║           ╚═══════════════════════════════╝           ║\n");
    printf("║                                                       ║\n");
    printf("║  Iniciar sesion                                       ║\n");
    printf("║                                                       ║\n");
    printf("║  Seleccione un usuario:                               ║\n");
    printf("║  A. Francisco                                         ║\n");
    printf("║  B. Juan                                              ║\n");
    printf("║                                                       ║\n");
    printf("║                                                       ║\n");
    printf("╚═══════════════════════════════════════════════════════╝\n");
    printf("\n");
} // End imprimirInicioSesion

void imprimirInterfazMetodoAutenticacion( char* usuarioSeleccionado )
{
    printf("            ╔═══════════════════════════════╗            \n");
    printf("╔═══════════╣ Sistema de registro de ventas ╠═══════════╗\n");
    printf("║           ╚═══════════════════════════════╝           ║\n");
    printf("║                                                       ║\n");
    printf("║  Iniciar sesion como %-33s║\n",usuarioSeleccionado );
    printf("║                                                       ║\n");
    printf("║  Seleccione un metodo de acceso:                      ║\n");
    printf("║  A. Contrasena                                        ║\n");
    printf("║  B. EEG                                               ║\n");
    printf("║  C. Cancelar                                          ║\n");
    printf("║                                                       ║\n");
    printf("╚═══════════════════════════════════════════════════════╝\n");
    printf("\n");
} // End imprimirInterfazMetodoAutenticacion

void imprimirInterfazIngresarClave(char* usuarioSeleccionado, bool mostrarError, unsigned int intentos )
{
    printf("            ╔═══════════════════════════════╗            \n");
    printf("╔═══════════╣ Sistema de registro de ventas ╠═══════════╗\n");
    printf("║           ╚═══════════════════════════════╝           ║\n");
    printf("║                                                       ║\n");
    printf("║  Especifique la contrasena para %-22s║\n",usuarioSeleccionado );
    printf("║                                                       ║\n");
    mostrarError ? 
    printf("║  [!] Contrasena incorrecta. Intente nuevamente        ║\n"):
    printf("║                                                       ║\n");
    mostrarError ? 
    printf("║  Intentos: %-4d                                       ║\n", intentos):
    printf("║                                                       ║\n");
    printf("║                                                       ║\n");
    printf("║                                                       ║\n");
    printf("║                                                       ║\n");
    printf("╚═══════════════════════════════════════════════════════╝\n");
    printf("\n");
} // End imprimirInicioSesion


void imprimirInterfazAutenticacion(char* usuarioSeleccionado, bool mostrarError, unsigned int intentos )
{
    printf("            ╔═══════════════════════════════╗            \n");
    printf("╔═══════════╣ Sistema de registro de ventas ╠═══════════╗\n");
    printf("║           ╚═══════════════════════════════╝           ║\n");
    printf("║                                                       ║\n");
    printf("║  Ingresando como %-37s║\n",usuarioSeleccionado );
    printf("║                                                       ║\n");
    mostrarError ? 
    printf("║  [!] Acceso rechazado por el sistema EEG              ║\n"):
    printf("║                                                       ║\n");
    mostrarError ? 
    printf("║  Intentos: %-4d                                       ║\n", intentos):
    printf("║                                                       ║\n");
    printf("║                                                       ║\n");
    mostrarError ? 
    printf("║  Presione enter para reintentar...                    ║\n"):
    printf("║                                                       ║\n");
    printf("║                                                       ║\n");
    printf("╚═══════════════════════════════════════════════════════╝\n");
    printf("\n");
} // End imprimirInicioSesion

void imprimirInterfazRegistros()
{


    printf("            ╔═══════════════════════════════╗            \n");
    printf("╔═══════════╣ Sistema de registro de ventas ╠═══════════╗\n");
    printf("║           ╚═══════════════════════════════╝           ║\n");
    printf("║                                                       ║\n");
    printf("║  Registros de ventas:                                 ║\n" );
    printf("║                                                       ║\n");
    printf("║  05 de enero:   $150.00 por Juan                      ║\n");
    printf("║  14 de febrero: $300.00 por Juan                      ║\n");
    printf("║  21 de febrero: $520.00 por Francisco                 ║\n");
    printf("║                                                       ║\n");
    printf("║  Presione enter para salir...                         ║\n");
    printf("║                                                       ║\n");
    printf("╚═══════════════════════════════════════════════════════╝\n");
    printf("\n");
} // End imprimirInicioSesion
