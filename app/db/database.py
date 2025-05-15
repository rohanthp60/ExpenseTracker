from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging

from app.core.config import settings

logging.basicConfig(level=logging.DEBUG)

engine = create_engine(str(settings.DATABASE_URL))
localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

logging.info("Database connection established")