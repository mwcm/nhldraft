from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from util.base import Base

class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema':'nhl'}

    def __str__(self):
        return "{}".format(self.display_name)

    stat_id              = Column('stat_id', Integer, primary_key=True)
    name                 = Column('name', String)
    display_name         = Column('display_name', String)
    stat_modifier        = Column('stat_modifier', Integer)
    sort_order           = Column('sort_order', Integer)
    stat_position_types  = Column('stat_position_types', JSON)
    operator             = Column('operator', String)
    is_only_display_stat = Column('is_only_display_stat', Integer)
    decimal_points       = Column('decimal_points', Integer)
    is_composite_stat    = Column('is_composite_stat', Integer)
