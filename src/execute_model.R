# 📂 src/execute_model.R - Script en R para procesamiento de datos

df <- data.frame(X1 = rnorm(10), X2 = rnorm(10), X3 = rnorm(10))
con <- DBI::dbConnect(odbc::odbc(), Driver = "SQL Server", Server = "tu_servidor", Database = "tu_db", UID = "usuario", PWD = "contraseña")
DBI::dbWriteTable(con, "ResultadosModelo", df, overwrite = TRUE)
print("Modelo en R ejecutado y datos insertados en SQL Server.")