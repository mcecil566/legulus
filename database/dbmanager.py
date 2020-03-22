import configparser
import os

class Database:
    
    def __init__(self, database):
        self.config = configparser.ConfigParser()
        self.config.read(os.environ['D_BOT_CFG'] + 'main.ini')

        self.db_host = self.config['postgre_sql']['hostname']
        self.db_user = self.config['postgre_sql']['username']
        self.db_pw = self.config['postgre_sql']['password']
        self.database = database

db = Database('d_bot')

print(db.db_host)