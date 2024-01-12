Driver =  'Oracle in EX'
myservicename = 'KRM_DBA'
myuserid = 'system'
mypassword= '031176kTA'
myhost = 'localhost'
Port = 1521

import pyodbc

cnxn = pyodbc.connect('DRIVER={Oracle in XE};Direct=True;Host=myhost;Service Name=myservicename;User ID=myuserid;Password=mypassword')
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM portalm ")
rows = cursor.fetchall()
for row in rows:
    print(row.CompanyName, row.City)