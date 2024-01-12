import cx_Oracle
import pandas as pd
import pandas.io.sql as psql

con = cx_Oracle.connect('system/031176kTA@localhost')

cur = con.cursor()
cur.execute("update  portalm set amort_type=999 where amort_type=122" )
con.commit()
# res = cur.fetchall()
# for row in res:
#     print(row)


df = pd.read_sql_query('select * from portam',con=con)