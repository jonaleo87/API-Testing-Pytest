import os
import pyodbc

def get_person_from_db(person_id):
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};SERVER={os.getenv('DB_SERVER', 'localhost')};"
            f"DATABASE={os.getenv('DB_NAME', 'Test')};UID={os.getenv('DB_USER', 'usuario')};PWD={os.getenv('DB_PASS', 'contraseña')}"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT * FROM Worldsys WHERE personId = ?", person_id)
        row = cursor.fetchone()
        conn.close()
        return row
    except Exception as e:
        print(f"[ERROR] Error al consultar la base de datos: {e}")
        return None