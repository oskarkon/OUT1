import pandas as pd
import pyodbc
import sqlite3

connString = 'Trusted_Connection=no;DRIVER={Oracle in XE};SERVER=localhost;PORT=1521;DATABASE=krm_dba;UID=system;PWD=031176kTA;'

conn = pyodbc.connect(connString)

cursor = conn.cursor()
cursor.execute("""SELECT *  FROM portalm_org""")
cursor.fetchone()
cursor.fetchall()


query = """
            INSERT INTO portalm_org (currency2)  VALUES ('ooo')
        """

cursor.execute(query)



#
# cursor = cnn.cursor()
# cursor.execute("SELECT * FROM portalm ")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# df=pd.read_sql('select * from portalm_org',cnn)
# df