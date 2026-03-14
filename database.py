
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:shivam%40123@localhost/info"

DATABASE_URL = os.getenv("mysql://root:jAQIrZGUbNUyYYBAZTYJMPoBcpeCyzHe@centerbeam.proxy.rlwy.net:49081/railway")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

