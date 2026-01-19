from database.db_pacientes import DatabasePacientes
import sqlite3
import os

db = DatabasePacientes()

# db.criar_banco()


caminho = os.path.join(os.getenv("APPDATA"), "BD ATENDIMENTOS")
os.makedirs(caminho, exist_ok=True)

bd = os.path.join(caminho, "pacientes.db")

conexao = sqlite3.connect(bd)
cursor = conexao.cursor()
cursor.execute('SELECT * FROM pacientes')
linhas = cursor.fetchall()

for linha in linhas:
    print(linha)

conexao.close()