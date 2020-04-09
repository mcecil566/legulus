import configparser
import os
import psycopg2
import logging
import sys

log = logging.getLogger(__name__)

class Database:
    
    def __init__(self, database):
        self.config = configparser.ConfigParser()
        self.config.read(os.environ['D_BOT_CFG'] + 'main.ini')

        self.db_host = self.config['postgre_sql']['hostname']
        self.db_user = self.config['postgre_sql']['username']
        self.db_pw = self.config['postgre_sql']['password']
        self.db_port = self.config['postgre_sql']['port']
        self.db_database = database
    
    def connect(self):
        # connect to the postgres database

        try:
            self.db_connection = psycopg2.connect(
                host=self.db_host,
                user=self.db_user,
                password=self.db_pw,
                database=self.db_database,
                port=self.db_port
            )
            return self.db_connection
            log.info('Successfully connected to PostgreSQL database.')

        except Exception as e:
            log.error('Could not connect to PostgreSQL database.')
            log.error(e)

    def update_lastfm_account(self, discord_id, lastfm_account):
        # check to see if we already have a discord account id and
        # update the lastfm account if we do

        try:
            cursor = self.db_connection.cursor()

            cursor.execute('SELECT * FROM discord_user')
            result = cursor.fetchall()
            
            for row in result:
                if discord_id in row[3]:
                    update_user_query = "UPDATE discord_user SET lastfm_account = '{lastfm_account}' WHERE user_id = '{user_id}'".format(
                        lastfm_account=lastfm_account,
                        user_id=row[0]
                    )

                    cursor.execute(update_user_query)
                    self.db_connection.commit()
                    log.info('Updated row: {}'.format(row[0]))
                    return discord_id
                else:
                    log.info('No row found')

            cursor.close()
        
        except Exception as e:
            log.error(e)
        
    def add_account(self, discord_account, discord_id, lastfm_account):
        # add row to db with discord account, discord account id and
        # lastfm account if it doesn't exist

        try:
            cursor = self.db_connection.cursor()

            insert_user_query = "INSERT INTO discord_user (discord_account, discord_id, lastfm_account) VALUES ('{discord_account}', '{discord_id}', '{lastfm_account}')".format(
                discord_account=discord_account,
                discord_id=discord_id,
                lastfm_account=lastfm_account
            )

            cursor.execute(insert_user_query)
            self.db_connection.commit()
            log.info('Added row: {}'.format(discord_id))

            cursor.close()

        except Exception as e:
            log.error(e)
    
    def delete_row(self, user_id):
        # delete a row in the discord_user table

        try:
            cursor = self.db_connection.cursor()

            delete_row_query = "DELETE FROM discord_user WHERE user_id = '{user_id}'".format(
                user_id=user_id
            )

            cursor.execute(delete_row_query)
            self.db_connection.commit()
            log.info('Deleted row: {}'.format(user_id))

            cursor.close()
        
        except Exception as e:
            log.error(e)

# db = Database('d_bot')

# conn = db.connect()
# update = db.update_lastfm_account('test_account_1', 'modified_account')