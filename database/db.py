from sqlalchemy.orm import sessionmaker,create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///../db/addresses.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
