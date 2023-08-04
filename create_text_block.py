def create_text_block501(operacion, clave, referencia, moneda):
    fields = [''] * 5

    fields[0] = "501"       #1 Tipo de Registro
    fields[1] = operacion   #2 Tipo de Operacion
    fields[2] = clave       #3 Clave de Pedimento
    #num_pedimento ?        #4 Numero de Pedimento
    fields[3] = referencia  #17 Referencia
    fields[4] = moneda      #20 Pais Moneda ?

    return f"{'|'.join(fields)}||"

def create_text_block551(fraccion, descripcion, unidad_medida, valor_dolares):
    fields = [''] * 46
    result = []  # Aquí almacenaremos los resultados de todas las iteraciones

    for fra, desc, um, val_dol in zip(fraccion, descripcion, unidad_medida, valor_dolares):
        fields[0] = "551"  # 1 Tipo de Registro
        fields[1] = fra
        fields[2] = desc
        fields[6] = um
        fields[37] = val_dol

        result.append('|'.join(fields) + '||\n')  # Agregar el resultado de la iteración con salto de línea

    return ''.join(result)  # Unir todos los resultados en una sola cadena y retornarla



def create_text_block505(folio, fecha, incoterm, moneda, total_usd, destinatario_nombre, uuid):
    formatted_fecha = fecha.replace('-', '')
    fields = [''] * 44
    fields[0] = folio
    fields[1] = formatted_fecha
    fields[2] = incoterm
    fields[3] = moneda
    fields[4] = total_usd
    fields[5] = total_usd
    fields[6] = destinatario_nombre
    fields[17] = ' '  # Observaciones a nivel factura
    fields[18:25] = ['0'] * 7
    fields[30] = fecha
    fields[39] = uuid

    return f"505|{'|'.join(fields)}||"

