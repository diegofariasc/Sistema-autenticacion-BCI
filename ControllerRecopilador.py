from time               import sleep
from Controller         import Controller
from Movimiento         import Movimiento
from Lector             import Lector
from random             import randint, shuffle
from threading          import Thread
from ViewAuxiliar       import ViewAuxiliar

class ControllerRecopilador(Controller, Thread):


    def __init__(self, view, model, viewRaiz, controllerRaiz):
        super().__init__(view,model)
        self.__viewRaiz = viewRaiz
        self.__controllerRaiz = controllerRaiz


    def __cambiarMovimiento(self, movimiento):

        # Borrar las flechas de izquierda y derecha al iniciar el 
        # cambio de movimiento
        try:
            self._view.etiquetaImagenIzquierda.place_forget()
            self._view.etiquetaImagenDerecha.place_forget()
        except:
            pass

        if movimiento == Movimiento.PREPARACION:

            # Cambiar imagen de movimiento
            self._view.etiquetaImagenMovimiento.config(
                image=self._view.renderImagenMovimientoAtencion
            ) # End config

            # Cambiar texto
            self._view.etiquetaDescripcionMovimiento.config(
                text="PREPÁRESE"
            ) # End config

            self._view.etiquetaDescripcionMovimiento.config( 
                fg=ViewAuxiliar.obtenerColor(241,196,15),
            ) # End config
            

        elif movimiento == Movimiento.REPOSO:

            # Cambiar imagen de movimiento
            self._view.etiquetaImagenMovimiento.config(
                image=self._view.renderImagenMovimientoReposo
            ) # End config

            # Cambiar texto
            self._view.etiquetaDescripcionMovimiento.config(
                text="REPOSO"
            ) # End config

        elif movimiento == Movimiento.MANO_IZQUIERDA:

            # Cambiar imagen de movimiento
            self._view.etiquetaImagenMovimiento.config(
                image=self._view.renderImagenMovimientoMano
            ) # End config

            # Cambiar texto
            self._view.etiquetaDescripcionMovimiento.config(
                text="MANO IZQUIERDA"
            ) # End config
            self._view.etiquetaImagenIzquierda.place(x= ((self._view.LARGO - 100) / 2) - 60, y= 120, height=60, width=60)

        elif movimiento == Movimiento.MANO_DERECHA:

            # Cambiar imagen de movimiento
            self._view.etiquetaImagenMovimiento.config(
                image=self._view.renderImagenMovimientoMano
            ) # End config

            # Cambiar texto
            self._view.etiquetaDescripcionMovimiento.config(
                text="MANO DERECHA"
            ) # End config
            self._view.etiquetaImagenDerecha.place(x= ((self._view.LARGO - 100) / 2) + 100, y= 120, height=60, width=60)

        elif movimiento == Movimiento.PIE_IZQUIERDO:

            # Cambiar imagen de movimiento
            self._view.etiquetaImagenMovimiento.config(
                image=self._view.renderImagenMovimientoPie
            ) # End config

            # Cambiar texto
            self._view.etiquetaDescripcionMovimiento.config(
                text="PIE IZQUIERDO"
            ) # End config
            self._view.etiquetaImagenIzquierda.place(x= ((self._view.LARGO - 100) / 2) - 60, y= 120, height=60, width=60)

        elif movimiento == Movimiento.PIE_DERECHO:

            # Cambiar imagen de movimiento
            self._view.etiquetaImagenMovimiento.config(
                image=self._view.renderImagenMovimientoPie
            ) # End config

            # Cambiar texto
            self._view.etiquetaDescripcionMovimiento.config(
                text="PIE DERECHO"
            ) # End config
            self._view.etiquetaImagenDerecha.place(x= ((self._view.LARGO - 100) / 2) + 100, y= 120, height=60, width=60)

        elif movimiento == Movimiento.FINALIZADO:

            # Cambiar imagen de movimiento
            self._view.etiquetaImagenMovimiento.config(
                image=self._view.renderImagenMovimientoFinalizado
            ) # End config

            # Cambiar texto
            self._view.etiquetaDescripcionMovimiento.config(
                text="LISTO, ESPERE..."
            ) # End config

    def conducirExperimento(self, tareas, duracionExperimentos, callback):

        # Crear un lector
        lector = Lector(Lector.SIMULADOR,[1,2,3],puerto="")
        
        # Inicializar colecciones de datos
        senal_C1 = []
        senal_C2 = []

        # Preparar al usuario por 5 segundos
        self.__cambiarMovimiento(Movimiento.PREPARACION)
        sleep(5)

        # Realizar cada tarea solicitada
        for tarea in tareas:

            # Cambiar a reposo
            # Nota: Se usa randint para garantizar que el tiempo
            # de reposo sea aleatorio, aunque el valor asignado por randint
            # no es el reposo final. El lector agrega tiempo dada la demora
            # en conectar con el casco
            self.__cambiarMovimiento(Movimiento.REPOSO)
            sleep(randint(3, 5))

            # Iniciar la recopilacion de experimentos
            datosExperimento = lector.recopilarDatosExperimento(
                duracionExperimentos, 
                callbackIniciar=
                lambda tipoTarea=tarea : self.__cambiarMovimiento(tipoTarea)
            ) # End recopilarDatosExperimento

            if tarea == Movimiento.MANO_IZQUIERDA:
                senal_C1.append(datosExperimento)
            if tarea == Movimiento.MANO_IZQUIERDA:
                senal_C2.append(datosExperimento)

        # Notificar finalizacion
        self.__cambiarMovimiento(Movimiento.FINALIZADO)
        self._view.etiquetaDescripcionMovimiento.config( 
            fg=ViewAuxiliar.obtenerColor(46,204,113),
        ) # End config

        # VALORES ALEATORIOS -- PRUEBA --
        from numpy.random import rand
        senal_C1 = rand(5,3,500)
        senal_C2 = rand(5,3,500)

        # Procesar la senal obtenida
        sleep(2)
        callback(senal_C1, senal_C2)


    # Funcion auxiliar para enviar a la base de datos la informacion recopilada 
    def __almacenarDatosRecopilados(self, senal_C1, senal_C2):

        senalProcesada_C1, senalProcesada_C2 = self._model.procesarSenal(senal_C1, senal_C2, 2)

        # Cambiar view de la ventana raiz para denotar validacion
        self.__viewRaiz.etiquetaSeccionEEG.config(
            text = 'Grabación EEG' 
        ) # End config
        self.__viewRaiz.etiquetaImagenValidacionDatosEEG.config(  
            image=self.__viewRaiz.renderValidacionCorrecta
        ) # End config

        # Desaparecer botones para seleccionar origen de datos
        self.__viewRaiz.botonDescartarDatos.place(x=170, y=211, height=28, width=115)
        self.__viewRaiz.botonEscaneoEEG.place_forget()

        # Indicarle al segundo controller que los datos funcionan
        # y pasar un apuntador a los datos
        # Nota: La insercion se lleva a cabo en crear usuario 
        # pues se necesita el identificador
        self.__controllerRaiz.aprobadoOrigenDatosEEG = True
        self.__controllerRaiz.datos_C1 = senalProcesada_C1
        self.__controllerRaiz.datos_C2 = senalProcesada_C2
        self.__controllerRaiz.hayDatosEEG = True
        self.__controllerRaiz.validarTodosCampos()

        # Cerrar la ventana del recopilador
        self._view.ventana.destroy()


    # Funcion auxiliar para enviar a la base de datos la informacion recopilada 
    def __autenticarConDatosRecopilados(self, senal_C1, senal_C2):

        senalProcesada_C1, senalProcesada_C2 = self._model.procesarSenal(senal_C1, senal_C2, 5)

        # Recuperar los datos de entrenamiento de la base de datos
        entrenamiento_C1 = self._model.obtenerExperimentos(
            self.__controllerRaiz.idUsuarioSeleccionado,
            Movimiento.TIPO_C1
        ) # End obtenerExperimentos
        entrenamiento_C2 = self._model.obtenerExperimentos(
            self.__controllerRaiz.idUsuarioSeleccionado,
            Movimiento.TIPO_C2
        ) # End obtenerExperimentos

        # Obtener los parametros de autenticacion
        # i.e. las fronteras, medias y desviaciones
        parametros_C1 = self._model.obtenerParametrosAutenticacion(entrenamiento_C1)
        parametros_C2 = self._model.obtenerParametrosAutenticacion(entrenamiento_C2)

        # Determinar el estado de aprobacion
        estados_C1 = self._model.obtenerAprobados(parametros_C1, entrenamiento_C1)
        estados_C2 = self._model.obtenerAprobados(parametros_C2, entrenamiento_C2)
        aprueba = self._model.determinarEstadoAutenticacion(
            self.__controllerRaiz.idUsuarioSeleccionado,
            estados_C1, estados_C2
        ) # End determinarEstadoAutenticacion
        
        # Pasar el resultado
        self.__controllerRaiz.resultadoRecopilador = aprueba

        # Si el sistema determino que el sujeto es correcto
        # reentrenar
        if aprueba:
            senalReentrenamiento_C1, senalReentrenamiento_C2 = self._model.procesarSenal(senal_C1, senal_C2, 1)

            # Para verificar elementos insertados para reentrenamiento
            # -- SOLO PRUEBA --
            # from numpy import shape
            # print(shape(senalReentrenamiento_C1))

            self._model.abrirEspacioParaExperimentos(senalReentrenamiento_C1, self.__controllerRaiz.idUsuarioSeleccionado)
            self._model.insertarExperimentos(senalReentrenamiento_C1, Movimiento.TIPO_C1, self.__controllerRaiz.idUsuarioSeleccionado)
            self._model.insertarExperimentos(senalReentrenamiento_C2, Movimiento.TIPO_C2, self.__controllerRaiz.idUsuarioSeleccionado)
            self._model.notificarGrabacionSesion(self.__controllerRaiz.idUsuarioSeleccionado)

        # Cerrar la ventana del recopilador
        self._view.ventana.destroy()
        self._view.ventana.quit()

    def recopilarDatosEntrenamiento(self):

        # Establecer parametros del experimento
        duracion = 4
        experimentos = [Movimiento.MANO_IZQUIERDA for _ in range(5)] + [Movimiento.MANO_DERECHA for _ in range(3)]
        shuffle(experimentos)

        # Verificar el tipo del objeto que invoco al recopilador
        # para determinar la accion que se realizara con los datos
        funcionCallback = None

        if type(self.__controllerRaiz).__name__ == 'ControllerCrearUsuario':
            funcionCallback = self.__almacenarDatosRecopilados
        else:
            funcionCallback = self.__autenticarConDatosRecopilados

        # Iniciar la recopilacion de forma asincrona
        Thread(
            target= lambda coleccionExperimentos=experimentos, duracionExperimentos=duracion, 
                    callback=funcionCallback: 
                    self.conducirExperimento(
                        coleccionExperimentos, duracionExperimentos, callback
                    ) # End conducir experimento
        ).start()
        

    def inicializarView(self):
        self._view.construirView()
        self._view.establecerListeners(self)
        self.recopilarDatosEntrenamiento()
        self._view.ventana.mainloop()
        


