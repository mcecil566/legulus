import configparser
import os
import psycopg2

class Database:
    
    def __init__(self, database):
        self.config = configparser.ConfigParser()
        self.config.read(os.environ['D_BOT_CFG'] + 'main.ini')

        self.db_host = self.config['postgre_sql']['hostname']
        self.db_user = self.config['postgre_sql']['username']
        self.db_pw = self.config['postgre_sql']['password']
        self.db_port = self.config['postgre_sql']['port']
        self.database = database
    
    def connect(self):
        self.db_connection = psycopg2.connect(
            database=self.database,
            user=self.db_user,
            password=self.db_pw,
            host=self.db_host,
            port=self.db_port
        )
        return self.db_connection

db = Database('d_bot_db')
print(db.db_host)
conn = db.connect()