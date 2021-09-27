from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd

class Connection:
    def __init__(self):
        this.engine = create_engine('mysql+mysqlconnector://root:password@localhost/oshes')
        this.connection = db.connect()

    def init_table(self):
        init_table_file = open('sql/Database.sql')
        init_table_query = text(init_table_file.read())

        this.connection.execute(init_table_query)

if __name__ == 'main':
    db = Connection()
    print(db.engine)
    print(pd.read_sql('Customer', db.connection))
    print(pd.read_sql_query('SELECT * FROM Customer WHERE gender = "F"', db))

