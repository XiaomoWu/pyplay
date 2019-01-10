import wrds
db = wrds.Connection()

db.describe_table()
db.get_table()
db.engine()
db.insp()
db.raw_sql()
db.get_row_count()
db.schema_perm()


db.list_libraries()
db.list_tables('taqmsec')

db.describe_table(library="taqmsec", table="ctm_20030910")

data = db.get_table(library='taqmsec', table='ctm_20140910', columns=['date', 'time_m'], obs=10)
data

del data
sql = """
    select *
    from taqmsec.ctm_20150414
    limit 100;
"""
data = db.raw_sql(sql.replace('\n', ' '))
data