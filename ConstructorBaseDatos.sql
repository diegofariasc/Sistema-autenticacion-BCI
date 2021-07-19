-- Drop si existe la base de datos
DROP DATABASE IF EXISTS AutenticadorEEG;
CREATE DATABASE AutenticadorEEG;
USE AutenticadorEEG;

-- Tabla para representar los usuarios
CREATE TABLE USUARIO( 
    
    id                      INTEGER         NOT NULL AUTO_INCREMENT,
    nombre                  VARCHAR(255)    NOT NULL,
    contrasena              VARCHAR(255)    NOT NULL,
    fechaRegistro           DATE            NOT NULL, 
    nivelSeguridad          VARCHAR(10)     NOT NULL,
    imagen                  BLOB,
    
    CONSTRAINT nivelSeguridadValido CHECK (
    nivelSeguridad = 'reducido' OR 
    nivelSeguridad = 'intermedio' OR
    nivelSeguridad = 'maximo'),

    PRIMARY KEY (id)
); -- End USUARIO

CREATE TABLE EXPERIMENTO (
    
    usuario             INTEGER         NOT NULL,
    numeroExperimento   INTEGER         NOT NULL,
    dimension           INTEGER         NOT NULL,
    valor               DOUBLE          NOT NULL,
    tipo                VARCHAR(14)     NOT NULL,

    CONSTRAINT tipoExperimentoValido CHECK (
        tipo = 'mano izquierda' OR 
        tipo = 'mano derecha' OR
        tipo = 'pie izquierdo' OR
        tipo = 'pie derecho'
    ), -- End constraint

    FOREIGN KEY (usuario) REFERENCES USUARIO(id),
    PRIMARY KEY (usuario, numeroExperimento, dimension)
); 


DELIMITER ;;
CREATE TRIGGER `registrarFecha` 
BEFORE INSERT ON USUARIO 
FOR EACH ROW
BEGIN
    SET NEW.fechaRegistro = CURDATE();
END;;
DELIMITER ;
