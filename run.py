from util import database, load_json
from models.Player import Player
from models.Category import Category
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def setup():
    engine, SessionMaker = database.init_db()
    s = SessionMaker()
    load_json.main() # load json data in tables
    s.commit()
    s.close()
    test(s)
    raise SystemExit

def test(session):
    print('\n\n TEST \n\n')
    q1 = session.query(Player).first()
    q2 = session.query(Category).first()
    print(q1.__dict__)
    print(q2.__dict__)
    print('\n\n TEST FINISHED \n\n')



if __name__ == '__main__':
    setup()
