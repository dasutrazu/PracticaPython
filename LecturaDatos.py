import sqlite3
import pandas as pd
from pathlib import Path

con = sqlite3.connect('./Datos/Ventas.db')

data = pd.read_sql_query(
    """
    SELECT Precio, Fecha
    FROM PRECIO
    WHERE Producto_id = 5 AND Fecha > '2015-01-1' and Fecha < '2018-01-1'
    """, 
    con, 
    parse_dates='Fecha', 
    dtype={'Precio':'float64'})
#data.loc['Fecha'] = pd.to_datetime(data['Fecha'])
data.head(4)

cursor= con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tablas = cursor.fetchall()
print("Tablas en la base de datos:")
for t in tablas:
    print(t[0])

#print(data)
