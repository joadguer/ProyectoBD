import mysql.connector
from mysql.connector import Error

# Configura la conexión a la base de datos
def create_connection(usuario, clave):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user= usuario,  
            password= clave,  
            database='EstudioJuridicoDB'
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

#Insertar persona juridica
def insertar_persona_juridica( correo_electronico, nombre, apellido_p, apellido_m,
                              fecha_nacimiento, telefono, tipo_de_sociedad, sector_de_actividad, ruc):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarPersonaJuridica', [
                 correo_electronico, nombre, apellido_p, apellido_m,
                fecha_nacimiento, telefono, tipo_de_sociedad, sector_de_actividad, ruc
            ])
            connection.commit()
            print("Persona jurídica insertada exitosamente.")
        except Error as e:
            print(f"Error al insertar persona jurídica: {e}")
        finally:
            cursor.close()
            connection.close()
            

# Función para obtener todos los clientes
def obtener_clientesJuridicos():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ConsultarPersonasJuridicas')
            print("Obteniendo personas juridicas")
            all_rows = []
            
            # Iterar sobre los resultados del procedimiento almacenado
            for result in cursor.stored_results():
                rows = result.fetchall()  # Recuperar todas las filas del conjunto de resultados
                all_rows.extend(rows)     # Agregar las filas a la lista total
            return all_rows

        except Error as e:
            print(f"Error al consultar personas juridicas: {e}")
        finally:
            cursor.close()
            connection.close()
            return []
        


#Insertar persona natural
def insertar_persona_natural(correo_electronico, nombre, apellido_p, apellido_m,
                              fecha_nacimiento, telefono, estado_civil, profesion):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarPersonaNatural', [
                 correo_electronico, nombre, apellido_p, apellido_m,
                fecha_nacimiento, telefono, estado_civil, profesion
            ])
            connection.commit()
            print("Persona natural insertada exitosamente.")
        except Error as e:
            print(f"Error al insertar persona natural: {e}")
        finally:
            cursor.close()
            connection.close()



def obtener_clientesNaturales():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ConsultarPersonasNaturales')
            print("Obteniendo personas naturales")            
            all_rows = []
            
            # Iterar sobre los resultados del procedimiento almacenado
            for result in cursor.stored_results():
                rows = result.fetchall()  # Recuperar todas las filas del conjunto de resultados
                all_rows.extend(rows)     # Agregar las filas a la lista total
            return all_rows
        except Error as e:
            print(f"Error al consultar personas naturales: {e}")
        finally:
            cursor.close()
            connection.close()
            return []


