import tkinter as tk

def mostrar_ventana_secundaria(app,codigo_impo):
    def actualizar_listbox(event):
        input_text = entrada_secundaria.get().lower()
        listbox.delete(0, tk.END)
        for nombre, clave in datos.items():
            if input_text in nombre.lower():
                listbox.insert(tk.END, nombre)

    def seleccionar_elemento(event):
        seleccionado = listbox.get(listbox.curselection())
        codigo_impo.delete(0, tk.END)
        codigo_impo.insert(0, seleccionado)
        ventana_secundaria.destroy()

    ventana_secundaria = tk.Toplevel(app)
    ventana_secundaria.title("Ventana Secundaria")

    entrada_secundaria = tk.Entry(ventana_secundaria)
    entrada_secundaria.pack(pady=15)
    entrada_secundaria.bind("<KeyRelease>", actualizar_listbox)

    listbox = tk.Listbox(ventana_secundaria, width=50, selectmode=tk.SINGLE)
    listbox.pack(pady=15, padx=15, fill=tk.BOTH, expand=True)
    listbox.bind("<<ListboxSelect>>", seleccionar_elemento)

    for nombre in datos.keys():
        listbox.insert(tk.END, nombre)

""" root = tk.Tk()
root.title("Ventana Principal")

entrada_principal = tk.Entry(root)
entrada_principal.pack(pady=15, padx=15, side="left", fill=tk.X, expand=True)

btn = tk.Button(root, text="Abrir", command=mostrar_ventana_secundaria)
btn.pack(pady=15, padx=15, side="right") """

# Datos para el Listbox con claves asociadas
datos = {
    "Perro": "P01",
    "Gato": "G01",
    "Elefante": "E01",
    "León": "L01",
    "Tigre": "T01",
    "Jirafa": "J01",
    "Hipopótamo": "H01",
    "Cebra": "C01"
}

#root.mainloop()
