import mysql.connector
import json
from mysql.connector import errorcode

class BondDAO:
    def __init__(self):
        self.db = self.connect_to_database()

    def connect_to_database(self):
        with open('config.json') as config_file:
            config = json.load(config_file)
        
        try:
            db = mysql.connector.connect(
                host=config['host'],
                user=config['username'],
                password=config['password'],
                database=config['bondsdb']
            )

            return db

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return None

    def execute_query(self, query):
        with self.db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            rows = [dict(zip(columns, row)) for row in result]
            return rows