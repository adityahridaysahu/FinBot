import mysql.connector
from flask_mysqldb import MySQL
import json, datetime, uuid
from mysql.connector import errorcode

class ConvoDAO:
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
                database=config['convodb']
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

    def update_status(self, unique_id, is_resolved, is_closed):
        query = f"UPDATE convo SET isResolved = {is_resolved}, isClosedbyUser = {is_closed} WHERE unique_ID = '{unique_id}'"
        with self.db.cursor() as cursor:
            cursor.execute(query)
            self.db.commit()

        query = f"SELECT unique_ID, isResolved, isClosedbyUser FROM convo WHERE unique_ID = '{unique_id}'"
        result = ""
        with self.db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()

        response = {
            "unique_ID": result[0],
            "isResolved": result[1],
            "isClosedByUser": result[2]
        }

        return response

    def mask_session(self, unique_id):
        current_datetime = datetime.datetime.now()

        query = "SELECT 1 FROM convo WHERE unique_ID = %s"
        values = (unique_id,)
        result = ""
        with self.db.cursor() as cursor:
            cursor.execute(query, values)
            result = cursor.fetchone()

        if result is None:
            unique_id = str(uuid.uuid4())[:11]
            insert_query = "INSERT INTO convo (unique_ID, time_stamp) VALUES (%s, %s)"
            insert_values = (unique_id, current_datetime)
            with self.db.cursor() as cursor:
                cursor.execute(insert_query, insert_values)
            self.db.commit()

            response = {
                'unique_id': unique_id,
                'time_stamp': current_datetime
            }
            return response
        else:
            query = "SELECT cum_sum_user, cum_sum_bot, global_hits FROM convo WHERE unique_ID = %s"
            values = (unique_id,)
            with self.db.cursor() as cursor:
                cursor.execute(query, values)
                result = cursor.fetchone()

            hits = "[]" if result[2] is None else result[2]

            return {
                "cum_sum_user": result[0],
                "cum_sum_bot": result[1],
                "global_hits": hits,
            }

    def update_summary(self, unique_id, new_cum_sum_user, new_cum_sum_bot, global_hits):
        current_datetime = datetime.datetime.now()

        query = "UPDATE convo SET time_stamp = %s, cum_sum_user = %s, cum_sum_bot = %s, global_hits = %s WHERE unique_ID = %s"
        values = (current_datetime, new_cum_sum_user, new_cum_sum_bot, global_hits, unique_id)
        with self.db.cursor() as cursor:
            cursor.execute(query, values)
        self.db.commit()

        result = ""
        query = f"SELECT global_hits FROM convo WHERE unique_ID = '{unique_id}'"
        with self.db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchone()
        decoded_hits = result[0]

        response = {
            "time_stamp": current_datetime,
            "global_hits": decoded_hits
        }

        return response
