import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import dbconnections as dbc
from mysql.connector import Error
from tkcalendar import DateEntry

connection = dbc.create_connection()

# Función para cargar los datos de los clientes desde la base de datos
def cargar_clientes():
    try:
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)  # Usa el cursor para obtener resultados como diccionarios
            clientesNaturales = dbc.obtener_clientesNaturales()
            clientesJuridicos = dbc.obtener_clientesJuridicos()

            clientes = clientesJuridicos + clientesNaturales
            
            # Recupera todos los resultados de la consulta
            return clientes
    
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return []

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Función para verificar el inicio de sesión
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == "abogado" and contraseña == "1234":
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        #cargar_datos_en_tabla()  # Cargar los casos en la tabla después del login exitoso
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


def agregar_demanda():

    global cliente_id
        
    def guardar_cliente():
            global cliente_id
            tipo_cliente = tipo_cliente_var.get()
            correo = entry_correo.get()
            nombre = entry_nombre.get()
            apellido_paterno = entry_apellido_paterno.get()
            apellido_materno = entry_apellido_materno.get()
            fecha_nacimiento = entry_fecha_nacimiento.get()
            telefono = entry_telefono.get()

            if tipo_cliente == "Natural":
                estado_civil = entry_estado_civil.get()
                profesion = entry_profesion.get()
                cedula = entry_cedula.get()
                cliente_id=dbc.insertar_persona_natural()
            else:
                tipo_sociedad = entry_tipo_sociedad.get()
                sector_actividad = entry_sector_actividad.get()
                ruc = entry_ruc.get()
                cliente_id=dbc.insertar_persona_juridica()

            messagebox.showinfo("Éxito", "Cliente agregado correctamente")
            agregar_cliente_window.destroy()

    agregar_cliente_window = tk.Toplevel(agregar_caso_window)
    agregar_cliente_window.title("Agregar Cliente")
        
    tk.Label(agregar_cliente_window, text="Tipo de Cliente:").pack(pady=5)
    tipo_cliente_var = tk.StringVar(value="Natural")
    tk.Radiobutton(agregar_cliente_window, text="Natural", variable=tipo_cliente_var, value="Natural").pack()
    tk.Radiobutton(agregar_cliente_window, text="Jurídico", variable=tipo_cliente_var, value="Jurídico").pack()
        
    tk.Label(agregar_cliente_window, text="Correo:").pack(pady=5)
    entry_correo = tk.Entry(agregar_cliente_window)
    entry_correo.pack()
        
    tk.Label(agregar_cliente_window, text="Nombre:").pack(pady=5)
    entry_nombre = tk.Entry(agregar_cliente_window)
    entry_nombre.pack()
        
    tk.Label(agregar_cliente_window, text="Apellido Paterno:").pack(pady=5)
    entry_apellido_paterno = tk.Entry(agregar_cliente_window)
    entry_apellido_paterno.pack()
        
    tk.Label(agregar_cliente_window, text="Apellido Materno:").pack(pady=5)
    entry_apellido_materno = tk.Entry(agregar_cliente_window)
    entry_apellido_materno.pack()
        
    tk.Label(agregar_cliente_window, text="Fecha de Nacimiento:").pack(pady=5)
    entry_fecha_nacimiento = DateEntry(agregar_cliente_window, date_pattern="yyyy-mm-dd", width=12, background='lightblue',
                           foreground='black', borderwidth=2)
    entry_fecha_nacimiento.pack()
        
    tk.Label(agregar_cliente_window, text="Teléfono:").pack(pady=5)
    entry_telefono = tk.Entry(agregar_cliente_window)
    entry_telefono.pack()
        
    # Campos adicionales para cliente natural
    natural_frame = tk.Frame(agregar_cliente_window)
    tk.Label(natural_frame, text="Estado Civil:").pack(pady=5)
    entry_estado_civil = tk.Entry(natural_frame)
    entry_estado_civil.pack()
        
    tk.Label(natural_frame, text="Profesión:").pack(pady=5)
    entry_profesion = tk.Entry(natural_frame)
    entry_profesion.pack()
        
    tk.Label(natural_frame, text="Cédula:").pack(pady=5)
    entry_cedula = tk.Entry(natural_frame)
    entry_cedula.pack()
        
    # Campos adicionales para cliente jurídico
    juridico_frame = tk.Frame(agregar_cliente_window)
    tk.Label(juridico_frame, text="Tipo de Sociedad:").pack(pady=5)
    entry_tipo_sociedad = tk.Entry(juridico_frame)
    entry_tipo_sociedad.pack()
        
    tk.Label(juridico_frame, text="Sector de Actividad:").pack(pady=5)
    entry_sector_actividad = tk.Entry(juridico_frame)
    entry_sector_actividad.pack()
        
    tk.Label(juridico_frame, text="RUC:").pack(pady=5)
    entry_ruc = tk.Entry(juridico_frame)
    entry_ruc.pack()
        
    def mostrar_campos_cliente(*args):
            if tipo_cliente_var.get() == "Natural":
                juridico_frame.pack_forget()
                natural_frame.pack(pady=10)
            else:
                natural_frame.pack_forget()
                juridico_frame.pack(pady=10)
        
    tipo_cliente_var.trace("w", mostrar_campos_cliente)
    mostrar_campos_cliente()
        
    tk.Button(agregar_cliente_window, text="Guardar Cliente", command=guardar_cliente).pack(pady=20)    

    agregar_caso_window = tk.Toplevel(root)
    agregar_caso_window.title("Agregar Caso")


