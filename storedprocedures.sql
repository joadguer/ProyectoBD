USE EstudioJuridicoDB;

-- Cambiar el delimitador temporalmente
DELIMITER $$

-- Insertar un nuevo pago
CREATE PROCEDURE InsertarPago(
    IN p_codigoContrato INT,
    IN p_metodoDePago VARCHAR(255),
    IN p_fecha DATE,
    IN p_monto DECIMAL(10, 2),
    IN p_descripcion TEXT
)
BEGIN
    INSERT INTO pago ( codigoContrato, metodoDePago, fecha, monto, descripcion)
    VALUES (p_codigoContrato, p_metodoDePago, p_fecha, p_monto, p_descripcion);
END $$

-- Actualizar un pago existente
CREATE PROCEDURE ActualizarPago(
    IN p_codigoPago INT,
    IN p_codigoDemanda INT,
    IN p_metodoDePago VARCHAR(255),
    IN p_fecha DATE,
    IN p_monto DECIMAL(10, 2),
    IN p_descripcion TEXT
)
BEGIN
    UPDATE pago
    SET codigoDemanda = p_codigoDemanda, metodoDePago = p_metodoDePago, fecha = p_fecha, monto = p_monto, concepto = p_concepto, descripcion = p_descripcion
    WHERE codigoPago = p_codigoPago;
END $$

-- Eliminar un pago
CREATE PROCEDURE EliminarPago(IN p_codigoPago INT)
BEGIN
    DELETE FROM pago WHERE codigoPago = p_codigoPago;
END $$

-- Consultar pagos por demanda
CREATE PROCEDURE ConsultarPagosPorDemanda(IN p_codigoDemanda INT)
BEGIN
    SELECT * FROM pago WHERE codigoDemanda = p_codigoDemanda;
END $$

CREATE PROCEDURE InsertarContrato(
    IN estadoGeneral VARCHAR(255),
    IN descripcion TEXT
)
BEGIN
    INSERT INTO contrato (estadoGeneral, descripcion) 
    VALUES (estadoGeneral, descripcion);
    
    SELECT LAST_INSERT_ID() AS contrato_id;
END;



-- Actualizar un contrato existente
CREATE PROCEDURE ActualizarContrato(
    IN p_codigoContrato INT,
    IN p_codigoPago INT,
    IN p_estadoGeneral VARCHAR(255),
    IN p_descripcion TEXT
)
BEGIN
    UPDATE contrato
    SET codigoPago = p_codigoPago, estadoGeneral = p_estadoGeneral, descripcion = p_descripcion
    WHERE codigoContrato = p_codigoContrato;
END $$

-- Eliminar un contrato
CREATE PROCEDURE EliminarContrato(IN p_codigoContrato INT)
BEGIN
    DELETE FROM contrato WHERE codigoContrato = p_codigoContrato;
END $$

-- Consultar contratos por pago
CREATE PROCEDURE ConsultarContratosPorPago(IN p_codigoPago INT)
BEGIN
    SELECT * FROM contrato WHERE codigoPago = p_codigoPago;
END $$

-- Insertar una nueva demanda
CREATE PROCEDURE InsertarDemanda(
    IN p_codigoContrato INT,
    IN p_descripcion TEXT,
    IN p_FechaInicio DATE,
    IN p_FechaFin DATE,
    IN p_Area VARCHAR(50),
    IN p_Etapa VARCHAR(50),
    IN p_Estado VARCHAR(50),
    IN p_Monto DECIMAL(10,2)
)
BEGIN
    INSERT INTO demanda (codigoContrato, descripcion, FechaInicio, FechaFin, Area, Etapa, Estado, Monto)
    VALUES (p_codigoContrato, p_descripcion, p_FechaInicio, p_FechaFin, p_Area, p_Etapa, p_Estado, p_Monto);
END $$ 


-- Actualizar una demanda existente
CREATE PROCEDURE ActualizarDemanda(
    IN p_CodigoDemanda INT,
    IN p_codigoContrato INT,
    IN p_EstadoDeProceso VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_FechaInicio DATE,
    IN p_FechaFin DATE,
    IN p_Audiencia DATE,
    IN p_EstadoDeJuicio VARCHAR(255)
)
BEGIN
    UPDATE demanda
    SET codigoContrato = p_codigoContrato, EstadoDeProceso = p_EstadoDeProceso, descripcion = p_descripcion, FechaInicio = p_FechaInicio, FechaFin = p_FechaFin, Audiencia = p_Audiencia, EstadoDeJuicio = p_EstadoDeJuicio
    WHERE CodigoDemanda = p_CodigoDemanda;
END $$