# Función para insertar un nuevo pago
def insertar_pago(codigoPago, codigoDemanda, metodoDePago, fecha, monto, concepto, descripcion):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarPago', [codigoPago, codigoDemanda, metodoDePago, fecha, monto, concepto, descripcion])
            connection.commit()
            print("Pago insertado exitosamente")
        except Error as e:
            print(f"Error al insertar pago: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para actualizar un pago existente
def actualizar_pago(codigoPago, codigoDemanda, metodoDePago, fecha, monto, concepto, descripcion):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ActualizarPago', [codigoPago, codigoDemanda, metodoDePago, fecha, monto, concepto, descripcion])
            connection.commit()
            print("Pago actualizado exitosamente")
        except Error as e:
            print(f"Error al actualizar pago: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para eliminar un pago
def eliminar_pago(codigoPago):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('EliminarPago', [codigoPago])
            connection.commit()
            print("Pago eliminado exitosamente")
        except Error as e:
            print(f"Error al eliminar pago: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para consultar pagos por demanda
def consultar_pagos_por_demanda(codigoDemanda):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ConsultarPagosPorDemanda', [codigoDemanda])
            for result in cursor.stored_results():
                for row in result.fetchall():
                    print(row)
        except Error as e:
            print(f"Error al consultar pagos por demanda: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para insertar un nuevo contrato
def insertar_contrato(codigoContrato, codigoPago, estadoGeneral, descripcion):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarContrato', [codigoContrato, codigoPago, estadoGeneral, descripcion])
            connection.commit()
            print("Contrato insertado exitosamente")
        except Error as e:
            print(f"Error al insertar contrato: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para actualizar un contrato existente
def actualizar_contrato(codigoContrato, codigoPago, estadoGeneral, descripcion):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ActualizarContrato', [codigoContrato, codigoPago, estadoGeneral, descripcion])
            connection.commit()
            print("Contrato actualizado exitosamente")
        except Error as e:
            print(f"Error al actualizar contrato: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para eliminar un contrato
def eliminar_contrato(codigoContrato):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('EliminarContrato', [codigoContrato])
            connection.commit()
            print("Contrato eliminado exitosamente")
        except Error as e:
            print(f"Error al eliminar contrato: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para consultar contratos por pago
def consultar_contratos_por_pago(codigoPago):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ConsultarContratosPorPago', [codigoPago])
            for result in cursor.stored_results():
                for row in result.fetchall():
                    print(row)
        except Error as e:
            print(f"Error al consultar contratos por pago: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para insertar una nueva demanda
def insertar_demanda(CodigoDemanda, codigoContrato, EstadoDeProceso, descripcion, FechaInicio, FechaFin, Audiencia, EstadoDeJuicio):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarDemanda', [CodigoDemanda, codigoContrato, EstadoDeProceso, descripcion, FechaInicio, FechaFin, Audiencia, EstadoDeJuicio])
            connection.commit()
            print("Demanda insertada exitosamente")
        except Error as e:
            print(f"Error al insertar demanda: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para actualizar una demanda existente
def actualizar_demanda(CodigoDemanda, codigoContrato, EstadoDeProceso, descripcion, FechaInicio, FechaFin, Audiencia, EstadoDeJuicio):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ActualizarDemanda', [CodigoDemanda, codigoContrato, EstadoDeProceso, descripcion, FechaInicio, FechaFin, Audiencia, EstadoDeJuicio])
            connection.commit()
            print("Demanda actualizada exitosamente")
        except Error as e:
            print(f"Error al actualizar demanda: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para eliminar una demanda
def eliminar_demanda(CodigoDemanda):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('EliminarDemanda', [CodigoDemanda])
            connection.commit()
            print("Demanda eliminada exitosamente")
        except Error as e:
            print(f"Error al eliminar demanda: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para consultar demandas por contrato
def consultar_demandas_por_contrato(codigoContrato):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ConsultarDemandasPorContrato', [codigoContrato])
            for result in cursor.stored_results():
                for row in result.fetchall():
                    print(row)
        except Error as e:
            print(f"Error al consultar demandas por contrato: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para insertar una nueva área
def insertar_area(CodigoArea, Nombre, Descripcion, TipoDeProceso):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarArea', [CodigoArea, Nombre, Descripcion, TipoDeProceso])
            connection.commit()
            print("Área insertada exitosamente")
        except Error as e:
            print(f"Error al insertar área: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para actualizar un área existente
def actualizar_area(CodigoArea, Nombre, Descripcion, TipoDeProceso):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ActualizarArea', [CodigoArea, Nombre, Descripcion, TipoDeProceso])
            connection.commit()
            print("Área actualizada exitosamente")
        except Error as e:
            print(f"Error al actualizar área: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para eliminar un área
def eliminar_area(CodigoArea):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('EliminarArea', [CodigoArea])
            connection.commit()
            print("Área eliminada exitosamente")
        except Error as e:
            print(f"Error al eliminar área: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para consultar todas las áreas
def consultar_areas():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ConsultarAreas')
            for result in cursor.stored_results():
                for row in result.fetchall():
                    print(row)
        except Error as e:
            print(f"Error al consultar áreas: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para insertar una nueva etapa
def insertar_etapa(CodigoEtapa, Descripcion, FechaInicio, FechaFin, Estado, Nombre):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarEtapa', [CodigoEtapa, Descripcion, FechaInicio, FechaFin, Estado, Nombre])
            connection.commit()
            print("Etapa insertada exitosamente")
        except Error as e:
            print(f"Error al insertar etapa: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para actualizar una etapa existente
def actualizar_etapa(CodigoEtapa, Descripcion, FechaInicio, FechaFin, Estado, Nombre):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ActualizarEtapa', [CodigoEtapa, Descripcion, FechaInicio, FechaFin, Estado, Nombre])
            connection.commit()
            print("Etapa actualizada exitosamente")
        except Error as e:
            print(f"Error al actualizar etapa: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para eliminar una etapa
def eliminar_etapa(CodigoEtapa):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('EliminarEtapa', [CodigoEtapa])
            connection.commit()
            print("Etapa eliminada exitosamente")
        except Error as e:
            print(f"Error al eliminar etapa: {e}")
        finally:
            cursor.close()
            connection.close()

# Función para consultar todas las etapas
def consultar_etapas():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ConsultarEtapas')
            for result in cursor.stored_results():
                for row in result.fetchall():
                    print(row)
        except Error as e:
            print(f"Error al consultar etapas: {e}")
        finally:
            cursor.close()
            connection.close()