# Crear ventana principal
root = tk.Tk()
root.title("Estudio Jurídico")
root.geometry("1200x720")


# Crear el frame de inicio de sesión
login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Usuario:").pack(pady=10)
entry_usuario = tk.Entry(login_frame)
entry_usuario.pack()

tk.Label(login_frame, text="Contraseña:").pack(pady=10)
entry_contraseña = tk.Entry(login_frame, show="*")
entry_contraseña.pack()

btn_login = tk.Button(login_frame, text="Iniciar Sesión", command=verificar_login)
btn_login.pack(pady=20)

# Crear frame principal que se mostrará tras el inicio de sesión exitoso
main_frame = tk.Frame(root)

# Crear tabla para mostrar los casos
tabla_casos = ttk.Treeview(main_frame, columns=("id", "cliente", "descripcion", "etapa", "estado", "abogado", "fechaInicio", "fechaFin","area", "contrato", "monto"), show="headings")

# Definir encabezados de columnas
tabla_casos.heading("id", text="ID Caso")
tabla_casos.heading("cliente", text="Cliente")
tabla_casos.heading("descripcion", text="Descripción")
tabla_casos.heading("etapa", text="Etapa")
tabla_casos.heading("estado", text="Estado")
tabla_casos.heading("abogado", text="Abogado")
tabla_casos.heading("fechaInicio", text="Fecha Inicio")
tabla_casos.heading("fechaFin", text="Fecha Fin")
tabla_casos.heading("area",text="Área")
tabla_casos.heading("contrato", text="Contrato")
tabla_casos.heading("monto", text="Monto")

# Configurar el ancho de las columnas
tabla_casos.column("id", width=50)
tabla_casos.column("cliente", width=100)
tabla_casos.column("descripcion", width=150)
tabla_casos.column("etapa", width=100)
tabla_casos.column("estado", width=100)
tabla_casos.column("abogado", width=100)
tabla_casos.column("fechaInicio", width=100)
tabla_casos.column("fechaFin", width=100)
tabla_casos.column("area",width=100)
tabla_casos.column("contrato", width=100)
tabla_casos.column("monto", width=100)

# Empaquetar la tabla en el frame principal
tabla_casos.pack(fill="both", expand=True)

# Botones para agregar, editar, borrar casos
tk.Button(main_frame, text="Agregar Caso").pack(side="left", padx=10)
tk.Button(main_frame, text="Editar Caso", command=lambda: print("Editar caso")).pack(side="left", padx=10)
tk.Button(main_frame, text="Borrar Caso", command=lambda: print("Borrar caso")).pack(side="left", padx=10)

tk.mainloop()