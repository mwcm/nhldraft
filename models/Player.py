from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from util.base import Base

class Player(Base):
    __tablename__ = 'players'
    __table_args__ = {'schema':'nhl'}

    def __str__(self):
        return "{} {} {}".format(self.id, self.fname, self.lname)

    id              = Column('id', Integer, primary_key=True)
    player_key      = Column('player_key', String)
    team_key        = Column('team_key', String)
    team_name       = Column('team_name', String)
    team_abbr       = Column('team_abbr', String)
    uniform_num     = Column('uniform_num', String)
    average_pick    = Column('average_pick', String)
    average_round   = Column('average_round', String)
    percent_drafted = Column('percent_drafted', String)
    o_rank          = Column('o_rank', Integer)
    psr_rank        = Column('psr_rank', Integer)
    s_rank_1        = Column('s_rank_1', Integer)
    s_rank_2        = Column('s_rank_2', Integer)
    s_rank_3        = Column('s_rank_3', Integer)
    pos_type        = Column('pos_type', String)
    fname           = Column('fname', String)
    lname           = Column('lname', String)
    inj             = Column('inj', String)
    inj_full        = Column('inj_full', String)
    img             = Column('img', String)
    pos             = Column('pos', JSON)
    display_pos     = Column('display_pos', String)
    primary_pos     = Column('primary_pos', String)
    season_stats    = Column('season_stats', JSON)
    projected_stats = Column('projected_stats', JSON)
