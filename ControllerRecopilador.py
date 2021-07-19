from time           import sleep
from Controller     import Controller
from Movimiento     import Movimiento
from Lector         import Lector
from random         import randint, shuffle
from threading      import Thread
from ViewAuxiliar   import ViewAuxiliar

class ControllerRecopilador(Controller):


    def __init__(self, view, model):
        super().__init__(view,model)


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
                text="LISTO"
            ) # End config

    def conducirExperimento(self, tareas, duracionExperimentos):

        # Crear un lector
        lector = Lector(Lector.SIMULADOR,[1,2,3],puerto="")
        
        # Inicializar colecciones de datos
        from numpy import ones
        senal_C1 = ones((5,3,500)) #[]
        senal_C2 = ones((5,3,500))#[]

        # # Preparar al usuario por 5 segundos
        # self.__cambiarMovimiento(Movimiento.PREPARACION)
        # sleep(5)

        # # Realizar cada tarea solicitada
        # for tarea in tareas:

        #     # Cambiar a reposo
        #     # Nota: Se usa randint para garantizar que el tiempo
        #     # de reposo sea aleatorio, aunque el valor asignado por randint
        #     # no es el reposo final. El lector agrega tiempo dada la demora
        #     # en conectar con el casco
        #     self.__cambiarMovimiento(Movimiento.REPOSO)
        #     sleep(randint(3, 5))

        #     # Iniciar la recopilacion de experimentos
        #     datosExperimento = lector.recopilarDatosExperimento(
        #         duracionExperimentos, 
        #         callbackIniciar=
        #         lambda tipoTarea=tarea : self.__cambiarMovimiento(tipoTarea)
        #     ) # End recopilarDatosExperimento

        #     if tarea == Movimiento.MANO_IZQUIERDA:
        #         senal_C1.append(datosExperimento)
        #     if tarea == Movimiento.MANO_IZQUIERDA:
        #         senal_C2.append(datosExperimento)

        # Notificar finalizacion
        self.__cambiarMovimiento(Movimiento.FINALIZADO)

        # Procesar senal e insertarla en la base de datos
        #procesada_C1, procesada_C2 = self._model.procesarSenal(senal_C1, senal_C2)
        #self._model.insertarExperimentos(procesada_C1, Movimiento.TIPO_C1)
        #self._model.insertarExperimentos(procesada_C2, Movimiento.TIPO_C2)
        datos = self._model.obtenerExperimentos(1,Movimiento.TIPO_C1)
        self._model.obtenerParametrosAutenticacion(datos)

        self._view.etiquetaDescripcionMovimiento.config( 
            fg=ViewAuxiliar.obtenerColor(46,204,113),
        ) # End config


    def recopilarDatosEntrenamiento(self, _):

        # Establecer parametros del experimento
        duracion = 4
        experimentos = [Movimiento.MANO_IZQUIERDA for _ in range(5)] + [Movimiento.MANO_DERECHA for _ in range(5)]
        shuffle(experimentos)

        # Iniciar la recopilacion de forma asincrona
        Thread(
            target= lambda coleccionExperimentos=experimentos, duracionExperimentos=duracion : 
                    self.conducirExperimento(coleccionExperimentos, duracionExperimentos)
        ).start()
        

    def inicializarView(self):
        self._view.construirView()
        self._view.establecerListeners(self)
        self._view.ventana.mainloop()
        


