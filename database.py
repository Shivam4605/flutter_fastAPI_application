# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:shivam%40123@localhost/flutter_fastapi_db"

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:shivam%40123@localhost/info"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()