from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.base import Base

from models.Player import Player
from models.Category import Category

def connect():
   engine = create_engine('postgresql://mwcmitchell@localhost:5432/nhl', echo=True)
   Session = sessionmaker(autocommit=False,
                              autoflush=False,
                              bind=engine)
   return engine, Session


def init_db():
   engine, Session = connect()
   # TODO:
   # create database
   # create schema
   Base.metadata.create_all(bind=engine)
   return engine, Session

def cleanup(SessionMaker, engine):
   print('\n\n CLEANUP \n\n')
   SessionMaker.close_all()
   # session.query(Player).delete()
   # session.query(Category).delete()
   # session.commit()
   # session.close()
   Base.metadata.drop_all(bind=engine)
   print('\n\n CLEANUP FINISHED\n\n')
   return

if __name__ == '__main__':
   init_db()
