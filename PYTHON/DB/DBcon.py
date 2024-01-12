import pyodbc

class SQLConnector:
    def __init__(self,  database, trusted_connection=True):
        self.server = 'DESKTOP-TRCMICB\SQLEXPRESS'
        self.database = database
        self.trusted_connection = trusted_connection
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            conn_str = f"Driver={{SQL Server Native Client 11.0}};" \
                       f"Server={self.server};" \
                       f"Database={self.database};"
            if self.trusted_connection:
                conn_str += "Trusted_Connection=yes;"
            else:
                # Dodaj tutaj inne dane uwierzytelniające, jeśli są używane, np. UID i PWD
                pass

            self.connection = pyodbc.connect(conn_str)
            self.cursor = self.connection.cursor()
            print("Connected to the database.")

        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from the database.")


