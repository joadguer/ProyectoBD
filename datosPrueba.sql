-- Inserta un contrato
INSERT INTO contrato (estadoGeneral, descripcion)
VALUES ('Activo', 'Contrato de prueba');

-- Inserta un área
INSERT INTO area (Nombre, Descripcion, TipoDeProceso)
VALUES ('Área de Prueba', 'Descripción del área de prueba', 'Tipo de prueba');

-- Inserta una etapa
INSERT INTO etapa (Descripcion, FechaInicio, FechaFin, Estado, Nombre)
VALUES ('Etapa de prueba', '2024-01-01', '2024-12-31', 'En progreso', 'Etapa de Prueba');

-- Inserta una persona natural
INSERT INTO personaNatural (CorreoElectronico, Nombre, ApellidoP, ApellidoM, FechaNacimiento, Telefono, EstadoCivil, Profesion)
VALUES ('cliente@ejemplo.com', 'Juan', 'Pérez', 'Gómez', '1985-05-15', '123456789', 'Soltero', 'Abogado');

-- Inserta una demanda
INSERT INTO demanda (codigoContrato, descripcion, FechaInicio, FechaFin, Area, Etapa, Estado, Monto)
VALUES (1, 'Demanda de prueba', '2024-01-01', '2024-12-31', 'Área de Prueba', 'Etapa de Prueba', 'En curso', 10000.00);

-- Inserta en la tabla 'pertenece'
INSERT INTO pertenece (CodigoDemanda, CodigoArea)
VALUES (1, 1);

-- Inserta en la tabla 'tener'
INSERT INTO tener (CodigoArea, CodigoEtapa)
VALUES (1, 1);

-- Inserta en la tabla 'posee'
INSERT INTO posee (IdentificadorCliente, CodigoDemanda)
VALUES (1, 1);
