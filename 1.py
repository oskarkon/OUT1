from sqlalchemy.engine import URL
connection_string = "DRIVER={Oracle in XE};SERVER=lokalhost;DATABASE=KRM_DBA;UID=system;PWD=031176kTA"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

from sqlalchemy import create_engine
engine = create_engine(connection_url)

import pandas as pd
import sqlalchemy as sa


with engine.begin() as conn:
    df = pd.read_sql_query(sa.text("select txn_id from portalm"), conn)

df