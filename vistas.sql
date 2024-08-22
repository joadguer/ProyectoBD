-- vistas
-- Vista de Pagos por Demanda
use EstudioJuridicoDB;
CREATE VIEW VistaPagosPorDemanda AS
SELECT p.codigoPago, p.codigoDemanda, p.metodoDePago, p.fecha, p.monto, p.concepto, p.descripcion
FROM pago p
JOIN demanda d ON p.codigoDemanda = d.CodigoDemanda;

-- Vista de Contratos por Pago
CREATE VIEW VistaContratosPorPago AS
SELECT c.codigoContrato, c.codigoPago, c.estadoGeneral, c.descripcion
FROM contrato c
JOIN pago p ON c.codigoPago = p.codigoPago;

-- Vista de Demandas por Contrato
CREATE VIEW VistaDemandasPorContrato AS
SELECT d.CodigoDemanda, d.codigoContrato, d.EstadoDeProceso, d.descripcion, d.FechaInicio, d.FechaFin, d.Audiencia, d.EstadoDeJuicio
FROM demanda d
JOIN contrato c ON d.codigoContrato = c.codigoContrato;

-- Vista de Áreas y su Tipo de Proceso
CREATE VIEW VistaAreasYTipoProceso AS
SELECT a.CodigoArea, a.Nombre, a.Descripcion, a.TipoDeProceso
FROM area a;

-- Vista de Etapas con Estado
CREATE VIEW VistaEtapasConEstado AS
SELECT e.CodigoEtapa, e.Descripcion, e.FechaInicio, e.FechaFin, e.Estado, e.Nombre
FROM etapa e;

-- Vista de Personas Naturales
CREATE VIEW VistaPersonasNaturales AS
SELECT p.IdentificadorCliente, p.CorreoElectronico, p.Nombre, p.ApellidoP, p.ApellidoM, p.FechaNacimiento, p.Telefono, p.EstadoCivil, p.Profesion
FROM personaNatural p;

-- Vista de Abogados y su Área de Enfoque
CREATE VIEW VistaAbogadosYAreaDeEnfoque AS
SELECT a.Cedula, a.Nombre, a.ApellidoM, a.ApellidoP, a.FechaNacimiento, a.AreaDeEnfoque
FROM abogado a;

-- Índices para la tabla 'pago'
CREATE INDEX idx_codigoPago ON pago(codigoPago);
CREATE INDEX idx_codigoDemanda ON pago(codigoDemanda);
CREATE INDEX idx_metodoDePago ON pago(metodoDePago);

-- Índices para la tabla 'contrato'
CREATE INDEX idx_codigoContrato ON contrato(codigoContrato);
CREATE INDEX idx_codigoPago ON contrato(codigoPago);

-- Índices para la tabla 'demanda'
CREATE INDEX idx_CodigoDemanda ON demanda(CodigoDemanda);
CREATE INDEX idx_codigoContrato ON demanda(codigoContrato);
CREATE INDEX idx_EstadoDeProceso ON demanda(EstadoDeProceso);

-- Índices para la tabla 'area'
CREATE INDEX idx_CodigoArea ON area(CodigoArea);
CREATE INDEX idx_TipoDeProceso ON area(TipoDeProceso);

-- Índices para la tabla 'etapa'
CREATE INDEX idx_CodigoEtapa ON etapa(CodigoEtapa);
CREATE INDEX idx_Estado ON etapa(Estado);

-- Índices para la tabla 'personaNatural'
CREATE INDEX idx_IdentificadorCliente ON personaNatural(IdentificadorCliente);
CREATE INDEX idx_CorreoElectronico ON personaNatural(CorreoElectronico);
CREATE INDEX idx_EstadoCivil ON personaNatural(EstadoCivil);

-- Índices para la tabla 'personaJuridica'
CREATE INDEX idx_IdentificadorCliente ON personaJuridica(IdentificadorCliente);
CREATE INDEX idx_RUC ON personaJuridica(RUC);
CREATE INDEX idx_TipoDeSociedad ON personaJuridica(TipoDeSociedad);

-- Índices para la tabla 'abogado'
CREATE INDEX idx_Cedula ON abogado(Cedula);
CREATE INDEX idx_AreaDeEnfoque ON abogado(AreaDeEnfoque);
