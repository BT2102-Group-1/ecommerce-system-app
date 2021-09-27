from sqlalchemy import create_engine
import pandas as pd

db = create_engine('mysql+mysqlconnector://root:password@localhost/oshes')

print(db)

print(pd.read_sql('Customer', db))

