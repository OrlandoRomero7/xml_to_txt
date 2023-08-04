import xml.etree.ElementTree as ET
from datetime import datetime
from create_text_block import *
import sys

# Definir el espacio de nombres para el prefijo usado en el XML
namespace = {'ns': 'http://www.sat.gob.mx/ComercioExterior11'}
namespace2 = {'ns': 'http://www.sat.gob.mx/cfd/4'}

def parse_xml501(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    operacion = root.find(
        './/ns:ComercioExterior',namespace).get('TipoOperacion') #2
    clave = root.find(
        './/ns:ComercioExterior',namespace).get('ClaveDePedimento') #3
    #numero_pedimento = '' #4
    referencia = root.find(
        './/ns:Destinatario/ns:Domicilio',namespace).get('Referencia') #17
    moneda = root.get('Moneda') #20

    return operacion, clave, referencia, moneda

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

    destinatario_nombre = root.find(
        './/ns:Destinatario',namespace).get('Nombre')

    uuid = root.find(
        './/{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital').get('UUID')

    return folio, fecha, incoterm, moneda, total_usd,  destinatario_nombre, uuid,

def parse_xml551(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    list_fracciones = []
    list_descripciones = []
    list_unidadMedidaComercial = []
    list_valorDolares = []

    mercancias = root.findall('.//ns:Mercancias/ns:Mercancia', namespace)
    conceptos = root.findall('.//ns:Conceptos/ns:Concepto', namespace2)

    # Acceder a los atributos de los elementos encontrados
    for mercancia in mercancias:
        fraccion_arancelaria = mercancia.get('FraccionArancelaria')     
        unidadMedidaComercial = mercancia.get('UnidadAduana')      
        valor_en_dolares = mercancia.get('ValorDolares')     
        list_fracciones.append(fraccion_arancelaria)
        list_unidadMedidaComercial.append(unidadMedidaComercial)
        list_valorDolares.append(valor_en_dolares)

    for descripcion in conceptos:
        _descripcion = descripcion.get('Descripcion')
        list_descripciones.append(_descripcion) 
                #2              #3                      #7
    return  list_fracciones, list_descripciones, list_unidadMedidaComercial, list_valorDolares


# Load the XML file (replace 'example.xml' with the actual file path)
xml_file = 'C:/Users/Orlando/Documents/TxtCreator/404363-Soles_PRODD.xml'

#xml_file = 'C:/Users/medin/Downloads/F-0000005283.xml'

# 501 ###########################################################################
operacion, clave, referencia, moneda = parse_xml501(xml_file)

text_block501 = create_text_block501(
    operacion, clave, referencia, moneda)

# 505 ###########################################################################
folio, fecha, incoterm, moneda, total_usd, destinatario_nombre, uuid = parse_xml505(
    xml_file)

text_block505 = create_text_block505(
    folio, fecha, incoterm, moneda, total_usd,  destinatario_nombre, uuid)

# 551 #######################################################################
fraccion, descripcion, unidad_medida, valor_dolares= parse_xml551(
    xml_file)

text_block551 = create_text_block551(fraccion, descripcion, unidad_medida, valor_dolares)  


with open('archivo_salida.txt', 'w') as file:
    print(text_block501 + '\n' + text_block505 + '\n' + text_block551)
    file.write(text_block501 + '\n' + text_block505 + '\n' + text_block551)
    # Restaurar la salida estándar a su valor original (consola)
    sys.stdout = sys.__stdout__
