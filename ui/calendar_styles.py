from PyQt5.QtGui import QTextCharFormat, QColor, QBrush, QFont
from PyQt5.QtCore import Qt


class CalendarStyles:
    # ----------- DIA ATUAL -------------
    @staticmethod
    def dia_atual():
        fmt = QTextCharFormat()
        fmt.setForeground(Qt.black)
        fmt.setFontWeight(QFont.Bold)
        fmt.setFontPointSize(13)
        fmt.setToolTip("Hoje")
        return fmt

    # ----------- DIA ATUAL CHEIO -------------
    @staticmethod
    def dia_atual_cheio():
        fmt = QTextCharFormat()
        fmt.setBackground(QBrush(QColor("#C45656")))
        fmt.setForeground(Qt.black)
        fmt.setFontWeight(QFont.Bold)
        fmt.setFontPointSize(13)
        fmt.setToolTip("Hoje - Dia Cheio")
        return fmt

    # ----------- DIA ATUAL PARCIAL -------------
    @staticmethod
    def dia_atual_parcial():
        fmt = QTextCharFormat()
        fmt.setBackground(QBrush(QColor("#FDE34E")))
        fmt.setForeground(Qt.black)
        fmt.setFontWeight(QFont.Bold)
        fmt.setFontPointSize(13)
        fmt.setToolTip("Hoje - Dia Parcialmente Cheio")
        return fmt

    # ----------- DIA CHEIO -------------
    @staticmethod
    def dia_cheio():
        fmt = QTextCharFormat()
        fmt.setBackground(QBrush(QColor("#C45656")))
        fmt.setToolTip("Dia Cheio")
        return fmt

    # ----------- DIA PARCIAL -------------
    @staticmethod
    def dia_parcial():
        fmt = QTextCharFormat()
        fmt.setBackground(QBrush(QColor("#FDE34E")))
        fmt.setToolTip("Dia Parcialmente Cheio")
        return fmt

    # ----------- DIA LIVRE -------------
    @staticmethod
    def dia_livre():
        fmt = QTextCharFormat()
        fmt.setToolTip("Dia Livre")
        return fmt

    # ----------- DIA DE FOLGA -------------
    @staticmethod
    def folgas():
        fmt = QTextCharFormat()
        fmt.setBackground(QBrush(QColor("#EFB04C")))
        fmt.setToolTip("Folga")
        return fmt