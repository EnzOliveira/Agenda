from PyQt5.QtSql import QSqlTableModel
from datetime import date

class HorariosModel(QSqlTableModel):
    def __init__(self, parent, db):
        super().__init__(parent, db)
        self.setTable("horarios")
        self.setFilter(f"Data = '{date.today().strftime('%d-%m-%Y')}'")
        self.select()
