import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# Definir archivos para guardar los datos
CLIENTES_FILE = "clientes.json"
CASOS_FILE = "casos.json"
ABOGADOS_FILE = "abogados.json"
CONTRATOS_FILE = "contratos.json"


# Función para cargar los datos de los clientes desde un archivo JSON
def cargar_clientes():
    if os.path.exists(CLIENTES_FILE):
        try:
            with open(CLIENTES_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

# Función para guardar los datos de los clientes en un archivo JSON
def guardar_clientes():
    with open(CLIENTES_FILE, "w") as file:
        json.dump(clientes, file, indent=4)

# Función para cargar los datos de los casos desde un archivo JSON
def cargar_casos():
    if os.path.exists(CASOS_FILE):
        try:
            with open(CASOS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

# Función para guardar los datos de los casos en un archivo JSON
def guardar_casos():
    with open(CASOS_FILE, "w") as file:
        json.dump(casos, file, indent=4)

# Función para cargar los datos de los abogados desde un archivo JSON
def cargar_abogados():
    if os.path.exists(ABOGADOS_FILE):
        try:
            with open(ABOGADOS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

# Función para guardar los datos de los abogados en un archivo JSON
def guardar_abogados():
    with open(ABOGADOS_FILE, "w") as file:
        json.dump(abogados, file, indent=4)


#Funcion para cargar los datos de los contratos desde un archivo JSON
def cargar_contratos():
    if os.path.exists(CONTRATOS_FILE):
        try:
            with open(CONTRATOS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

#Funcion para guardar los datos de los contratos en un archivo JSON
def guardar_contratos():
    with open(CONTRATOS_FILE, "w") as file:
        json.dump(contratos,file, indent=4)

# Cargar los datos de clientes, casos, abogados y contratos al iniciar la aplicación
clientes = cargar_clientes()
casos = cargar_casos()
abogados = cargar_abogados()
contratos = cargar_contratos()

# Obtener el siguiente ID disponible para clientes, casos y abogados
def obtener_siguiente_id(lista):
    if lista:
        return max(item["id"] for item in lista) + 1
    return 1

# Variable global para almacenar el cliente y el abogado seleccionados
nuevo_cliente = None
nuevo_abogado = None
nuevo_contrato = None



# Función para verificar el inicio de sesión
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == "abogado" and contraseña == "1234":
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        mostrar_casos()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para mostrar los casos en la tabla
def mostrar_casos():
    for item in tabla_casos.get_children():
        tabla_casos.delete(item)
    for caso in casos:
        cliente = next((c for c in clientes if c["id"] == caso["cliente"]), {})
        abogado = next((a for a in abogados if a["id"] == caso["abogado"]), {})
        contrato = next((b for b in contratos if b["id"] == caso["contrato"]), {})
        cliente_nombre = f'{cliente.get("nombre", "")} {cliente.get("apellidoPaterno", "")}'
        abogado_nombre = f'{abogado.get("nombre", "")} {abogado.get("apellidoPaterno", "")}'
        tabla_casos.insert("", "end", values=(
            caso["id"], 
            cliente_nombre, 
            caso["descripcion"], 
            caso.get("etapa",""),
            caso["estado"], 
            abogado_nombre,
            caso.get("fechaInicio", ""),
            caso.get("fechaFin", ""),
            contrato["id"],
            
        ))

# Función para agregar un caso
def agregar_caso():
    def guardar_caso():
        if nuevo_cliente is None:
            messagebox.showerror("Error", "Debe agregar un cliente antes de guardar el caso")
            return
        if nuevo_abogado is None:
            messagebox.showerror("Error", "Debe agregar un abogado antes de guardar el caso")
            return
        if nuevo_contrato is None:  
            messagebox.showerror("Error", "Debe agregar un contrato antes de guardar el caso")
        
        nuevo_caso = {
            "id": obtener_siguiente_id(casos),
            "cliente": nuevo_cliente["id"],
            "descripcion": entry_descripcion.get(),
            "estado": entry_estado.get(),
            "fechaInicio": entry_fechaInicio.get(),
            "fechaFin": entry_fechaFin.get(),
            "abogado": nuevo_abogado["id"],
            "contrato":nuevo_contrato["id"],
            "area": combobox_area.get(),
            "etapa":combobox_etapa.get()
        }
        
        casos.append(nuevo_caso)
        guardar_casos()
        agregar_caso_window.destroy()
        mostrar_casos()
    
    def agregar_abogado():
            global nuevo_abogado
            # Solo permite guardar el abogado después de completar los campos
            def guardar_abogado():
                global nuevo_abogado
                nuevo_abogado = {
                    "id": obtener_siguiente_id(abogados),
                    "cedula": entry_cedula_abogado.get(),
                    "nombre": entry_nombre_abogado.get(),
                    "apellidoPaterno": entry_apellido_paterno_abogado.get(),
                    "apellidoMaterno": entry_apellido_materno_abogado.get(),
                    "fechaNacimiento": entry_fecha_nacimiento_abogado.get(),
                    "areaEnfoque": entry_area_enfoque.get()
                }
                abogados.append(nuevo_abogado)
                guardar_abogados()
                agregar_abogado_window.destroy()
            
            agregar_abogado_window = tk.Toplevel(agregar_caso_window)
            agregar_abogado_window.title("Agregar Abogado")
            
            tk.Label(agregar_abogado_window, text="Cédula:").pack(pady=5)
            entry_cedula_abogado = tk.Entry(agregar_abogado_window)
            entry_cedula_abogado.pack()
            
            tk.Label(agregar_abogado_window, text="Nombre:").pack(pady=5)
            entry_nombre_abogado = tk.Entry(agregar_abogado_window)
            entry_nombre_abogado.pack()
            
            tk.Label(agregar_abogado_window, text="Apellido Paterno:").pack(pady=5)
            entry_apellido_paterno_abogado = tk.Entry(agregar_abogado_window)
            entry_apellido_paterno_abogado.pack()
            
            tk.Label(agregar_abogado_window, text="Apellido Materno:").pack(pady=5)
            entry_apellido_materno_abogado = tk.Entry(agregar_abogado_window)
            entry_apellido_materno_abogado.pack()
            
            tk.Label(agregar_abogado_window, text="Fecha de Nacimiento:").pack(pady=5)
            entry_fecha_nacimiento_abogado = tk.Entry(agregar_abogado_window)
            entry_fecha_nacimiento_abogado.pack()
            
            tk.Label(agregar_abogado_window, text="Área de Enfoque:").pack(pady=5)
            entry_area_enfoque = tk.Entry(agregar_abogado_window)
            entry_area_enfoque.pack()
            
            tk.Button(agregar_abogado_window, text="Guardar Abogado", command=guardar_abogado).pack(pady=20)
    
    areas_y_etapas = {
        "Penal": ["Investigación", "Juicio", "Apelación"],
        "Infancia": ["Audiencia", "Custodia", "Mediación"],
        "Civil": ["Demanda", "Audiencia Preliminar", "Juicio"],
        "Laboral": ["Conciliación", "Juicio", "Sentencia"],
        "Tributario": ["Notificación", "Audiencia", "Resolución"]
        }
    
    def agregar_contrato():
        
        global nuevo_contrato

        

        # Solo permite guardar el contrato después de completar los campos
        def guardar_contrato():
            global nuevo_contrato
            nuevo_contrato = {
                "id": obtener_siguiente_id(contratos),
                "Estado": entry_estado_contrato.get(),
                "Descripcion": entry_descripcion_contrato.get(),
                "Fecha": entry_fecha_contrato.get(),
            }
            contratos.append(nuevo_contrato)
            guardar_contratos()
            agregar_contrato_window.destroy()

        agregar_contrato_window = tk.Toplevel(agregar_caso_window)
        agregar_contrato_window.title("Agregar Contrato")

        tk.Label(agregar_contrato_window, text="Estado:").pack(pady=5)
        entry_estado_contrato = tk.Entry(agregar_contrato_window)
        entry_estado_contrato.pack()

        tk.Label(agregar_contrato_window, text="Descripcion:").pack(pady=5)
        entry_descripcion_contrato = tk.Entry(agregar_contrato_window)
        entry_descripcion_contrato.pack()
    

        tk.Label(agregar_contrato_window, text="Fecha:").pack(pady=5)
        entry_fecha_contrato = tk.Entry(agregar_contrato_window)
        entry_fecha_contrato.pack()

        tk.Button(agregar_contrato_window, text="Guardar Contrato", command=guardar_contrato).pack(pady=20)

    def agregar_cliente():
        global nuevo_cliente
        # Solo permite guardar el cliente después de completar los campos
        def guardar_cliente():
            global nuevo_cliente
            nuevo_cliente = {
                "id": obtener_siguiente_id(clientes),
                "tipo": tipo_cliente_var.get(),
                "correo": entry_correo.get(),
                "nombre": entry_nombre.get(),
                "apellidoPaterno": entry_apellido_paterno.get(),
                "apellidoMaterno": entry_apellido_materno.get(),
                "fechaNacimiento": entry_fecha_nacimiento.get(),
                "telefono": entry_telefono.get()
            }
            if nuevo_cliente["tipo"] == "Natural":
                nuevo_cliente.update({
                    "estadoCivil": entry_estado_civil.get(),
                    "profesion": entry_profesion.get(),
                    "cedula": entry_cedula.get()
                })
            else:
                nuevo_cliente.update({
                    "tipoSociedad": entry_tipo_sociedad.get(),
                    "sectorActividad": entry_sector_actividad.get(),
                    "ruc": entry_ruc.get()
                })
            
            clientes.append(nuevo_cliente)
            guardar_clientes()
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
        entry_fecha_nacimiento = tk.Entry(agregar_cliente_window)
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
    
    tk.Label(agregar_caso_window, text="Descripción:").pack(pady=5)
    entry_descripcion = tk.Entry(agregar_caso_window)
    entry_descripcion.pack()

    
    tk.Label(agregar_caso_window, text="Estado:").pack(pady=5)
    entry_estado = tk.Entry(agregar_caso_window)
    entry_estado.pack()

    tk.Label(agregar_caso_window, text="Fecha Inicio:").pack(pady=5)
    entry_fechaInicio = tk.Entry(agregar_caso_window)
    entry_fechaInicio.pack()

    tk.Label(agregar_caso_window, text="Fecha Fin:").pack(pady=5)
    entry_fechaFin = tk.Entry(agregar_caso_window)
    entry_fechaFin.pack()

    tk.Button(agregar_caso_window, text="Agregar Cliente", command=agregar_cliente).pack(pady=10)
    tk.Button(agregar_caso_window, text="Agregar Abogado", command=agregar_abogado).pack(pady=10)
    tk.Button(agregar_caso_window, text="Agregar Contrato", command= agregar_contrato).pack(pady=10)
    tk.Button(agregar_caso_window, text="Guardar Caso", command=guardar_caso).pack(pady=20)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Gestión Jurídica")
root.geometry("800x600")

# Crear el frame de inicio de sesión
login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Usuario:").pack(pady=10)
entry_usuario = tk.Entry(login_frame)
entry_usuario.pack()

tk.Label(login_frame, text="Contraseña:").pack(pady=10)
entry_contraseña = tk.Entry(login_frame, show="*")
entry_contraseña.pack()

tk.Button(login_frame, text="Iniciar Sesión", command=verificar_login).pack(pady=20)

# Crear el frame principal (que se muestra tras el login)
main_frame = tk.Frame(root)

# Crear la tabla para mostrar los casos
tabla_casos = ttk.Treeview(main_frame, columns=("id", "cliente", "descripcion", "etapa", "estado", "abogado", "fechaInicio", "fechaFin","contrato"), show="headings")

# Definir encabezados de columnas
tabla_casos.heading("id", text="ID Caso")
tabla_casos.heading("cliente", text="Cliente")
tabla_casos.heading("descripcion", text="Descripción")
tabla_casos.heading("etapa", text="Etapa")
tabla_casos.heading("estado", text="Estado")
tabla_casos.heading("abogado", text="Abogado")
tabla_casos.heading("fechaInicio", text="Fecha Inicio")
tabla_casos.heading("fechaFin", text="Fecha Fin")
tabla_casos.heading("contrato",text="Contrato")

tabla_casos.column("id", width=50)
tabla_casos.column("cliente", width=100)
tabla_casos.column("descripcion", width=150)
tabla_casos.column("etapa", width=100)
tabla_casos.column("estado", width=100)
tabla_casos.column("abogado", width=100)
tabla_casos.column("fechaInicio", width=50)
tabla_casos.column("fechaFin", width=50)
tabla_casos.column("contrato", width=50)

tabla_casos.pack(fill="both", expand=True, pady=20)

# Botones para agregar, editar, borrar casos
tk.Button(main_frame, text="Agregar Caso", command=agregar_caso).pack(side="left", padx=10)
tk.Button(main_frame, text="Editar Caso").pack(side="left", padx=10)
tk.Button(main_frame, text="Borrar Caso").pack(side="left", padx=10)

root.mainloop()
