import sqlite3

class Database:
    def __init__(self, url):
        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS ew (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL
            );
            """
            cursor.execute(sql)

            sql_insert = """
            INSERT INTO ew (task) VALUES (?);
            """
            cursor.execute(sql_insert, ('Complete Flask web dev',))
            db.commit()

    def get_ews(self):
        """
        TO IMPLEMENT
        """
        pass

    def create_ew(self, task):
        """
        TO IMPLEMENT
        """
        pass



    # EXTRA CREDIT
    def get_ew(self, id):
        """
        TO IMPLEMENT
        """
        pass