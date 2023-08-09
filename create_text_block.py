from tqdm import tqdm

def create_text_block501(operacion, clave,  no_pedimento,no_factura,moneda):
    fields = [''] * 24

    fields[0] = "501"       #1 Tipo de Registro
    fields[1] = operacion   #2 Tipo de Operacion
    fields[2] = clave       #3 Clave de Pedimento
    fields[3] = no_pedimento       #4 Numero de Pedimento
    fields[16] = no_factura  #17 Referencia
    fields[19] = moneda      #20 Pais Moneda ?

    return f"{'|'.join(fields)}||"

def create_text_block551(noParte, fraccion, descripcion, cantidadComercial, valor_dolares, pais_origen, pais_destino, moneda, no_factura):
    fields = [''] * 46
    result = []  # Aquí almacenaremos los resultados de todas las iteraciones

    for parte, fra, desc, canti, val_dol in tqdm(zip(noParte, fraccion, descripcion, cantidadComercial, valor_dolares), desc="Processing 551", total=len(noParte)):
        fields[0] = "551"  # 1 Tipo de Registro
        fields[1] = fra
        fields[2] = desc
        fields[3] = parte
        fields[5] = canti
        #fields[6] = um
        fields[13] = pais_origen
        fields[14] = pais_destino
        fields[23] = moneda
        fields[37] = val_dol
        fields[43] = no_factura

        result.append('|'.join(fields) + '||\n')  # Agregar el resultado de la iteración con salto de línea

    return ''.join(result)  # Unir todos los resultados en una sola cadena y retornarla

def create_text_block505(folio, fecha, incoterm, moneda, total_usd, uuid):
    formatted_fecha = fecha.replace('-', '')
    fields = [''] * 44
    fields[0] = folio
    fields[1] = formatted_fecha
    fields[2] = incoterm
    fields[3] = moneda
    fields[4] = total_usd
    fields[5] = total_usd
    #fields[6] = destinatario_nombre
    fields[17] = ' '  # Observaciones a nivel factura
    fields[18:25] = ['0'] * 7
    fields[30] = fecha
    fields[39] = uuid

    return f"505|{'|'.join(fields)}||"

