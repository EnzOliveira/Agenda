from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QDateEdit, QTimeEdit, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QSpinBox, QGroupBox, QTabWidget, QPushButton, QMessageBox, QInputDialog, QLineEdit, QFileDialog, QFrame
from PyQt5.QtCore import QDate, QTime
import sys
import sqlite3

# Gerar janela
class PacientesFixos(QDialog):
    def __init__(self):
        super().__init__()
        # Definindo o título e tamanho da janela
        self.setWindowTitle('Registrar Horários de Pacientes')
        self.setGeometry(600, 250, 700, 100)

        # Definindo layouts da janela
        self.layout_principal = QVBoxLayout()
        self.frame_botoes = QFrame()
        self.layout_frame_botoes = QHBoxLayout(self.frame_botoes)

        # Inserir aqui elementos gráficos da janela
        self.label_paciente = QLabel('Nome do Paciente')
        self.layout_principal.addWidget(self.label_paciente)

        self.nome_paciente = QComboBox()
        self.nome_paciente.setEditable(True)
        op = []
        self.nome_paciente.addItems(op)
        self.layout_principal.addWidget(self.nome_paciente)

        self.label_dia_semana = QLabel('Apartir de:')
        self.layout_principal.addWidget(self.label_dia_semana)

        self.data_partida = QDateEdit()
        data_inicio = QDate.currentDate()
        data_fim = QDate(2028, 12, 31)

        self.data_partida.setCalendarPopup(True)
        self.data_partida.setMinimumDate(data_inicio)
        self.data_partida.setMaximumDate(data_fim)
        self.data_partida.setDate(QDate.currentDate())
        self.data_partida.dateChanged.connect(self.atualizar_data_final)
        self.layout_principal.addWidget(self.data_partida)


        self.label_dia_semana = QLabel('Até:')
        self.layout_principal.addWidget(self.label_dia_semana)
        
        data_partida = self.data_partida.date()

        
        self.data_final = QDateEdit()
        data_inicio = data_partida
        data_fim = QDate(2028, 12, 31)

        self.data_final.setCalendarPopup(True)
        self.data_final.setMinimumDate(data_inicio)
        self.data_final.setMaximumDate(data_fim)
        self.data_final.setDate(data_partida)
        self.layout_principal.addWidget(self.data_final)

        self.cancelar_btn = QPushButton('Cancelar')
        self.cancelar_btn.clicked.connect(self.cancelar)
        self.layout_frame_botoes.addWidget(self.cancelar_btn)
        
        self.confirmar_btn = QPushButton('Confirmar')
        self.confirmar_btn.clicked.connect(self.confirmar)
        self.layout_frame_botoes.addWidget(self.confirmar_btn)

        self.layout_principal.addWidget(self.frame_botoes)

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