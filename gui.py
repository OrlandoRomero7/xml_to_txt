import customtkinter as ctk
from tkinter import filedialog
from cfdiConverter import create
import os
from PIL import Image
from tkinterdnd2 import DND_FILES
from CTkMessagebox import CTkMessagebox
from selectClient import mostrar_clientes
from selectSuppliers import mostrar_proveedores
import pickle

# Ruta del archivo de bloqueo
lock_file_path = "my_app.lock"
abrir="yes"
filepath = ""

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
    app.geometry("425x420")
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

    def abrir_explorador(filepath,abrir):
        if (no_factura.get() != "" or switch_var.get()=="on") and (no_pedimento.get() != "" and codigo_impo.get() != "" and codigo_proveedor.get()!="" and entry_UMF.get()!=""):
            
            if abrir=="yes":
                opciones = {
                "title": "Selecciona un archivo XML",
                "filetypes": (("Archivos XML", "*.xml"),),
                }
                archivo = filedialog.askopenfilename(**opciones)
                nombre, extension = os.path.splitext(os.path.basename(archivo))
            elif abrir=="no":
                archivo = filepath
                nombre, extension = os.path.splitext(os.path.basename(archivo))

            if archivo != "" :
                #if(checkbox_mar.get()=="on")
                try:
                    create(archivo, nombre, no_pedimento.get(), no_factura.get().upper(),codigo_impo.get().upper(),codigo_proveedor.get().upper(),set_focus_on_entry,entry_UMF.get().upper(),checkbox_tra.get(),switch_var.get())
                    clear_entry()
                except Exception as e:
                    None

    def clear_entry():
        no_pedimento.delete(0, 'end')  
        codigo_impo.delete(0, 'end')  
        codigo_proveedor.delete(0, 'end') 
        entry_UMF.delete(0, 'end') 
        checkbox_tra.deselect()
        #checkbox_mar.deselect()
        #no_factura.configure(state='normal')
        no_factura.delete(0, 'end') 
        #check_var.set("false")
        

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
        
    # def checkbox_event_mar():
    #     if check_var.get() == "on":
    #         no_factura.delete(0, 'end') 
    #         no_factura.configure(state='disabled')
            
    #     else:
    #         no_factura.configure(state='normal')

    def switch_event():
        if(switch_var.get()=="on"):
            switch.configure(text="Si")
            no_factura.delete(0, 'end') 
            #no_factura.configure(state='disabled')
        else:
            switch.configure(text="No")
            #no_factura.configure(state='normal')
        # Guardar el estado en un archivo pickle
        with open("switch_state.pkl", "wb") as file:
            pickle.dump(switch_var.get(), file)


    
    """ def validate_cant_tarifa(value_if_allowed):
        if value_if_allowed == "":
            return True
        elif value_if_allowed.isdigit() and len(value_if_allowed) <= 19:
            return True
        else:
            return False """
    
    
    
    #################################################################################
    
    ############################# SWITCH ########################################
    switch_CTkLabel = ctk.CTkLabel(
        app, text="Maritimo", text_color="#595959")
    switch_CTkLabel.place(x=20, y=40)
    switch_var = ctk.StringVar(value="on")
    switch = ctk.CTkSwitch(master=app,text="Si",variable=switch_var, command=switch_event,onvalue="on", offvalue="off")
    switch.place(x=20, y=65)

    # Intentar cargar el estado anterior desde el archivo pickle
    try:
        with open("switch_state.pkl", "rb") as file:
            saved_state = pickle.load(file)
            switch_var.set(saved_state)
            if(switch_var.get()=="on"):
                switch.configure(text="Si")
            else:
                switch.configure(text="No")
    except FileNotFoundError:
        pass  # El archivo aún no existe
    
    

    ################# INPUTS #######################

    #Numero de pedimento
    no_pedimento_CTkLabel = ctk.CTkLabel(
        app, text="No. Pedimento:", text_color="#595959")
    no_pedimento_CTkLabel.place(x=20, y=90)

    no_pedimento = ctk.CTkEntry(
        app, fg_color="white", corner_radius=7,  width=125)
    no_pedimento.place(x=20, y=120)
    no_pedimento.configure(validate="key",
                        validatecommand=(app.register(validate_pedimento), '%P'))
    
    #Maritimo
    # mar_CTkLabel = ctk.CTkLabel(
    #     app, text="Maritimo", text_color="#595959")
    # mar_CTkLabel.place(x=260, y=230)
    # check_var = ctk.StringVar(value="off")
    # checkbox_mar = ctk.CTkCheckBox(master=app, fg_color="black", corner_radius=7,text="", variable=check_var,
    #                                 onvalue="on", offvalue="off",command=checkbox_event_mar)
    # checkbox_mar.place(x=270, y=260)

    #Numero de factura
    no_factura_CTkLabel = ctk.CTkLabel(
        app, text="No. Factura:", text_color="#595959")
    no_factura_CTkLabel.place(x=260, y=90)

    no_factura = ctk.CTkEntry(
        app, fg_color="white", corner_radius=7,  width=125)
    no_factura.place(x=260, y=120)
    no_factura.configure(validate="key",
                        validatecommand=(app.register(validate_numero_factura), '%P'))
    # if(switch_var.get()=="on"):
    #     no_factura.configure(state='disabled')

    #Codigo del Importador
    def activate_button_provee(event):
        mostrar_clientes(app,codigo_impo,codigo_proveedor)

    codigo_impo_CTkLabel = ctk.CTkLabel(
        app, text="Código Cliente:", text_color="#595959")
    codigo_impo_CTkLabel.place(x=20, y=160)

    codigo_impo = ctk.CTkEntry(
        app, fg_color="white", corner_radius=7,  width=125)
    codigo_impo.place(x=20, y=190)
    codigo_impo.configure(validate="key",
                        validatecommand=(app.register(validate_codigo_impANDprovee), '%P'))
    codigo_impo.bind("<Tab>", activate_button_provee)
    button_cli = ctk.CTkButton(app, text="+",width=25,height=25,command=lambda: mostrar_clientes(app,codigo_impo,codigo_proveedor))
    button_cli.place(x=150, y=190)
    

    def activate_button_clients(event):
        mostrar_proveedores(app,codigo_proveedor,entry_UMF)

    #Codigo del proveedor
    codigo_proveedor_CTkLabel = ctk.CTkLabel(
        app, text="Código Proveedor:", text_color="#595959")
    codigo_proveedor_CTkLabel.place(x=260, y=160)
    
    codigo_proveedor = ctk.CTkEntry(
        app, fg_color="white", corner_radius=7,  width=125)
    codigo_proveedor.place(x=260, y=190)
    codigo_proveedor.configure(validate="key",
                        validatecommand=(app.register(validate_codigo_impANDprovee), '%P'))
    codigo_proveedor.bind("<Tab>", activate_button_clients)
    button_provee = ctk.CTkButton(app, text="+",width=25,height=25,command=lambda: mostrar_proveedores(app,codigo_proveedor,entry_UMF))
    button_provee.place(x=390, y=190)
    
    
    #UMF
    UMF_CTkLabel = ctk.CTkLabel(
        app, text="UMF:", text_color="#595959")
    UMF_CTkLabel.place(x=20, y=230)

    entry_UMF = ctk.CTkEntry(app, fg_color="white", corner_radius=7,  width=125)
    entry_UMF.place(x=20, y=260)
    entry_UMF.configure(validate="key",
                        validatecommand=(app.register(validate_UMF), '%P'))
    
    #Checkbox Traducir Descipcion
    tra_CTkLabel = ctk.CTkLabel(
        app, text="Traducir\nDescripción", text_color="#595959")
    tra_CTkLabel.place(x=320, y=230)
    checkbox_tra = ctk.CTkCheckBox(master=app, fg_color="black", corner_radius=7,text="", 
                                    onvalue="on", offvalue="off")
    checkbox_tra.place(x=340, y=260)
    
    #################################################################################

    def handle_drop(event):
        global abrir,filepath
        abrir="no"
        filepath = event.data.replace("{", "").replace("}", "")

        # Check if the dropped file has the desired extension (e.g., '.txt')
        desired_extension = '.xml'  # Change this to the desired extension
        if filepath.lower().endswith(desired_extension):
            abrir_explorador(filepath,abrir)
        else:
            CTkMessagebox(title="Formato no admitido", message="Archivo incorrecto. Debe ser de tipo {}".format(desired_extension), icon="cancel")
            
        abrir="yes"
        
    # Use CTkButton instead of tkinter Button
    button = ctk.CTkButton(master=app, text="Cargar CFDI",
                        command=lambda: abrir_explorador(filepath,abrir))
    button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)
    #button.bind("<Tab>", abrir_explorador)

    raw_add_first_icon = Image.open(r'pasar.jpg')
    add_first_width, add_first_height = 202, 42
    resized_add_first_icon = raw_add_first_icon.resize(
        (add_first_width, add_first_height))
    converted_add_first_icon = ctk.CTkImage(resized_add_first_icon, size=(202, 40))

    add_first_icon = ctk.CTkLabel(
        app, image=converted_add_first_icon, text=None, fg_color="#4D5057")
    add_first_icon.place(relx=0.5, rely=0.91, anchor=ctk.CENTER)
    #add_first_icon.place(x=100, y=360)

    add_first_icon.drop_target_register(DND_FILES)
    add_first_icon.dnd_bind('<<Drop>>', handle_drop)


    app.mainloop()
