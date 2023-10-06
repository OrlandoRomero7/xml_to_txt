from tkinter import ttk
import tkinter as tk
import customtkinter as ctk
from query import obtenerProveedores

ventana_secundaria = None  # referencia global para la ventana secundaria
 
def mostrar_proveedores(app, codigo_impo, entry_UMF):
    global ventana_secundaria
    
    if ventana_secundaria and ventana_secundaria.winfo_exists():
        ventana_secundaria.focus()
        return

    def seleccionar_elemento(event):
        item = treeview.selection()[0]
        valores = treeview.item(item, "values")
        # valores[0] es el nombre, valores[1] es el código
        codigo_impo.delete(0, ctk.END)
        codigo_impo.insert(0, valores[0])
        ventana_secundaria.destroy()
        entry_UMF.focus_set()
        return "break"  # Para evitar el comportamiento predeterminado de Tab
    
    def actualizar_treeview(event):
        # Borrar los elementos actuales del Treeview
        for row in treeview.get_children():
            treeview.delete(row)

        # Obtener el texto ingresado en el Entry
        input_text = entrada_secundaria.get().lower()

        # Filtrar y agregar los resultados al Treeview
        for codigo, nombre in resultados:
            if input_text in nombre.lower():
                treeview.insert("", "end", values=(codigo, nombre))

    ventana_secundaria = ctk.CTkToplevel(app)
    ventana_secundaria.title("Proveedores")
    ventana_secundaria.geometry("600x300")
    ventana_secundaria.after(250,lambda:ventana_secundaria.iconbitmap('icon.ico'))
    ventana_secundaria.resizable(False,False)
    ventana_secundaria.attributes('-topmost', True)

    busqueda_CTkLabel = ctk.CTkLabel(
        ventana_secundaria, text="Búsqueda:", text_color="#595959")
    busqueda_CTkLabel.place(x=150, y=15)
    entrada_secundaria = ctk.CTkEntry(ventana_secundaria)
    entrada_secundaria.pack(pady=15)
    entrada_secundaria.bind("<KeyRelease>", actualizar_treeview)
    
    frame = ttk.Frame(ventana_secundaria)
    frame.pack(pady=15, padx=15, fill=tk.BOTH, expand=True)

    treeview = ttk.Treeview(frame, columns=("Código", "Nombre"), show="headings")
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=treeview.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    treeview.heading("Código", text="Código")
    treeview.heading("Nombre", text="Nombre")
    treeview.column("Código", width=100, stretch=tk.NO)
    treeview.column("Nombre", stretch=tk.YES)
    treeview.bind("<Double-1>", seleccionar_elemento)
    treeview.configure(yscrollcommand=scrollbar.set)

    for codigo,nombre  in resultados:
        treeview.insert("", "end", values=(codigo, nombre))

    ventana_secundaria.update_idletasks()

    #Reactivar la actualización de la GUI
    ventana_secundaria.update()

resultados = obtenerProveedores()
