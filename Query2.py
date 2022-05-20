import sqlite3

conn = sqlite3.connect('persons.db')

cursor = conn.cursor()

#2. Distribuição de pessoas por gênero e por país
cursor.execute('''
SELECT [gender], [location.country], COUNT(*) FROM persons GROUP BY [gender], [location.country];
''')

print('Distribuição de pessoas por gênero e por país.')

print('Gênero, País, Quantidade')

for linha in cursor.fetchall():
  print(linha)

conn.close()