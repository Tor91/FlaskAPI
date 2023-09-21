import mysql.connector

class UseDatabase:
    def __init__(self, config: dict)-> None:
        self.configuration = config
    def __enter__(self)->'cursor':
        self.conn = mysql.connector(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor
    def __exit__(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()