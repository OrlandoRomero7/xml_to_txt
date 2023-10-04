from tqdm import tqdm

def create_text_block501(operacion, clave, no_pedimento,codigo_impo,no_factura, moneda, uuid, checkbox_mar):
    fields = [''] * 24

    fields[0] = "501"       #1 Tipo de Registro
    fields[1] = operacion   #2 Tipo de Operacion
    fields[2] = clave       #3 Clave de Pedimento
    fields[3] = no_pedimento       #4 Numero de Pedimento
    fields[4] = codigo_impo
    if(checkbox_mar == "on"):
        no_factura=uuid
    fields[16] = no_factura  #17 Referencia
    fields[19] = moneda      #20 Pais Moneda ?

    return f"{'|'.join(fields)}||"

def create_text_block551(noParte, fraccion, descripcion, cantidadComercial, UMF,valor_dolares, pais_origen, pais_destino, moneda, no_factura,uuid,checkbox_mar):
    fields = [''] * 46
    result = []  # Aquí almacenaremos los resultados de todas las iteraciones

    for parte, fra, desc, canti, val_dol in zip(noParte, fraccion, descripcion, cantidadComercial, valor_dolares):
        fields[0] = "551"  # 1 Tipo de Registro
        fields[1] = fra
        fields[2] = desc
        fields[3] = parte
        fields[4] = val_dol
        fields[5] = canti
        fields[6] = UMF
        #fields[7] = cant_tarifa
        fields[13] = pais_origen
        fields[14] = pais_destino
        fields[23] = moneda
        fields[37] = val_dol
        if(checkbox_mar == "on"):
            no_factura=uuid
        fields[43] = no_factura

        result.append('|'.join(fields) + '||\n')  # Agregar el resultado de la iteración con salto de línea

    return ''.join(result)  # Unir todos los resultados en una sola cadena y retornarla

def create_text_block505(folio, fecha, incoterm, moneda, total_usd, codigo_proveedor,uuid):
    formatted_fecha = fecha.replace('-', '')
    fields = [''] * 52
    fields[0] = "505"
    fields[1] = folio # ??????
    fields[2] = formatted_fecha
    fields[3] = incoterm #?????
    fields[4] = moneda
    fields[5] = total_usd
    fields[6] = total_usd
    #fields[6] = destinatario_nombre
    fields[7] = codigo_proveedor
    #fields[16] = ' '  # Observaciones a nivel factura
    #fields[17:24] = ['0'] * 7
    fields[31] = fecha # ?????
    fields[40] = uuid 

    return f"{'|'.join(fields)}||"

