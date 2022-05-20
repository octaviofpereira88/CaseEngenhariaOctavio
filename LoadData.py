import pandas as pd
import sqlite3

person = pd.read_csv('https://randomuser.me/api/?format=csv&results=1000')

conn = sqlite3.connect('persons.db')

cursor = conn.cursor()

cursor.execute('''
DROP TABLE IF EXISTS persons;
''')

person.to_sql('persons', con=conn)