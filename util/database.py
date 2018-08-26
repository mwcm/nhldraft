from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.base import Base

def connect():
   engine = create_engine('postgresql://mwcmitchell@localhost:5432/nhl', echo=True)
   Session = sessionmaker(autocommit=False,
                              autoflush=False,
                              bind=engine)
   return engine, Session


def init_db():
   engine, Session = connect()
   from models.Player import Player
   from models.Category import Category
   Base.metadata.create_all(bind=engine)
   return engine, Session

if __name__ == '__main__':
   init_db()
