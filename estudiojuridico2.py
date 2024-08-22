import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import dbconnections as dbc
from mysql.connector import Error
import loginConection 

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






# # Función para verificar el inicio de sesión
# def verificar_login():
#     usuario = entry_usuario.get()
#     contraseña = entry_contraseña.get()
    
#     if usuario == "abogado" and contraseña == "1234":
#         login_frame.pack_forget()
#         main_frame.pack(fill="both", expand=True)
#         #cargar_datos_en_tabla()  # Cargar los casos en la tabla después del login exitoso
#     else:
#         messagebox.showerror("Error", "Usuario o contraseña incorrectos")

#Funcion para verificar al usuario de ingreso
def verificar_login():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    
    if loginConection.connect_to_database(usuario,contraseña):
        connection = dbc.create_connection(usuario, contraseña)
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        #cargar_datos_en_tabla()  # Cargar los casos en la tabla después del login exitoso
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")


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