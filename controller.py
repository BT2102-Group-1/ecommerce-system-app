from numpy.lib.function_base import append
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import pandas as pd
import numpy as np

class Connection:
    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:password@localhost/oshes')
        self.connection = self.engine.connect()

if __name__ == '__main__':
    db = Connection()
    print(db.engine)
    # print(pd.read_sql('Customer', db.connection))
    # print(pd.read_sql_query('SELECT * FROM Customer WHERE gender = "F"', db.connection))

    insert = pd.DataFrame(np.array([['Lyn Tan', 'F', '123 Tiong Bahru Rd', 'hihi@jeno.com', 'cpassword', '92969405']]), columns=['name', 'gender', 'address', 'email', 'password', 'phoneNo']) 
    insert.to_sql('Customer', db.connection, if_exists='append', index_label='customerId') # write “customers” to database
    print(pd.read_sql('Customer', db.connection))
