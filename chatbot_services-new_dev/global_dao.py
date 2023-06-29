import mysql.connector
import json
from mysql.connector import errorcode

class GlobalDAO:
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
                database=config['globaldb']
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

    def extract_responses(self, keywords):
        keywords_list = keywords.split(',')
        keyword_hits = []

        rows = []
        query = "SELECT id, keywords, expected_response FROM global"
        with self.db.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()

        for row in rows:
            response_keywords = row[1].lower().split(",")
            hits = sum(keyword.lower() in response_keywords for keyword in keywords_list)
            keyword_hits.append({
                "id": row[0],
                "keyword_hits": hits,
                "response": row[2]
            })

        filtered_data = [d for d in keyword_hits if d['keyword_hits'] >= 1]
        sorted_hits = sorted(filtered_data, key=lambda x: x["keyword_hits"], reverse=True)

        return sorted_hits

    def update_positive_feedback(self, ids, threshold):
        ids = ids.split(",")
        if ids[0] == '':
            return {
                "updated" : False
            }
        for idp in ids:
            idx = int(idp)
            query = f'SELECT probability FROM global WHERE id = {idx}'
            
            result = ""
            with self.db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
            
            p = result[0]
            if p < 1:
                query = f'UPDATE global SET probability = probability + {threshold} where id = {idx}'
                with self.db.cursor() as cursor:
                    cursor.execute(query)
                    self.db.commit()  # Commit the change
        
        rows = []
        result = ""
        for idx in ids:
            query = f'SELECT probability FROM global where id = {idx}'
            
            with self.db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
            
            rows.append({
                "id" : idx,
                "probability" : result[0]
            })

        return {
            "updated" : rows
        }

    def update_negative_feedback(self, ids, threshold):
        ids = ids.split(",")
        if ids[0] == '':
            return {
                "updated" : False
            }
        
        result = ""
        
        for idp in ids:
            idx = int(idp)
            query = f'SELECT probability FROM global WHERE id = {idx}'
            
            with self.db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
            
            p = result[0]
            if p > 0:
                query = f'UPDATE global SET probability = probability - {threshold} where id = {idx}'
                with self.db.cursor() as cursor:
                    cursor.execute(query)
                    self.db.commit()  # Commit the change
        
        rows = []
        for idx in ids:
            query = f'SELECT probability FROM global where id = {idx}'
            with self.db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
            rows.append({
                "id" : idx,
                "probability" : result[0]
            })

        return  {
            "updated" : rows
        }
