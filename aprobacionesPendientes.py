import pandas as pd
import pyodbc

# Cargar el archivo Excel
df_excel = pd.read_excel("aprobacionesPendientes.xlsx", engine="openpyxl")
refaccion_ids = df_excel["refaccion_idx1"].unique().tolist()

# Configura tu conexión a SQL Server
server = 'TU_SERVIDOR'
database = 'TU_BASE_DE_DATOS'
username = 'TU_USUARIO'
password = 'TU_CONTRASEÑA'
,
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};DATABASE={database};UID={username};PWD={password}'
)

# Conectar a la base de datos
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Crear la consulta SQL para actualizar los registros
query = """
UPDATE refaccion
SET aprobacion_mtto = 1
WHERE refaccion_idx1 = ?
AND aprobacion_mtto = 0
"""

# Ejecutar la actualización para cada ID
for idx in refaccion_ids:
    cursor.execute(query, idx)

# Confirmar los cambios
conn.commit()
cursor.close()
conn.close()

print("✅ Actualización completada.")
