# 📂 src/execute_model.py - Script en Python para ejecución de modelo matemático

import pandas as pd
import numpy as np
import pyodbc

def run_model():
    data = np.random.rand(10, 3)  # Generación de datos aleatorios
    df = pd.DataFrame(data, columns=['X1', 'X2', 'X3'])
    
    conn = pyodbc.connect("DRIVER={SQL Server};SERVER=tu_servidor;DATABASE=tu_db;UID=usuario;PWD=contraseña")
    df.to_sql("ResultadosModelo", conn, if_exists="replace", index=False)
    print("Modelo ejecutado y datos insertados en SQL Server.")

if __name__ == "__main__":
    run_model()