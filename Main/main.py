import sys
import os
from sqlalchemy.orm import Session
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Database.connection import (
    SessionLocal, 
    TaskDB, 
    TaskStatus, 
    create_database_if_not_exists,
    default_engine
)

from InterfazGrafica.interfazGrafica import App

def connection():
    try:
        session = SessionLocal()
        print("Conexión Exitosa")
    except Exception as e:
        print(f"Error al probar la conexión: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    
    # Crear la base de datos si no existe
    db_name = "To_do_list_db"
    create_database_if_not_exists(db_name)
    
    # Probar la conexión
    connection()

    # Iniciar la interfaz gráfica
    app = App()
    app.mainloop()