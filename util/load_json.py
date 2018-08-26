import sys
import os

from util import database
from models.Player import Player
from models.Category import Category

import json
from glom import glom
from pprint import pprint


def import_json_file(name):
   with open('{}/json/{}.json'.format('/'.join(os.path.realpath(__file__).split('/')[:-2]), name)) as f:
      data = json.load(f)
      f.close()
   return data

def import_json():
   category_data = import_json_file('categories')
   players = import_json_file('players')
   data = {'category_data':category_data,
           'player_data':players}
   return data

def load_data_into_models(data):
   categories = []
   for item in data['category_data']:
      c = Category(**item)
      categories.append(c)

   players = []
   for player in data['player_data']:
      p = Player(**player)
      players.append(p)

   populated_models = {'players': players,
                       'categories': categories}
   return populated_models


def check_tables_empty(session):
   players = session.query(Player).first()
   categories = session.query(Category).first()
   if (players == None) and (categories == None):
      return True
   else:
      return False



def load_data_into_tables(session, populated_models):
   session.add_all(populated_models['categories'])
   session.add_all(populated_models['players'])
   session.commit()
   return


def main():
   engine, Session = database.connect()
   s = Session()
   tables_empty = check_tables_empty(s)

   if tables_empty:
      data = import_json()
      populated_models = load_data_into_models(data)
      load_data_into_tables(s, populated_models)
   return


if __name__ == '__main__':
   main()
