import pandas as pd
import sqlite3

def agregar_datos_desde_csv():
    
    sqlite_file_name = "../data/database.sqlite"
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(sqlite_file_name)

    # Leer el archivo JSON utilizando pandas
    df = pd.read_csv('../data/movie_data.csv', index_col=False)

    # Realizar la inserción masiva utilizando to_sql()
    df.to_sql('movies', conn, if_exists='append', index=False)

    # Cerrar la conexión
    conn.close()

# Llamar a la función para agregar los datos desde el archivo JSON
agregar_datos_desde_csv()
