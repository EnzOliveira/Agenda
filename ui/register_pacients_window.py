from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QSpinBox, QGroupBox, QTabWidget, QPushButton, QMessageBox, QInputDialog, QLineEdit, QFileDialog, QFrame
import sys
import sqlite3

# Gerar janela
class RegistrarPacientes(QDialog):
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

        self.label_dia_semana = QLabel('Dia da Semana')
        self.layout_principal.addWidget(self.label_dia_semana)

        self.dia_semana = QComboBox()
        dias_semana = ['seg', 'ter', 'qua', 'qui', 'sex', 'sáb', 'dom']
        self.dia_semana.addItems(dias_semana)
        self.layout_principal.addWidget(self.dia_semana)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = RegistrarPacientes()
    janela.show()
    sys.exit(app.exec_())