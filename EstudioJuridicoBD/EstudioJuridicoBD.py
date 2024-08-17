import mysql.connector


def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="Gaibor_adm",
        password="macv2005",
        database="EstudioJuridicoBD"
    )

# Cargar datos desde la base de datos
def cargar_clientes():
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    conexion.close()
    return clientes

def cargar_abogados():
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Abogados")
    abogados = cursor.fetchall()
    conexion.close()
    return abogados

def cargar_casos():
    # Consulta SQL con JOIN para obtener nombres y apellidos de clientes y abogados
    query = """
    SELECT casos.id, clientes.nombre AS cliente_nombre, clientes.apellido_paterno AS cliente_apellido, 
           abogados.nombre AS abogado_nombre, abogados.apellido_paterno AS abogado_apellido,
           casos.descripcion, casos.etapa, casos.estado, casos.fechaInicio, casos.fechaFin, 
           casos.area, casos.contrato_id, casos.monto
    FROM Casos casos
    JOIN Clientes clientes ON casos.cliente_id = clientes.id
    JOIN Abogados abogados ON casos.abogado_id = abogados.id
    """
    
    # Conectarse a la base de datos
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    
    # Ejecutar la consulta
    cursor.execute(query)
    casos = cursor.fetchall()
    
    # Cerrar la conexión a la base de datos
    conexion.close()
    
    return casos

def cargar_contratos():
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Contratos")
    contratos = cursor.fetchall()
    conexion.close()
    return contratos

# Guardar datos en la base de datos
def guardar_cliente(nombre, tipo, correo, identificador, apellido_materno, apellido_paterno, fecha_nacimiento, telefono, es_natural=True, estado_civil=None, profesion=None, tipo_sociedad=None, sector_actividad=None):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO Clientes (nombre, tipo, correo, apellido_materno, apellido_paterno, fecha_nacimiento, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (nombre, tipo, correo, apellido_materno, apellido_paterno, fecha_nacimiento, telefono)
    )
    cliente_id = cursor.lastrowid
    if es_natural:
        cursor.execute(
            "INSERT INTO ClientesNaturales (id, cedula, estado_civil, profesion) VALUES (%s, %s, %s, %s)",
            (cliente_id, identificador, estado_civil, profesion)
        )
    else:
        cursor.execute(
            "INSERT INTO ClientesJuridicos (id, ruc, tipo_sociedad, sector_actividad) VALUES (%s, %s, %s, %s)",
            (cliente_id, identificador, tipo_sociedad, sector_actividad)
        )
    conexion.commit()
    conexion.close()
    return cliente_id


def guardar_abogado(cedula, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, area_enfoque):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO Abogados (cedula, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, area_enfoque) VALUES (%s, %s, %s, %s, %s, %s)",
        (cedula, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, area_enfoque)
    )
    abogado_id = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return abogado_id
    

def guardar_contrato(descripcion, fecha, pdf):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO Contratos (descripcion, fecha, pdf) VALUES (%s, %s, %s)",
        (descripcion, fecha, pdf)
    )
    contrato_id = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return contrato_id
   

def guardar_pago(monto, metodo_pago, descripcion, contrato_id):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO Pagos (monto, metodo_pago, descripcion, contrato_id) VALUES (%s, %s, %s, %s)",
        (monto, metodo_pago, descripcion, contrato_id)
    )
    pago_id = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return pago_id

    

def guardar_caso(cliente_id, abogado_id, contrato_id, descripcion, fechaInicio, fechaFin, area, etapa, estado,monto):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO Casos (cliente_id, abogado_id, contrato_id, descripcion, fechaInicio, fechaFin, area, etapa, estado,monto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (cliente_id, abogado_id, contrato_id, descripcion, fechaInicio, fechaFin, area, etapa, estado,monto)
    )
    conexion.commit()
    conexion.close()


    