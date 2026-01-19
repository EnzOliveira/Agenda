import os
import sqlite3

class DatabasePacientes:
    def __init__(self):
        self.caminho = os.path.join(os.getenv("APPDATA"), "BD ATENDIMENTOS")
        os.makedirs(self.caminho, exist_ok=True)

        self.bd = os.path.join(self.caminho, "pacientes.db")


    def criar_banco(self):
        conexao = sqlite3.connect(self.bd)
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pacientes (
                Nome TEXT,
                PRIMARY KEY (Nome)
            )
        """)

        conexao.commit()
        conexao.close()
