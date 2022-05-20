import sqlite3

conn = sqlite3.connect('persons.db')

cursor = conn.cursor()

#3. Quantas pessoas dessa distribuição possuí + de 50
print('Quantas pessoas dessa distribuição possuí + de 50.')

cursor.execute('SELECT COUNT(*) FROM persons WHERE [dob.age] > 50;')
print(cursor.fetchall())

for linha in cursor.execute('SELECT COUNT(*) FROM persons WHERE [dob.age] > 50;'):
  print(linha)

conn.close()