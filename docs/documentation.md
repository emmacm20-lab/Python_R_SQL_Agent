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
