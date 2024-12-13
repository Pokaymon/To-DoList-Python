import os
from sqlalchemy import create_engine, Column, String, Enum, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker
import enum

# Leer credenciales desde variables de entorno
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
db_name = os.getenv("MYSQL_DB")

# Validar que las variables de entorno estén configuradas
if not all([user, password, host, db_name]):
    raise ValueError("Faltan una o más variables de entorno necesarias para la conexión a la base de datos.")

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
default_engine_url = f"mysql+pymysql://{user}:{password}@{host}"

default_engine = create_engine(default_engine_url)

def create_database_if_not_exists(db_name):
    try:
        with default_engine.connect() as connection:
            connection.execute(text(f"CREATE DATABASE {db_name}"))
            print(f"Base de datos '{db_name}' creada con éxito.")
    except ProgrammingError as e:
        if "database exists" in str(e).lower():
            print(f"La base de datos '{db_name}' ya existe.")
        else:
            raise

create_database_if_not_exists(db_name)

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TaskStatus(enum.Enum):
    Pendiente = "Pendiente"
    Completada = "Completada"

class TaskDB(Base):
    __tablename__ = "tasks"
    titulo = Column(String(10), primary_key=True)
    descripcion = Column(String(50), nullable=True)
    completada = Column(Enum(TaskStatus), default=TaskStatus.Pendiente)

Base.metadata.create_all(bind=engine)