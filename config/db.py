from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+pymysql://root:123456@localhost/storedb"

engine = create_engine(DATABASE_URL)
meta = MetaData()

conn = engine.connect()