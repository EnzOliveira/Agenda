from PyQt5.QtWidgets import QApplication, QDialog, QFormLayout, QWidget, QDateEdit, QTimeEdit, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QSpinBox, QGroupBox, QTabWidget, QPushButton, QMessageBox, QInputDialog, QLineEdit, QFileDialog, QFrame
from PyQt5.QtCore import QDate, QTime
import sys
import sqlite3

# Gerar janela
class PacientesFixos(QDialog):
    def __init__(self):
        super().__init__()
        # Definindo o título e tamanho da janela
        self.setWindowTitle('Registrar Horários de Pacientes')
        self.setGeometry(600, 250, 110, 100)

        # Definindo layouts da janela
        self.layout_principal = QFormLayout()

        # Inserir aqui elementos gráficos da janela
        # ---------------------------- NOMES DE PACIENTES E LABEL ----------------------------
        self.label_nome_paciente = QLabel('Nome do Paciente')

        self.intput_nome_paciente = QComboBox()
        self.intput_nome_paciente.setEditable(True)
        op = []
        self.intput_nome_paciente.addItems(op)

        # ---------------------------- CAMPO DE DATAS E LABELS ----------------------------
        self.label_dia_partida = QLabel('Apartir de:')

        self.data_partida = QDateEdit()
        data_inicio = QDate.currentDate()
        data_fim = QDate(2028, 12, 31)
        self.data_partida.setCalendarPopup(True)
        self.data_partida.setMinimumDate(data_inicio)
        self.data_partida.setMaximumDate(data_fim)
        self.data_partida.setDate(QDate.currentDate())
        self.data_partida.dateChanged.connect(self.atualizar_data_final)
        
        self.label_dia_final = QLabel('Até:')
        
        data_partida = self.data_partida.date() # Pega a data selecionada no campo anterior para limitar a escolha a partir de tal data

        self.data_final = QDateEdit()
        data_inicio = data_partida
        data_fim = QDate(2028, 12, 31)
        self.data_final.setCalendarPopup(True)
        self.data_final.setMinimumDate(data_inicio)
        self.data_final.setMaximumDate(data_fim)
        self.data_final.setDate(data_partida)
        self.layout_principal.addWidget(self.data_final)

        # ---------------------------- BOTÕES ----------------------------
        self.cancelar_btn = QPushButton('Cancelar')
        self.cancelar_btn.clicked.connect(self.cancelar)
        
        self.confirmar_btn = QPushButton('Confirmar')
        self.confirmar_btn.clicked.connect(self.confirmar)

        # Inserido elementos no(s) layout(s)
        self.layout_principal.addRow(self.label_nome_paciente)
        self.layout_principal.addRow(self.intput_nome_paciente)
        self.layout_principal.addRow(self.label_dia_partida, self.label_dia_final)
        self.layout_principal.addRow(self.data_partida, self.data_final)
        self.layout_principal.addRow(self.cancelar_btn, self.confirmar_btn)

        # Setando layouts na janela
        self.setLayout(self.layout_principal)

    # Inserir aqui funções de ação dos elementos
    def confirmar(self):
        pass

    def cancelar(self):
        pass

    def atualizar_data_final(self, nova_data):
        self.data_final.setMinimumDate(nova_data)

        # Se a data final for menor que a inicial, corrige
        if self.data_final.date() < nova_data:
            self.data_final.setDate(nova_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = PacientesFixos()
    janela.show()
    sys.exit(app.exec_())