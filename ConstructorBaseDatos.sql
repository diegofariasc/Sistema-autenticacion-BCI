-- Drop si existe la base de datos
DROP DATABASE IF EXISTS AutenticadorEEG;
CREATE DATABASE AutenticadorEEG;
USE AutenticadorEEG;

-- Tabla para representar los usuarios
CREATE TABLE DOCUMENTO( id              INTEGER         NOT NULL AUTO_INCREMENT,
                        nombre          VARCHAR(255)    NOT NULL,
                        contrasena      VARCHAR(255)    NOT NULL,
                        fechaRegistro   DATE            NOT NULL, 
                        media           DOUBLE          NOT NULL,
                        desviacion      DOUBLE          NOT NULL,
                        nivelSeguridad  VARCHAR(10)     NOT NULL,
                        imagen          BLOB,
                        
                        CONSTRAINT nivelSeguridadValido CHECK (
                        nivelSeguridad = 'reducido' OR 
                        nivelSeguridad = 'intermedio' OR
                        nivelSeguridad = 'maximo'),

                        PRIMARY KEY (id));
