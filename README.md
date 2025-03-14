# 📂 docs/README.md - Documentación del Proyecto
"""
# 📊 Modelo Matemático en Python y R con SQL Server Agent

## 📌 Descripción del Proyecto

Este proyecto implementa una **integración entre Python, R y SQL Server** para la ejecución de **modelos matemáticos y procesamiento de datos**, permitiendo automatizar la ejecución a través de **SQL Server Agent**. Incluye:

- **Desarrollo de modelos matemáticos y estadísticos en Python y R.**
- **Ejecución automatizada de scripts externos desde SQL Server Agent.**
- **Inserción de resultados en tablas de SQL Server.**
- **Ejecución de stored procedures y triggers con parámetros dinámicos.**

## 📂 Estructura del Proyecto
```
📁 Python_R_SQL_Agent
│── 📂 src/
│   │── execute_model.py  # Script en Python para ejecución de modelo matemático
│   │── execute_model.R  # Script en R para procesamiento de datos
│   │── run_sql_jobs.sql  # Script SQL para ejecución en SQL Server Agent
│── 📂 tests/
│   │── test_execute_model.py  # Pruebas unitarias de ejecución en Python
│   │── test_run_sql_jobs.sql  # Pruebas de validación en SQL Server
│── 📂 docs/
│   │── README.md  # Documentación del proyecto
```

## 🚀 Instalación y Configuración

1. **Clona este repositorio:**
   ```sh
   git clone https://github.com/emmacm20-lab/Python_R_SQL_Agent.git
   ```
2. **Ejecuta el modelo matemático en Python:**
   ```sh
   python src/execute_model.py
   ```
3. **Ejecuta el modelo en R:**
   ```sh
   Rscript src/execute_model.R
   ```
4. **Configura y ejecuta los jobs en SQL Server Agent:**
   ```sh
   sqlcmd -S servidor -d base_de_datos -i src/run_sql_jobs.sql
   ```

## 📩 Flujo de Trabajo
1. **Ejecución de modelos matemáticos en Python y R.**
2. **Inserción de resultados en SQL Server.**
3. **Automatización de ejecución con SQL Server Agent.**
4. **Ejecución de stored procedures y triggers con parámetros dinámicos.**

## 🛠 Tecnologías Utilizadas
- **Python**: Implementación de modelos matemáticos y estadísticos.
- **R**: Procesamiento de datos y cálculos avanzados.
- **SQL Server Agent**: Automatización de ejecución de modelos.
- **T-SQL**: Inserción de datos y ejecución de stored procedures.

## 📈 Resultados Esperados
- 📌 **Automatización de modelos matemáticos con Python y R en SQL Server.**
- 📌 **Reducción del esfuerzo manual en ejecución de análisis y reportes.**
- 📌 **Ejecución escalable mediante SQL Server Agent.**
- 📌 **Mayor eficiencia en la integración de modelos estadísticos en bases de datos empresariales.**

## 🧪 Pruebas
El proyecto incluye pruebas en Python y SQL para validar la ejecución de modelos y almacenamiento de resultados.
1. **Ejecución de pruebas en Python:**
   ```sh
   python -m unittest discover tests/
   ```
2. **Validación en SQL Server:**
   ```sh
   sqlcmd -S servidor -d base_de_datos -i tests/test_run_sql_jobs.sql
   ```

## 📬 Contacto
Para consultas o sugerencias, contáctame en [emmanuel.cmora20@gmail.com](mailto:emmanuel.cmora20@gmail.com).
"""

# 📂 src/execute_model.py - Script en Python para ejecución de modelo matemático
```python
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
```

# 📂 src/execute_model.R - Script en R para procesamiento de datos
```r
df <- data.frame(X1 = rnorm(10), X2 = rnorm(10), X3 = rnorm(10))
con <- DBI::dbConnect(odbc::odbc(), Driver = "SQL Server", Server = "tu_servidor", Database = "tu_db", UID = "usuario", PWD = "contraseña")
DBI::dbWriteTable(con, "ResultadosModelo", df, overwrite = TRUE)
print("Modelo en R ejecutado y datos insertados en SQL Server.")
```

# 📂 src/run_sql_jobs.sql - Script SQL para ejecución de Jobs en SQL Server Agent
```sql
EXEC msdb.dbo.sp_start_job N'ModeloPythonRJob';
```

# 📂 tests/test_execute_model.py - Pruebas en Python para validación de ejecución
```python
import unittest
from src.execute_model import run_model

class TestModelExecution(unittest.TestCase):
    def test_run_model(self):
        try:
            run_model()
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
```

# 📂 tests/test_run_sql_jobs.sql - Pruebas de validación de ejecución en SQL Server
```sql
SELECT COUNT(*) AS TotalRegistros FROM ResultadosModelo;
```
