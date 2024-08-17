import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import filedialog
import EstudioJuridicoBD
from tkcalendar import DateEntry

# Función para verificar el inicio de sesión
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if usuario == "abogado" and contraseña == "1234":
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        cargar_datos_en_tabla()  # Cargar los casos en la tabla después del login exitoso
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def cargar_datos_en_tabla():
    tabla_casos.delete(*tabla_casos.get_children())  # Limpiar la tabla antes de insertar nuevos datos
    casos = EstudioJuridicoBD.cargar_casos()
    for caso in casos:
        tabla_casos.insert("", "end", values=(
            caso["id"], 
            f'{caso["cliente_nombre"]} {caso["cliente_apellido"]}', 
            caso["descripcion"], 
            caso["etapa"], 
            caso["estado"], 
            f'{caso["abogado_nombre"]} {caso["abogado_apellido"]}', 
            caso["fechaInicio"], 
            caso["fechaFin"], 
            caso["area"],
            caso["contrato_id"], 
            caso["monto"]
        ))


areas_y_etapas = {
        "Penal": ["Investigación", "Juicio", "Apelación"],
        "Infancia": ["Audiencia", "Custodia", "Mediación"],
        "Civil": ["Demanda", "Audiencia Preliminar", "Juicio"],
        "Laboral": ["Conciliación", "Juicio", "Sentencia"],
        "Tributario": ["Notificación", "Audiencia", "Resolución"]
        }


