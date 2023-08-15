import customtkinter as ctk
from tkinter import filedialog
from cfdiConverter import create
import os
from PIL import Image


# Ruta del archivo de bloqueo
lock_file_path = "my_app.lock"

def check_lock():
    if os.path.exists(lock_file_path):
        return True
    else:
        # Crear el archivo de bloqueo
        with open(lock_file_path, "w") as lock_file:
            lock_file.write("locked")
        return False
    
def on_closing():
    # Eliminar el archivo de bloqueo al cerrar la aplicación
    if os.path.exists(lock_file_path):
        os.remove(lock_file_path)
    app.destroy()

if not check_lock():

    ctk.set_appearance_mode("light")  # Modes: system (default), light, dark
    # Themes: blue (default), dark-blue, green
    ctk.set_default_color_theme("green")

    app = ctk.CTk()  # create CTk window like you do with the Tk window
    app.geometry("405x420")
    app.iconbitmap('icon.ico')
    app.resizable(False,False)
    app.title("Convertidor CFDI a TXT DARWIN")
    app.protocol("WM_DELETE_WINDOW", on_closing)


    raw_add_first_icon = Image.open('icon.png')
    add_first_width, add_first_height = 290, 196
    resized_add_first_icon = raw_add_first_icon.resize(
        (add_first_width, add_first_height))
    converted_add_first_icon = ctk.CTkImage(resized_add_first_icon, size=(85, 70))

    add_first_icon = ctk.CTkLabel(
        app, image=converted_add_first_icon, text=None, fg_color="#ebebeb")
    add_first_icon.place(x=160, y=20)

    def set_focus_on_entry():
        no_pedimento.focus()

    def abrir_explorador():
        if no_factura.get() != "" and no_pedimento.get() != "" and codigo_impo.get() != "" and codigo_proveedor.get()!="" and entry_UMF.get()!="":
            opciones = {
                "title": "Selecciona un archivo XML",
                "filetypes": (("Archivos XML", "*.xml"),)
            }
            archivo = filedialog.askopenfilename(**opciones)
            nombre, extension = os.path.splitext(os.path.basename(archivo))

            if archivo != "" :
                create(archivo, nombre, no_pedimento.get(), no_factura.get().upper(),codigo_impo.get().upper(),codigo_proveedor.get().upper(),set_focus_on_entry,entry_UMF.get().upper(),checkbox_tra.get())
                clear_entry()

    def clear_entry():
        no_pedimento.delete(0, 'end')  
        codigo_impo.delete(0, 'end')  
        no_factura.delete(0, 'end') 
        codigo_proveedor.delete(0, 'end') 
        entry_UMF.delete(0, 'end') 
        checkbox_tra.deselect()
        

    ################# Restricciones de digitos,letras y longitud de entrys ########

    def validate_pedimento(value_if_allowed):
        if value_if_allowed == "":
            return True
        elif value_if_allowed.isdigit() and len(value_if_allowed) <= 15:
            return True
        else:
            return False
        
    def validate_codigo_impANDprovee(value_if_allowed):
        if value_if_allowed == "":
            return True
        elif value_if_allowed.isalnum() and len(value_if_allowed) <= 10:
            return True
        else:
            return False
        
    def validate_numero_factura(value_if_allowed):
        if value_if_allowed == "":
            return True
        elif value_if_allowed.isalnum() and len(value_if_allowed) <= 40:
            return True
        else:
            return False
        
    def validate_UMF(value_if_allowed):
        if value_if_allowed == "":
            return True
        elif value_if_allowed.isalnum() and len(value_if_allowed) <= 2:
            return True
        else:
            return False
    
    """ def validate_cant_tarifa(value_if_allowed):
        if value_if_allowed == "":
            return True
        elif value_if_allowed.isdigit() and len(value_if_allowed) <= 19:
            return True
        else:
            return False """
    
    #################################################################################

    ######## INPUTS #######

    #Numero de pedimento
    no_pedimento_CTkLabel = ctk.CTkLabel(
        app, text="No. Pedimento:", text_color="#595959")
    no_pedimento_CTkLabel.place(x=20, y=90)

    no_pedimento = ctk.CTkEntry(
        app, fg_color="white", corner_radius=7,  width=125)
    no_pedimento.place(x=20, y=120)
    no_pedimento.configure(validate="key",
                        validatecommand=(app.register(validate_pedimento), '%P'))

    #Numero de factura
    no_factura_CTkLabel = ctk.CTkLabel(
        app, text="No. Factura:", text_color="#595959")
    no_factura_CTkLabel.place(x=260, y=90)

    no_factura = ctk.CTkEntry(
        app, fg_color="white", corner_radius=7,  width=125)
    no_factura.place(x=260, y=120)
    no_factura.configure(validate="key",
                        validatecommand=(app.register(validate_numero_factura), '%P'))
    
    #Codigo del Importador
    codigo_impo_CTkLabel = ctk.CTkLabel(
        app, text="Código Cliente:", text_color="#595959")
    codigo_impo_CTkLabel.place(x=20, y=160)

    codigo_impo = ctk.CTkEntry(
        app, fg_color="white", corner_radius=7,  width=125)
    codigo_impo.place(x=20, y=190)
    codigo_impo.configure(validate="key",
                        validatecommand=(app.register(validate_codigo_impANDprovee), '%P'))

    #Codigo del proveedor
    codigo_proveedor_CTkLabel = ctk.CTkLabel(
        app, text="Código Proveedor:", text_color="#595959")
    codigo_proveedor_CTkLabel.place(x=260, y=160)

    codigo_proveedor = ctk.CTkEntry(
        app, fg_color="white", corner_radius=7,  width=125)
    codigo_proveedor.place(x=260, y=190)
    codigo_proveedor.configure(validate="key",
                        validatecommand=(app.register(validate_codigo_impANDprovee), '%P'))
    
    """ all_options = [
    "LTR", "LF", "NPR", "MIL", "NRL", "MTK", "GLL", "DZN", "DR", "BJ",
    "EA", "BL", "PK_1", "CS", "SA", "YRD", "LBR", "LTI", "BO", "SET",
    "C62_1", "FTK", "BX", "BE", "KGM", "TON"
    ] """
    """ #Cantidad Tarifa
    cant_tarifa_CTkLabel = ctk.CTkLabel(
        app, text="Cantidad Tarifa:", text_color="#595959")
    cant_tarifa_CTkLabel.place(x=20, y=230)

    cant_tarifa = ctk.CTkEntry(app, fg_color="white", corner_radius=7,  width=125)
    cant_tarifa.place(x=20, y=260)
    cant_tarifa.configure(validate="key",
                        validatecommand=(app.register(validate_cant_tarifa), '%P')) """
    
    #UMF
    UMF_CTkLabel = ctk.CTkLabel(
        app, text="UMF:", text_color="#595959")
    UMF_CTkLabel.place(x=20, y=230)

    entry_UMF = ctk.CTkEntry(app, fg_color="white", corner_radius=7,  width=125)
    entry_UMF.place(x=20, y=260)
    entry_UMF.configure(validate="key",
                        validatecommand=(app.register(validate_UMF), '%P'))
    
    #Checkbox Traducir Descipcion
    checkbox_tra = ctk.CTkCheckBox(master=app, fg_color="black", corner_radius=7,text="Traducir\nDescripcion", 
                                    onvalue="on", offvalue="off")
    checkbox_tra.place(x=260, y=260)
    
    #################################################################################

    # Use CTkButton instead of tkinter Button
    button = ctk.CTkButton(master=app, text="Cargar CFDI",
                        command=abrir_explorador)
    button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)
    #button.bind("<Tab>", abrir_explorador)

    app.mainloop()
