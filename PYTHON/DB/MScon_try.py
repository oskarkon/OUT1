from PYTHON.DB.DBcon import MsConnector

# Stworzenie instancji klasy
sql_connector = MsConnector( database="SQL")

# Połączenie z bazą danych
sql_connector.connect()

# Przykład zapytania SQL
try:
    sql_connector.cursor.execute("select * from SQL.dbo.dept")
    rows = sql_connector.cursor.fetchall()

    for row in rows:
        print(row)

except Exception as e:
    print(f"Error executing SQL query: {e}")

finally:
    # Rozłączenie z bazą danych
    sql_connector.disconnect()