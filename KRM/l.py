import sqlalchemy as sa

x=sa.sql.text('select * from krm_dba.portalm')
print(x)