def agregar_caso():

    global cliente_id, abogado_id, contrato_id

    def agregar_cliente():

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
                cliente_id=EstudioJuridicoBD.guardar_cliente(
                    nombre, tipo_cliente, correo, cedula, apellido_materno, apellido_paterno, fecha_nacimiento, telefono, es_natural=True, estado_civil=estado_civil, profesion=profesion
                )
            else:
                tipo_sociedad = entry_tipo_sociedad.get()
                sector_actividad = entry_sector_actividad.get()
                ruc = entry_ruc.get()
                cliente_id=EstudioJuridicoBD.guardar_cliente(
                    nombre, tipo_cliente, correo, ruc, apellido_materno, apellido_paterno, fecha_nacimiento, telefono, es_natural=False, tipo_sociedad=tipo_sociedad, sector_actividad=sector_actividad
                )

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


    def agregar_contrato():
        global contrato_id
        agregar_contrato_window = tk.Toplevel(agregar_caso_window)
        agregar_contrato_window.title("Agregar Contrato")
        pdf_contenido = None 
        def limitarcaract(event):
            if len(entry_descripcion_contrato.get("1.0",tk.END))>150:
                entry_descripcion_contrato.delete("1.150",tk.END)

        def seleccionar_pdf():
            nonlocal pdf_contenido
            archivo_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if archivo_pdf:
                with open(archivo_pdf, "rb") as archivo:
                   pdf_contenido = archivo.read()
                   messagebox.showinfo("Exito","Subido correctamente")

        def guardar_contrato():
            global contrato_id
            descripcion= entry_descripcion.get("1.0", tk.END).strip() 
            fecha = entry_fecha_contrato.get()

            if pdf_contenido:
                contrato_id = EstudioJuridicoBD.guardar_contrato(descripcion, fecha, pdf_contenido)
                messagebox.showinfo("Éxito", "Contrato guardado correctamente")
                agregar_contrato_window.destroy()

                agregar_pago(contrato_id)
                agregar_contrato_window.destroy()
            else:
                messagebox.showerror("Error","Debe seleccionar un archivo PDF")

        tk.Label(agregar_contrato_window, text="Descripcion:").pack(pady=5)
        entry_descripcion_contrato = tk.Text(agregar_contrato_window,width=50,height=10)
        entry_descripcion_contrato.pack()
        entry_descripcion_contrato.bind("<KeyRelease>", limitarcaract)
    
        tk.Label(agregar_contrato_window, text="Fecha:").pack(pady=5)
        entry_fecha_contrato = DateEntry(agregar_contrato_window,date_pattern="yyyy-mm-dd",width=12, background='lightblue',
                            foreground='black', borderwidth=2)
        entry_fecha_contrato.pack()

        tk.Button(agregar_contrato_window, text="Seleccionar PDF", command=seleccionar_pdf).pack(pady=10)
        tk.Button(agregar_contrato_window, text="Guardar Contrato",command=guardar_contrato).pack(pady=20)
    
    def agregar_pago(contrato_id):
        def guardar_pago():
            monto = entry_monto_pago.get()
            metodo_pago = metodo_pago_var.get()
            descripcion = entry_descripcion_pago.get("1.0", tk.END).strip()

            if contrato_id:  # Verificar que el contrato_id esté disponible
                try:
                    EstudioJuridicoBD.guardar_pago(monto, metodo_pago, descripcion, contrato_id)
                    messagebox.showinfo("Éxito", "Pago guardado correctamente")
                    agregar_pago_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar el pago: {e}")
            else:
                messagebox.showerror("Error", "No se pudo identificar el contrato")

                # Crear la ventana para agregar un pago
        agregar_pago_window = tk.Toplevel()
        agregar_pago_window.title("Agregar Pago")

        # Campo para el monto del pago
        tk.Label(agregar_pago_window, text="Monto:").pack(pady=5)
        entry_monto_pago = tk.Entry(agregar_pago_window)
        entry_monto_pago.pack()

        # Campo para la fecha del pago
        tk.Label(agregar_pago_window, text="Fecha:").pack(pady=5)
        entry_fecha_pago = DateEntry(agregar_pago_window, date_pattern="yyyy-mm-dd", width=12, background='lightblue',
                                    foreground='black', borderwidth=2)
        entry_fecha_pago.pack()

        # Campo para seleccionar el método de pago
        tk.Label(agregar_pago_window, text="Método de Pago:").pack(pady=5)
        opciones_pago = ["Efectivo", "Transferencia", "Tarjeta", "Otro"]
        metodo_pago_var = tk.StringVar(value=opciones_pago[0])
        menu_metodo_pago = tk.OptionMenu(agregar_pago_window, metodo_pago_var, *opciones_pago)
        menu_metodo_pago.pack()

        # Campo para la descripción del pago
        tk.Label(agregar_pago_window, text="Descripción:").pack(pady=5)
        entry_descripcion_pago = tk.Text(agregar_pago_window, width=50, height=10)
        entry_descripcion_pago.pack()

        # Botón para guardar el pago
        tk.Button(agregar_pago_window, text="Guardar Pago", command=lambda:guardar_pago()).pack(pady=20)

    def agregar_abogado():
        global abogado_id
        def guardar_abogado():
            global abogado_id
            cedula = entry_cedula_abogado.get()
            nombre = entry_nombre_abogado.get()
            apellido_paterno = entry_apellido_paterno_abogado.get()
            apellido_materno = entry_apellido_materno_abogado.get()
            fecha_nacimiento = entry_fecha_nacimiento_abogado.get()
            area_enfoque = entry_area_enfoque.get()

            # Guardar en la base de datos
            abogado_id=EstudioJuridicoBD.guardar_abogado(cedula,nombre,apellido_paterno,apellido_materno,fecha_nacimiento,area_enfoque)
            messagebox.showinfo("Éxito", "Abogado agregado correctamente")
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
        entry_fecha_nacimiento_abogado = DateEntry(agregar_abogado_window,date_pattern="yyyy-mm-dd",width=12, background='lightblue',
                    foreground='black', borderwidth=2)
        entry_fecha_nacimiento_abogado.pack()
    
            
        tk.Label(agregar_abogado_window, text="Área de Enfoque:").pack(pady=5)
        entry_area_enfoque = tk.Entry(agregar_abogado_window)
        entry_area_enfoque.pack()
            
        tk.Button(agregar_abogado_window, text="Guardar Abogado",command=guardar_abogado).pack(pady=20)
    
    def obtener_monto_pago(contrato_id):
        # Esta función debería consultar la base de datos para obtener el monto del pago asociado al contrato
        conexion = EstudioJuridicoBD.conectar_bd()
        cursor = conexion.cursor()
        cursor.execute("SELECT monto FROM Pagos WHERE contrato_id = %s", (contrato_id,))
        resultado = cursor.fetchone()
        conexion.close()
        return resultado[0] if resultado else None
    
    def guardar_caso():
            
        global cliente_id, abogado_id, contrato_id   
        descripcion= entry_descripcion.get("1.0",tk.END).strip()
        fechaInicio = entry_fechaInicio.get()
        fechaFin = entry_fechaFin.get()
        area = combobox_area.get()
        etapa = combobox_etapa.get()
        estado = estado_var.get()
        monto = obtener_monto_pago(contrato_id)
            
        try:
            # Guardar el caso en la base de datos
            EstudioJuridicoBD.guardar_caso(cliente_id, abogado_id, contrato_id, descripcion, fechaInicio, fechaFin, area, etapa, estado, monto)
            messagebox.showinfo("Éxito", "Caso guardado correctamente")
            cargar_datos_en_tabla()
            agregar_caso_window.destroy()  # Cerrar la ventana de agregar caso
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el caso: {str(e)}")
    
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
    btn_agregar_abogado = tk.Button(botones_frame, text="Agregar Abogado",command=agregar_abogado )
    btn_agregar_contrato = tk.Button(botones_frame, text="Agregar Contrato",command=agregar_contrato)
    btn_guardar_caso = tk.Button(botones_frame, text="Guardar Caso",command=guardar_caso )

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
tk.Button(main_frame, text="Agregar Caso", command=agregar_caso).pack(side="left", padx=10)
tk.Button(main_frame, text="Editar Caso", command=lambda: print("Editar caso")).pack(side="left", padx=10)
tk.Button(main_frame, text="Borrar Caso", command=lambda: print("Borrar caso")).pack(side="left", padx=10)

tk.mainloop()