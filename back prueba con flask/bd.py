import pyodbc
direccion_servidor = 'DESKTOP-RT7R14U\SQLEXPRESS'
nombre_bd = 'PP'
nombre_usuario = 'Yanet'
password = 'Yanet05'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("conexión exitosa")
    
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
