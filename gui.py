import customtkinter as ctk
from tkinter import filedialog
from cfdiConverter import create
import os
from PIL import Image

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("Convertidor XML a TXT")

""" img = Image.open("icon.png")
img = img.resize((50, 50))
img = ctk.CTkImage(img)
image_label = ctk.CTkLabel(master=app, image=img)
image_label.place(relx=0.3, rely=0.4)
 """
raw_add_first_icon = Image.open('icon.png')
add_first_width, add_first_height = 290, 196
resized_add_first_icon = raw_add_first_icon.resize(
    (add_first_width, add_first_height))
converted_add_first_icon = ctk.CTkImage(resized_add_first_icon, size=(85, 70))

add_first_icon = ctk.CTkLabel(
    app, image=converted_add_first_icon, text=None, fg_color="#4D5057")
add_first_icon.place(x=160, y=20)


def abrir_explorador():
    opciones = {
        "title": "Selecciona un archivo XML",
        "filetypes": (("Archivos XML", "*.xml"),)
    }
    archivo = filedialog.askopenfilename(**opciones)
    nombre, extension = os.path.splitext(os.path.basename(archivo))
    #print(nombre)
    
    if archivo != "" and no_factura !="" and no_pedimento!="":
        #print("Archivo XML seleccionado:", archivo)
        create(archivo,nombre,no_pedimento.get(),no_factura.get())

# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=app, text="Cargar CFDI", command=abrir_explorador)
button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

################# Restriccion de solo numero y longitud de no. pedimiento ########
def validate_pedimento(value_if_allowed):
    if value_if_allowed == "":
        return True
    elif value_if_allowed.isdigit() and len(value_if_allowed) <= 15:
        return True
    else:
        return False
#################################################################################

######## INPUTS ####### 
no_pedimento_CTkLabel = ctk.CTkLabel(
    app,text="No. Pedimento:", text_color="#595959")
no_pedimento_CTkLabel.place(x=30, y=90)

no_pedimento = ctk.CTkEntry(
    app, fg_color="black", corner_radius=7,  width=125)
no_pedimento.place(x=20, y=120)
no_pedimento.configure(validate="key",
                           validatecommand=(app.register(validate_pedimento), '%P'))


no_factura_CTkLabel = ctk.CTkLabel(
    app,text="No. Factura:", text_color="#595959")
no_factura_CTkLabel.place(x=260, y=90)

no_factura = ctk.CTkEntry(
    app, fg_color="black", corner_radius=7,  width=125)
no_factura.place(x=260, y=120)
#################################################################################

""" ################### NAME ###############################
first_name_CTkLabel = ctk.CTkLabel(
    root, text="Nombre:", font=("NotoSans-Bold", 20, "bold"), text_color="#595959")
first_name_CTkLabel.place(x=256, y=312,)

name_field = ctk.CTkEntry(
    root, fg_color="white", corner_radius=7,  width=170, font=("Amiko", 15))
name_field.place(x=350, y=313,)
name_field.configure(validate="key",
                           validatecommand=(root.register(validate_name_input), '%P')) """

app.mainloop()