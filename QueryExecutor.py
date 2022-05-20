import sqlite3

con = sqlite3.connect('persons.db')
con.isolation_level = None
cur = con.cursor()

buffer = ""

print("Digite o código SQL aqui.")
print("Digite uma linha em branco para sair do console.")

while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""

con.close()