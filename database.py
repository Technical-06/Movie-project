from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

password="root"
DATABASE_URL = "mysql+mysqlconnector://root:"+password+"@localhost:3306/movie_rec"

engine = create_engine(DATABASE_URL)
con = engine.connect()

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()