import os
import sqlite3
from datetime import date, timedelta, datetime, time

class DatabaseManager:
    def __init__(self):
        self.caminho = os.path.join(os.getenv("APPDATA"), "BD ATENDIMENTOS")
        os.makedirs(self.caminho, exist_ok=True)

        self.bd = os.path.join(self.caminho, "horarios.db")

        self.data_min = date(2025, 11, 1)
        self.data_max = date(2028, 12, 31)

    def criar_banco(self):
        conexao = sqlite3.connect(self.bd)
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS horarios (
                Data TEXT NOT NULL,
                Horario TEXT NOT NULL,
                Nome TEXT,
                PRIMARY KEY (Data, Horario)
            )
        """)

        datas = [
            self.data_min + timedelta(days=i)
            for i in range((self.data_max - self.data_min).days + 1)
        ]

        horarios = []
        hora_atual = datetime.combine(date.today(), time(8, 0))
        hora_final = datetime.combine(date.today(), time(22, 0))

        while hora_atual <= hora_final:
            horarios.append(hora_atual.strftime("%H:%M"))
            hora_atual += timedelta(minutes=30)

        for d in datas:
            for h in horarios:
                cursor.execute("""
                    INSERT OR IGNORE INTO horarios (Data, Horario)
                    VALUES (?, ?)
                """, (d.strftime("%d-%m-%Y"), h))

        conexao.commit()
        conexao.close()
