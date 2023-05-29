import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base # Manipualcion de las tablas

sqlite_file_name = "../data/database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

# Conexion a la base de datos
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

# Conexion a la base de datos
engine = create_engine(
    url=database_url,
    echo=True, # para ver los logs de creacion de la base de datos
    )

# Sesion
Session = sessionmaker(bind=engine)

# Instancia declarativa
Base = declarative_base()