-- Eliminar una demanda
CREATE PROCEDURE EliminarDemanda(IN p_CodigoDemanda INT)
BEGIN
    DELETE FROM demanda WHERE CodigoDemanda = p_CodigoDemanda;
END $$

-- Consultar demandas por contrato
CREATE PROCEDURE ConsultarDemandasPorContrato(IN p_codigoContrato INT)
BEGIN
    SELECT * FROM demanda WHERE codigoContrato = p_codigoContrato;
END $$

-- Insertar una nueva área
CREATE PROCEDURE InsertarArea(
    IN p_Nombre VARCHAR(255),
    IN p_Descripcion TEXT,
    IN p_TipoDeProceso VARCHAR(255)
)
BEGIN
    INSERT INTO area ( Nombre, Descripcion, TipoDeProceso)
    VALUES ( p_Nombre, p_Descripcion, p_TipoDeProceso);
END $$

-- Actualizar un área existente
CREATE PROCEDURE ActualizarArea(
    IN p_CodigoArea INT,
    IN p_Nombre VARCHAR(255),
    IN p_Descripcion TEXT,
    IN p_TipoDeProceso VARCHAR(255)
)
BEGIN
    UPDATE area
    SET Nombre = p_Nombre, Descripcion = p_Descripcion, TipoDeProceso = p_TipoDeProceso
    WHERE CodigoArea = p_CodigoArea;
END $$

-- Eliminar un área
CREATE PROCEDURE EliminarArea(IN p_CodigoArea INT)
BEGIN
    DELETE FROM area WHERE CodigoArea = p_CodigoArea;
END $$

-- Consultar todas las áreas
CREATE PROCEDURE ConsultarAreas()
BEGIN
    SELECT * FROM area;
END $$

-- Insertar una nueva etapa
CREATE PROCEDURE InsertarEtapa(
    IN p_Descripcion TEXT,
    IN p_FechaInicio DATE,
    IN p_FechaFin DATE,
    IN p_Estado VARCHAR(255),
    IN p_Nombre VARCHAR(255)
)
BEGIN
    INSERT INTO etapa ( Descripcion, FechaInicio, FechaFin, Estado, Nombre)
    VALUES (p_Descripcion, p_FechaInicio, p_FechaFin, p_Estado, p_Nombre);
END $$

-- Actualizar una etapa existente
CREATE PROCEDURE ActualizarEtapa(
    IN p_CodigoEtapa INT,
    IN p_Descripcion TEXT,
    IN p_FechaInicio DATE,
    IN p_FechaFin DATE,
    IN p_Estado VARCHAR(255),
    IN p_Nombre VARCHAR(255)
)
BEGIN
    UPDATE etapa
    SET Descripcion = p_Descripcion, FechaInicio = p_FechaInicio, FechaFin = p_FechaFin, Estado = p_Estado, Nombre = p_Nombre
    WHERE CodigoEtapa = p_CodigoEtapa;
END $$

-- Eliminar una etapa
CREATE PROCEDURE EliminarEtapa(IN p_CodigoEtapa INT)
BEGIN
    DELETE FROM etapa WHERE CodigoEtapa = p_CodigoEtapa;
END $$

-- Consultar todas las etapas
CREATE PROCEDURE ConsultarEtapas()
BEGIN
    SELECT * FROM etapa;
END $$


-- Insertar una nueva persona natural
CREATE PROCEDURE InsertarPersonaNatural(
    IN p_CorreoElectronico VARCHAR(255),
    IN p_Nombre VARCHAR(255),
    IN p_ApellidoP VARCHAR(255),
    IN p_ApellidoM VARCHAR(255),
    IN p_FechaNacimiento DATE,
    IN p_Telefono VARCHAR(20),
    IN p_EstadoCivil VARCHAR(255),
    IN p_Profesion VARCHAR(255)
)
BEGIN
    INSERT INTO personaNatural ( CorreoElectronico, Nombre, ApellidoP, ApellidoM, FechaNacimiento, Telefono, EstadoCivil, Profesion)
    VALUES (p_CorreoElectronico, p_Nombre, p_ApellidoP, p_ApellidoM, p_FechaNacimiento, p_Telefono, p_EstadoCivil, p_Profesion);
END $$

