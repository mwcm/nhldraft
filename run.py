from util import database
from models.Player import Player
from models.Category import Category
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def init():
    engine, Session = database.init_db()
    test(Session)


def main():
    engine, Session = database.connect()
    test(Session)
    raise SystemExit


def test(Session):
    s = Session()
    q = s.query(Player).all()
    q = s.query(Category).all()
    print(q)

if __name__ == '__main__':
    main()
