# Tworzenie instancji klasy OracleConnector
import cx_Oracle

from PYTHON.DB.DBcon import OracleConnector

oracle_connector = OracleConnector(username='system',
                                   password='031176kTA!',
                                   host='DESKTOP-TRCMICB',
                                   port='1521',
                                   service_name='XE')

# Należy podmienić 'your_username', 'your_password', 'your_host', 'your_port', 'your_service_name' na rzeczywiste dane
# które pozwalają na połączenie się z Twoją bazą danych Oracle.

# Połączenie z bazą danych
oracle_connector.connect()

# Zapytanie SQL do pobrania danych
query = "SELECT * FROM hr.jobs"

try:
    # Wykonanie zapytania SQL
    with oracle_connector.connection.cursor() as cursor:
        cursor.execute(query)

        # Pobranie wyników zapytania
        rows = cursor.fetchall()

        # Wyświetlenie wyników
        for row in rows:
            print(row)

except cx_Oracle.Error as e:
    print(f"Error executing SQL query: {e}")

# Rozłączenie z bazą danych
oracle_connector.disconnect()