-- Actualizar una persona natural existente
CREATE PROCEDURE ActualizarPersonaNatural(
    IN p_IdentificadorCliente INT,
    IN p_CorreoElectronico VARCHAR(255),
    IN p_Nombre VARCHAR(255),
    IN p_ApellidoP VARCHAR(255),
    IN p_ApellidoM VARCHAR(255),
    IN p_FechaNacimiento DATE,
    IN p_Telefono VARCHAR(20),
    IN p_EstadoCivil VARCHAR(255),
    IN p_Profesion VARCHAR(255)
)
BEGIN
    UPDATE personaNatural
    SET CorreoElectronico = p_CorreoElectronico, Nombre = p_Nombre, ApellidoP = p_ApellidoP, ApellidoM = p_ApellidoM, FechaNacimiento = p_FechaNacimiento, Telefono = p_Telefono, EstadoCivil = p_EstadoCivil, Profesion = p_Profesion
    WHERE IdentificadorCliente = p_IdentificadorCliente;
END $$

-- Eliminar una persona natural
CREATE PROCEDURE EliminarPersonaNatural(IN p_IdentificadorCliente INT)
BEGIN
    DELETE FROM personaNatural WHERE IdentificadorCliente = p_IdentificadorCliente;
END $$

-- Consultar todas las personas naturales
CREATE PROCEDURE ConsultarPersonasNaturales()
BEGIN
    SELECT * FROM personaNatural;
END $$

-- Consultar todas las personas juridicas
CREATE PROCEDURE ConsultarPersonasJuridicas()
BEGIN
    SELECT * FROM personaJuridica;
END $$


CREATE PROCEDURE InsertarPersonaJuridica(
    IN p_CorreoElectronico VARCHAR(255),
    IN p_Nombre VARCHAR(255),
    IN p_ApellidoP VARCHAR(255),
    IN p_ApellidoM VARCHAR(255),
    IN p_FechaNacimiento DATE,
    IN p_Telefono VARCHAR(20),
    IN p_TipoDeSociedad VARCHAR(255),
    IN p_SectorDeActividad VARCHAR(255),
    IN p_RUC VARCHAR(20)
)
BEGIN
    INSERT INTO personaJuridica (
         CorreoElectronico, Nombre, ApellidoP, ApellidoM, FechaNacimiento, Telefono, TipoDeSociedad, SectorDeActividad, RUC
    )
    VALUES (
        p_CorreoElectronico,p_Nombre,p_ApellidoP,p_ApellidoM,p_FechaNacimiento,p_Telefono,p_TipoDeSociedad,p_SectorDeActividad,p_RUC
    );
END $$

-- Insertar un nuevo abogado
CREATE PROCEDURE InsertarAbogado(
    IN p_Cedula VARCHAR(20),
    IN p_Nombre VARCHAR(255),
    IN p_ApellidoM VARCHAR(255),
    IN p_ApellidoP VARCHAR(255),
    IN p_FechaNacimiento DATE,
    IN p_AreaDeEnfoque VARCHAR(255)
)
BEGIN
    INSERT INTO abogado (Cedula, Nombre, ApellidoM, ApellidoP, FechaNacimiento, AreaDeEnfoque)
    VALUES (p_Cedula, p_Nombre, p_ApellidoM, p_ApellidoP, p_FechaNacimiento, p_AreaDeEnfoque);
END $$

-- Actualizar un abogado existente
CREATE PROCEDURE ActualizarAbogado(
    IN p_Cedula VARCHAR(20),
    IN p_Nombre VARCHAR(255),
    IN p_ApellidoM VARCHAR(255),
    IN p_ApellidoP VARCHAR(255),
    IN p_FechaNacimiento DATE,
    IN p_AreaDeEnfoque VARCHAR(255)
)
BEGIN
    UPDATE abogado
    SET Nombre = p_Nombre, ApellidoM = p_ApellidoM, ApellidoP = p_ApellidoP, FechaNacimiento = p_FechaNacimiento, AreaDeEnfoque = p_AreaDeEnfoque
    WHERE Cedula = p_Cedula;
END $$

-- Eliminar un abogado
CREATE PROCEDURE EliminarAbogado(IN p_Cedula VARCHAR(20))
BEGIN
    DELETE FROM abogado WHERE Cedula = p_Cedula;
END $$

-- Consultar todos los abogados
CREATE PROCEDURE ConsultarAbogados()
BEGIN
    SELECT * FROM abogado;
END $$

-- Restaurar el delimitador predeterminado
DELIMITER ;



-- store procedure para el query de la base de datos
DELIMITER //

