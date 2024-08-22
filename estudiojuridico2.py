import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import dbconnections as dbc
from mysql.connector import Error
from tkcalendar import DateEntry

global connection

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

areas_y_etapas = {
        "Penal": ["Investigación", "Juicio", "Apelación"],
        "Infancia": ["Audiencia", "Custodia", "Mediación"],
        "Civil": ["Demanda", "Audiencia Preliminar", "Juicio"],
        "Laboral": ["Conciliación", "Juicio", "Sentencia"],
        "Tributario": ["Notificación", "Audiencia", "Resolución"]
        }
# Función para verificar el inicio de sesión
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == "abogadoprincipal" and contraseña == "1":
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        #cargar_datos_en_tabla()  # Cargar los casos en la tabla después del login exitoso
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def agregar_demanda():

    global cliente_id

    def agregar_cliente():

        def guardar_cliente():
                global cliente_id
                tipo_cliente = tipo_cliente_var.get()
                correo = entry_correo.get()
                nombre = entry_nombre.get()
                apellido_p = entry_apellido_paterno.get()
                apellido_m = entry_apellido_materno.get()
                fecha_nacimiento = entry_fecha_nacimiento.get()
                telefono = entry_telefono.get()

                if tipo_cliente == "Natural":
                    estado_civil = entry_estado_civil.get()
                    profesion = entry_profesion.get()
                    cedula = entry_cedula.get()
                    cliente_id=dbc.insertar_persona_natural(correo, nombre, apellido_p, apellido_m,
                              fecha_nacimiento, telefono, estado_civil, profesion)
                else:
                    tipo_sociedad = entry_tipo_sociedad.get()
                    sector_actividad = entry_sector_actividad.get()
                    ruc = entry_ruc.get()
                    cliente_id=dbc.insertar_persona_juridica(correo, nombre, apellido_p, apellido_m,
                              fecha_nacimiento, telefono, tipo_sociedad, sector_actividad, ruc)

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

    def actualizar_etapas(event):
        area_seleccionada = combobox_area.get()
        etapas = areas_y_etapas.get(area_seleccionada, [])
        combobox_etapa['values'] = etapas
        combobox_etapa.current(0)

    tk.Label(agregar_caso_window, text="Área:").pack(pady=5)
    opciones_area = list(areas_y_etapas.keys())
    combobox_area = ttk.Combobox(agregar_caso_window, values=opciones_area, state="readonly")
    combobox_area.pack()
    combobox_area.bind("<<ComboboxSelected>>", actualizar_etapas)

    tk.Label(agregar_caso_window, text="Etapa:").pack(pady=5)
    combobox_etapa = ttk.Combobox(agregar_caso_window, state="readonly")
    combobox_etapa.pack()

    
    tk.Label(agregar_caso_window, text="Estado:").pack(pady=5)
    estado_var = tk.StringVar()

    frame_estado = tk.Frame(agregar_caso_window)
    frame_estado.pack(pady=5)

    opciones_estado = [
        ("Inicio", "green"),
        ("En proceso", "yellow"),
        ("Finalizado", "red")
    ]
    
    for texto, color in opciones_estado:
        frame_opcion = tk.Frame(frame_estado)
        frame_opcion.pack(anchor='w')
        
        canvas = tk.Canvas(frame_opcion, width=20, height=20, highlightthickness=0)
        canvas.create_oval(2, 2, 18, 18, fill=color, outline=color)
        canvas.pack(side='left')
        
        radio_btn = tk.Radiobutton(frame_opcion, text=texto, variable=estado_var, value=texto)
        radio_btn.pack(side='left')

    tk.Label(agregar_caso_window, text="Fecha Inicio:").pack(pady=5)
    entry_fechaInicio= DateEntry(agregar_caso_window, date_pattern="yyyy-mm-dd",width=12, background='lightblue',
                            foreground='black', borderwidth=2)
    entry_fechaInicio.pack(pady=5)

    tk.Label(agregar_caso_window, text="Fecha Fin:").pack(pady=5)
    entry_fechaFin = DateEntry(agregar_caso_window, date_pattern="yyyy-mm-dd",width=12, background='lightblue',
                         foreground='white', borderwidth=2)
    entry_fechaFin.pack(pady=5)

    def limitarcaract(event):
        if len(entry_descripcion.get("1.0", tk.END)) > 150:
            entry_descripcion.delete("1.150", tk.END)
        
    tk.Label(agregar_caso_window, text="Descripción:").pack(pady=5)
    entry_descripcion = tk.Text(agregar_caso_window, width=50, height=10)
    entry_descripcion.pack()
    entry_descripcion.bind("<KeyRelease>", limitarcaract)

    botones_frame = tk.Frame(agregar_caso_window)
    botones_frame.pack(pady=20)

    btn_agregar_cliente = tk.Button(botones_frame, text="Agregar Cliente",command=agregar_cliente)
    btn_agregar_abogado = tk.Button(botones_frame, text="Agregar Abogado" )
    btn_agregar_contrato = tk.Button(botones_frame, text="Agregar Contrato")
    btn_guardar_caso = tk.Button(botones_frame, text="Guardar Caso" )

    btn_agregar_cliente.grid(row=0, column=0, padx=10)
    btn_agregar_abogado.grid(row=0, column=1, padx=10)
    btn_agregar_contrato.grid(row=0, column=2, padx=10)
    btn_guardar_caso.grid(row=0, column=3, padx=10)

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
tk.Button(main_frame, text="Agregar Caso",command=agregar_demanda).pack(side="left", padx=10)
tk.Button(main_frame, text="Editar Caso", command=lambda: print("Editar caso")).pack(side="left", padx=10)
tk.Button(main_frame, text="Borrar Caso", command=lambda: print("Borrar caso")).pack(side="left", padx=10)

tk.mainloop()