-- Crear la tabla 'pago'
drop database  EstudioJuridicoDB;
create database EstudioJuridicoDB;
use EstudioJuridicoDB;
CREATE TABLE pago (
    codigoPago INT AUTO_INCREMENT PRIMARY KEY,
    codigoContrato INT,
    metodoDePago VARCHAR(255),
    fecha DATE,
    monto DECIMAL(10, 2),
    descripcion TEXT
);

-- Crear la tabla 'contrato'
CREATE TABLE contrato (
    codigoContrato INT AUTO_INCREMENT PRIMARY KEY,
    estadoGeneral VARCHAR(255),
    descripcion TEXT
    
);

-- Crear la tabla 'demanda'
CREATE TABLE demanda (
    CodigoDemanda INT AUTO_INCREMENT PRIMARY KEY,
    codigoContrato INT,
    -- EstadoDeProceso VARCHAR(255),
    descripcion TEXT,
    FechaInicio DATE,
    FechaFin DATE,
    -- Audiencia DATE,
    Area VARCHAR(50), 
    Etapa VARCHAR(50),
    Estado VARCHAR(50),
    Monto DECIMAL(10,2)
    -- EstadoDeJuicio VARCHAR(255)
);

-- Crear la tabla 'area'
CREATE TABLE area (
    CodigoArea INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255),
    Descripcion TEXT,
    TipoDeProceso VARCHAR(255)
);

-- Crear la tabla 'etapa'
CREATE TABLE etapa (
    CodigoEtapa INT AUTO_INCREMENT PRIMARY KEY,
    Descripcion TEXT,
    FechaInicio DATE,
    FechaFin DATE,
    Estado VARCHAR(255),
    Nombre VARCHAR(255)
);

-- Crear la tabla 'personaNatural'
CREATE TABLE personaNatural (
    IdentificadorCliente INT AUTO_INCREMENT PRIMARY KEY,
    CorreoElectronico VARCHAR(255),
    Nombre VARCHAR(255),
    ApellidoP VARCHAR(255),
    ApellidoM VARCHAR(255),
    FechaNacimiento DATE,
    Telefono VARCHAR(20),
    EstadoCivil VARCHAR(255),
    Profesion VARCHAR(255)
);

-- Crear la tabla 'personaJuridica'
CREATE TABLE personaJuridica (
    IdentificadorCliente INT AUTO_INCREMENT PRIMARY KEY,
    CorreoElectronico VARCHAR(255),
    Nombre VARCHAR(255),
    ApellidoP VARCHAR(255),
    ApellidoM VARCHAR(255),
    FechaNacimiento DATE,
    Telefono VARCHAR(20),
    TipoDeSociedad VARCHAR(255),
    SectorDeActividad VARCHAR(255),
    RUC VARCHAR(20)
);

-- Crear la tabla 'abogado'
CREATE TABLE abogado (
    CodigoAbogado INT AUTO_INCREMENT PRIMARY KEY,
    Cedula INT UNIQUE,
    Nombre VARCHAR(255),
    ApellidoP VARCHAR(255),
    ApellidoM VARCHAR(255),
    FechaNacimiento DATE,
    AreaDeEnfoque VARCHAR(255)
);

-- Crear la tabla 'pertenece'
CREATE TABLE pertenece (
    CodigoDemanda INT,
    CodigoArea INT,
    PRIMARY KEY (CodigoDemanda, CodigoArea)
);

-- Crear la tabla 'tener'
CREATE TABLE tener (
    CodigoArea INT,
    CodigoEtapa INT,
    PRIMARY KEY (CodigoArea, CodigoEtapa)
);

-- Crear la tabla 'posee'
CREATE TABLE posee (
    IdentificadorCliente INT,
    CodigoDemanda INT,
    PRIMARY KEY (IdentificadorCliente, CodigoDemanda)
);

-- Crear la tabla 'trabaja'
CREATE TABLE trabaja (
    CodigoAbogado INT,
    CodigoContrato INT,
    PRIMARY KEY (Cedula, CodigoContrato)
);


ALTER TABLE pago
    ADD CONSTRAINT fk_pago_contrato
    FOREIGN KEY (codigoContrato) REFERENCES contrato(codigoContrato)
    ON DELETE CASCADE;

ALTER TABLE demanda
    ADD CONSTRAINT fk_demanda_contrato
    FOREIGN KEY (codigoContrato) REFERENCES contrato(codigoContrato)
    ON DELETE CASCADE;

ALTER TABLE pertenece
    ADD CONSTRAINT fk_pertenece_demanda
    FOREIGN KEY (CodigoDemanda) REFERENCES demanda(CodigoDemanda)
    ON DELETE CASCADE,
    ADD CONSTRAINT fk_pertenece_area
    FOREIGN KEY (CodigoArea) REFERENCES area(CodigoArea)
    ON DELETE CASCADE;

ALTER TABLE tener
    ADD CONSTRAINT fk_tener_area
    FOREIGN KEY (CodigoArea) REFERENCES area(CodigoArea)
    ON DELETE CASCADE,
    ADD CONSTRAINT fk_tener_etapa
    FOREIGN KEY (CodigoEtapa) REFERENCES etapa(CodigoEtapa)
    ON DELETE CASCADE;

ALTER TABLE posee
    ADD CONSTRAINT fk_posee_cliente
    FOREIGN KEY (IdentificadorCliente) REFERENCES personaNatural(IdentificadorCliente)
    ON DELETE CASCADE,
    ADD CONSTRAINT fk_posee_demanda
    FOREIGN KEY (CodigoDemanda) REFERENCES demanda(CodigoDemanda)
    ON DELETE CASCADE;

ALTER TABLE trabaja
    ADD CONSTRAINT fk_trabaja_abogado
    FOREIGN KEY (CodigoAbogado) REFERENCES abogado(CodigoAbogado)
    ON DELETE CASCADE,
    ADD CONSTRAINT fk_trabaja_contrato
    FOREIGN KEY (CodigoContrato) REFERENCES contrato(codigoContrato)
    ON DELETE CASCADE;