CREATE PROCEDURE obtener_datos_demanda()
BEGIN
    SELECT 
        d.CodigoDemanda AS idDemanda,
        CONCAT(p.Nombre, ' ', p.ApellidoP, ' ', p.ApellidoM) AS cliente,
        d.descripcion AS descripcionDemanda,
        e.Nombre AS etapa,
        d.Estado AS estado,
        CONCAT(a.Nombre, ' ', a.ApellidoP, ' ', a.ApellidoM) AS abogado,
        d.FechaInicio AS fechaInicio,
        d.FechaFin AS fechaFin,
        ar.Nombre AS area,
        c.estadoGeneral AS contrato,
        p2.monto AS monto
    FROM demanda d
    JOIN posee ps ON d.CodigoDemanda = ps.CodigoDemanda
    JOIN personaNatural p ON ps.IdentificadorCliente = p.IdentificadorCliente
    JOIN pertenece pe ON d.CodigoDemanda = pe.CodigoDemanda
    JOIN area ar ON pe.CodigoArea = ar.CodigoArea
    JOIN tener te ON ar.CodigoArea = te.CodigoArea
    JOIN etapa e ON te.CodigoEtapa = e.CodigoEtapa
    JOIN contrato c ON d.codigoContrato = c.codigoContrato
    LEFT JOIN trabaja tr ON c.codigoContrato = tr.CodigoContrato
    LEFT JOIN abogado a ON tr.CodigoAbogado = a.CodigoAbogado
    LEFT JOIN pago p2 ON c.codigoContrato = p2.codigoContrato;
END //

DELIMITER ;


DELIMITER $$

CREATE PROCEDURE ObtenerMontoPorPago(
    IN p_codigoPago INT,
    OUT p_monto DECIMAL(10,2)
)
BEGIN
    -- Seleccionar el monto del pago correspondiente al codigoPago
    SELECT monto
    INTO p_monto
    FROM pago
    WHERE codigoPago = p_codigoPago;
END $$

DELIMITER ;





-- Procedimiento para insertar en la tabla 'pertenece'
DELIMITER //

CREATE PROCEDURE InsertarPertenencia()
BEGIN
    DECLARE ultimoCodigoDemanda INT;
    DECLARE ultimoCodigoArea INT;

    -- Obtener el último CódigoDemanda insertado
    SELECT MAX(CodigoDemanda) INTO ultimoCodigoDemanda FROM demanda;

    -- Obtener el último CódigoArea insertado
    SELECT MAX(CodigoArea) INTO ultimoCodigoArea FROM area;

    -- Insertar en la tabla pertenece
    INSERT INTO pertenece (CodigoDemanda, CodigoArea) 
    VALUES (ultimoCodigoDemanda, ultimoCodigoArea);
END //

DELIMITER ;

-- Procedimiento para insertar en la tabla 'tener'
DELIMITER //

CREATE PROCEDURE InsertarTener()
BEGIN
    DECLARE ultimoCodigoArea INT;
    DECLARE ultimoCodigoEtapa INT;

    -- Obtener el último CódigoArea insertado
    SELECT MAX(CodigoArea) INTO ultimoCodigoArea FROM area;

    -- Obtener el último CódigoEtapa insertado
    SELECT MAX(CodigoEtapa) INTO ultimoCodigoEtapa FROM etapa;

    -- Insertar en la tabla tener
    INSERT INTO tener (CodigoArea, CodigoEtapa) 
    VALUES (ultimoCodigoArea, ultimoCodigoEtapa);
END //

DELIMITER ;

-- Procedimiento para insertar en la tabla 'posee'
DELIMITER //

CREATE PROCEDURE InsertarPosee()
BEGIN
    DECLARE ultimoIdentificadorCliente INT;
    DECLARE ultimoCodigoDemanda INT;

    -- Obtener el último IdentificadorCliente insertado
    SELECT MAX(IdentificadorCliente) INTO ultimoIdentificadorCliente FROM personaNatural;

    -- Obtener el último CódigoDemanda insertado
    SELECT MAX(CodigoDemanda) INTO ultimoCodigoDemanda FROM demanda;

    -- Insertar en la tabla posee
    INSERT INTO posee (IdentificadorCliente, CodigoDemanda) 
    VALUES (ultimoIdentificadorCliente, ultimoCodigoDemanda);
END //

DELIMITER ;

-- Procedimiento para insertar en la tabla 'trabaja'
DELIMITER //

CREATE PROCEDURE InsertarTrabaja()
BEGIN
    DECLARE ultimoCodigoAbogado INT;
    DECLARE ultimoCodigoContrato INT;

    -- Obtener el último CódigoAbogado insertado
    SELECT MAX(CodigoAbogado) INTO ultimoCodigoAbogado FROM abogado;

    -- Obtener el último CódigoContrato insertado
    SELECT MAX(CodigoContrato) INTO ultimoCodigoContrato FROM contrato;

    -- Insertar en la tabla trabaja
    INSERT INTO trabaja (CodigoAbogado, CodigoContrato) 
    VALUES (ultimoCodigoAbogado, ultimoCodigoContrato);
END //

DELIMITER ;

