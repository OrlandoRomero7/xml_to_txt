import xml.etree.ElementTree as ET
from datetime import datetime
from create_text_block import *
import sys
from pathlib import Path
import os
import shutil
import subprocess
from CTkMessagebox import CTkMessagebox
from translate import Translator

# Definir el espacio de nombres para el prefijo usado en el XML
namespace = {'ns': 'http://www.sat.gob.mx/ComercioExterior11'}
namespace2 = {'ns': 'http://www.sat.gob.mx/cfd/4'}

translator = Translator(to_lang="es")

def parse_xml501(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    operacion = root.find(
        './/ns:ComercioExterior',namespace).get('TipoOperacion') #2
    clave = root.find(
        './/ns:ComercioExterior',namespace).get('ClaveDePedimento') #3
    #numero_pedimento = '' #4
    """ referencia = root.find(
        './/ns:Destinatario/ns:Domicilio',namespace).get('Referencia') #17  """
    moneda = root.get('Moneda') #20
    uuid = root.find(
        './/{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital').get('UUID')

    return operacion, clave, moneda, uuid

def parse_xml505(xml_file):
    
    tree = ET.parse(xml_file)
    root = tree.getroot()
    folio = root.get('Folio')
    fecha = root.get('Fecha')[:10].replace('-', '')
    incoterm = root.find(
        './/ns:ComercioExterior',namespace).get('Incoterm')
    moneda = root.get('Moneda')
    total_usd = root.find(
        './/ns:ComercioExterior',namespace).get('TotalUSD')
    """ destinatario_nombre = root.find(
        './/ns:Destinatario',namespace).get('Nombre') """
    uuid = root.find(
        './/{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital').get('UUID')
    return folio, fecha, incoterm, moneda, total_usd,  uuid
    

def parse_xml551(xml_file,checkbox_tra):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    list_fracciones = []
    list_descripciones = []
    list_unidadMedidaComercial = []
    list_valorDolares = []
    list_noParte = []
    list_cantidadComercial = []
    uuid = root.find(
        './/{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital').get('UUID')
    mercancias = root.findall('.//ns:Mercancias/ns:Mercancia', namespace)
    conceptos = root.findall('.//ns:Conceptos/ns:Concepto', namespace2)
    pais_origen = root.find('.//ns:Receptor/ns:Domicilio',namespace).get('Pais')
    #pais_destino = root.find('.//ns:Destinatario/ns:Domicilio',namespace).get('Pais')
    pais_destino_elemento = root.find('.//ns:Destinatario/ns:Domicilio', namespace)

    if pais_destino_elemento is not None:
        pais_destino = pais_destino_elemento.get('Pais')
    else: 
        pais_destino = pais_origen
    
        

    moneda = root.get('Moneda')

    # Acceder a los atributos de los elementos encontrados
    for mercancia in mercancias:
        no_parte = mercancia.get('NoIdentificacion')
        fraccion_arancelaria = mercancia.get('FraccionArancelaria')     
        #unidadMedidaComercial = mercancia.get('UnidadAduana')      
        valor_en_dolares = mercancia.get('ValorDolares')  
        list_noParte.append(no_parte)   
        list_fracciones.append(fraccion_arancelaria)
        #list_unidadMedidaComercial.append(unidadMedidaComercial)
        list_valorDolares.append(valor_en_dolares)

    for concepto in conceptos:
        _descripcion = concepto.get('Descripcion')
        descripcion_formateada = _descripcion.replace('&#xA;', ' ').replace('\n', ' ').strip()
        if checkbox_tra == "on":
            descripcion_final= translator.translate(descripcion_formateada)
        else:
            descripcion_final = descripcion_formateada
        cantidad = concepto.get('Cantidad')
        list_descripciones.append(descripcion_final) 
        list_cantidadComercial.append(cantidad)
                
    return  list_noParte,list_fracciones, list_descripciones, list_cantidadComercial, list_valorDolares, pais_origen,pais_destino,moneda,uuid


# Load the XML file (replace 'example.xml' with the actual file path)

#xml_file= r'C:\Users\Orlando\Documents\XML_to_TXT\facturas\XEXX010101000FFCD0000000167.xml'
#xml_file = 'C:/Users/medin/Downloads/F-0000005283.xml'


def create(ruta,name_file,no_pedimento,no_factura,codigo_impo,codigo_proveedor,set_focus_on_entry,UMF,checkbox_tra,switch_var):
    try:
        xml_file = ruta
        # 501 ###########################################################################
        operacion, clave, moneda, uuid= parse_xml501(xml_file)
        text_block501 = create_text_block501(
            operacion, clave, no_pedimento,codigo_impo,no_factura, moneda, uuid, switch_var) 
        # 505 ###########################################################################
        folio, fecha, incoterm, moneda, total_usd, uuid = parse_xml505(
            xml_file)
        text_block505 = create_text_block505(
            folio, fecha, incoterm, moneda, total_usd, codigo_proveedor, uuid,switch_var,no_factura)
        # 511 #######################################################################
        text_block511 = create_text_block511(
            switch_var,no_factura)
        # 551 #######################################################################
        noParte,fraccion, descripcion, cantidadComercial, valor_dolares,pais_origen,pais_destino,moneda,uuid= parse_xml551(
            xml_file,checkbox_tra)
        text_block551 = create_text_block551(noParte,fraccion, descripcion,cantidadComercial,UMF,valor_dolares,pais_origen,pais_destino,moneda,no_factura,uuid,switch_var) 

        success_first_try = True 
    except Exception as e:
        set_focus_on_entry()
        success_first_try = False
        CTkMessagebox(title="Error al convertir", message="No se pudo convertir el archivo, puede que sea un archivo no admitido. O esta ingresando mas de un archivo", icon="cancel")
        

    if success_first_try:    
        ############### Guardar archivo #####################################
        # Ruta en la unidad de red
        try:
            network_folder = r'C:\Users\Orlando\Desktop\cfdiConvertidos'
            #network_folder = r'H:\Vantec\DARWIN\Facturas\In'
            #H:\Vantec\DARWIN\Facturas\In
            export_file_name = name_file + ".txt"
            export_txt_folder = os.path.join(network_folder, export_file_name)

            with open(export_txt_folder, 'w') as file:
                if(switch_var=="off"):
                    file.write(text_block501 + '\n' + text_block505 + '\n' + text_block551)
                else:
                    file.write(text_block501 + '\n' + text_block505 + '\n' + text_block511 +'\n' + text_block551)
            set_focus_on_entry()
            #CTkMessagebox(message="Se convirtio correctamente el archivo.",icon="check", option_1="Okay")
            
        
        except Exception as e:
            None
            #CTkMessagebox(title="Error al guardar", message="No se pudo guardar el archivo", icon="cancel")
        
    



