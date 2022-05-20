import sqlite3

conn = sqlite3.connect('persons.db')

cursor = conn.cursor()

#1. Total de pessoas com o mesmo nome por país
cursor.execute('''
SELECT [name.first], [location.country], COUNT(*) FROM persons GROUP BY [name.first], [location.country];
''')

print('Total de pessoas com o mesmo nome por país.')

print('Nome, País, Quantidade')

for linha in cursor.fetchall():
  print(linha)

conn.close()