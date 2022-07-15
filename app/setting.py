from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Engine の作成
Engine = create_engine("mysql+pymysql://dbuser:password@db/mydb", encoding="utf-8", echo=False)
Base = declarative_base()
