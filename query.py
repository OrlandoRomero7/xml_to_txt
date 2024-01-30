import pyodbc

def obtenerClientes():
    # Datos de conexión
    server = '192.168.4.102'
    database = 'Darwin_DB'
    username = 'sa'
    password = 'Darwin2020'
    driver = '{SQL Server}'  # Asegúrate de que esta versión del driver esté instalada en tu máquina.

    # Crear conexión
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(connection_string)

    # Realizar alguna consulta (ejemplo)
    cursor = conn.cursor()
    cursor.execute("select Numero, Nombre from VT_Clientes")
    rows = cursor.fetchall()


    cursor.close()
    conn.close()
    return rows


def obtenerProveedores():
    # Datos de conexión
    server = '192.168.4.102'
    database = 'Darwin_DB'
    username = 'sa'
    password = 'Darwin2020'
    driver = '{SQL Server}'  # Asegúrate de que esta versión del driver esté instalada en tu máquina.

    # Crear conexión
    connection_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    conn = pyodbc.connect(connection_string)

    # Realizar alguna consulta (ejemplo)
    cursor = conn.cursor()
    cursor.execute("select Clave, Nombre from VT_Proveedores")
    rows = cursor.fetchall()


    cursor.close()
    conn.close()
    return rows
