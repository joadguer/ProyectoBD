import mysql.connector
from mysql.connector import Error

# Configura la conexión a la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user= 'usuarioprincipal',  
            password= '1',  
            database='EstudioJuridicoDB'
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
        
def insertar_persona_juridica(correo_electronico, nombre, apellido_p, apellido_m,
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
            # Obtener el ID generado
            cursor.execute("SELECT LAST_INSERT_ID()")
            cliente_id = cursor.fetchone()[0]
            print("Persona jurídica insertada exitosamente con ID:", cliente_id)
            return cliente_id
        except Error as e:
            print(f"Error al insertar persona jurídica: {e}")
            return None
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
            # Obtener el ID generado
            cursor.execute("SELECT LAST_INSERT_ID()")
            cliente_id = cursor.fetchone()[0]
            print("Persona natural insertada exitosamente con ID:", cliente_id)
            return cliente_id
        except Error as e:
            print(f"Error al insertar persona natural: {e}")
            return None
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


#TODOO DE ABOGADOS
def insertar_abogado(cedula, nombre, apellido_m, apellido_p, fecha_nacimiento, area_enfoque):
  connection= create_connection()
  if connection:
        try:
          cursor = connection.cursor()
          cursor.callproc('InsertarAbogado', [
          cedula, nombre, apellido_m, apellido_p, fecha_nacimiento, area_enfoque])
          connection.commit()
          print("Abogado insertada exitosamente.")
        except Error as e:
          print(f"Error al insertar Abogado: {e}")
        finally:
            cursor.close()
            connection.close()


def actualizar_abogado(cedula, nombre, apellido_m, apellido_p, fecha_nacimiento, area_enfoque, usuario, clave):
    connection = create_connection(usuario, clave)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('ActualizarAbogado', [
                cedula, nombre, apellido_m, apellido_p, fecha_nacimiento, area_enfoque
            ])
            connection.commit()
            print("Abogado actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar abogado: {e}")
        finally:
            cursor.close()
            connection.close()
def eliminar_abogado(cedula, usuario, clave):
    connection = create_connection(usuario, clave)
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('EliminarAbogado', [cedula])
            connection.commit()
            print("Abogado eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar abogado: {e}")
        finally:
            cursor.close()
            connection.close()


# Función para insertar un nuevo pago
def insertar_pago( codigoContrato, metodoDePago, fecha, monto, descripcion):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarPago', [codigoContrato, metodoDePago, fecha, monto, descripcion])
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
def insertar_contrato(estadoGeneral, descripcion):
    connection = create_connection()
    contrato_id = None  # Inicializar contrato_id
    
    if connection:
        try:
            cursor = connection.cursor()
            # Llamar al procedimiento almacenado
            cursor.callproc('InsertarContrato', [estadoGeneral, descripcion])
            connection.commit()

            # Obtener el contrato_id del contrato recién insertado
            cursor.execute("SELECT LAST_INSERT_ID();")
            contrato_id = cursor.fetchone()[0]
            
            print(f"Contrato insertado exitosamente con ID: {contrato_id}")
        except Error as e:
            print(f"Error al insertar contrato: {e}")
        finally:
            cursor.close()
            connection.close()
    
    return contrato_id  # Devolver el contrato_id


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
def insertar_demanda(codigoContrato, descripcion, FechaInicio, FechaFin, Area, Etapa, Estado, Monto):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarDemanda', [codigoContrato, descripcion, FechaInicio, FechaFin, Area, Etapa, Estado, Monto])
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
def insertar_area( Nombre, Descripcion, TipoDeProceso):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarArea', [ Nombre, Descripcion, TipoDeProceso])
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
def insertar_etapa( Descripcion, FechaInicio, FechaFin, Estado, Nombre):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.callproc('InsertarEtapa', [ Descripcion, FechaInicio, FechaFin, Estado, Nombre])
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

import mysql.connector
from mysql.connector import Error

def obtener_monto_por_pago(codigoPago):
    try:
        # Conecta a la base de datos
        connection = create_connection()
        
        # Crea un cursor
        cursor = connection.cursor()
        out_param = cursor.callproc('ObtenerMontoPorPago', [codigoPago, 0])
        # Obtener el monto del parámetro de salida
        monto = out_param[1]
        # print(f"El monto del pago con ID {codigoPago} es: {monto}")
        return monto
            
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Ejemplo de uso
obtener_monto_por_pago(1)



def ejecutar_stored_procedure():
    try:
        # Conecta a la base de datos
        connection = create_connection()
        
        # Crea un cursor
        cursor = connection.cursor()

        # Llama al stored procedure
        cursor.callproc('obtener_datos_demanda')

        # Recoge los resultados
        results = cursor.stored_results()
        
        # Imprime los resultados
        for result in results:
            for row in result:
                print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cierra el cursor y la conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Llama a la función
ejecutar_stored_procedure()


