from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QSpinBox, QGroupBox, QTabWidget, QPushButton, QMessageBox, QInputDialog, QLineEdit, QFileDialog, QFrame
from database.db_pacientes import DatabasePacientes
import sys
import sqlite3

# Gerar janela
class RegistrarPacientes(QDialog):
    def __init__(self):
        super().__init__()

        # ✅ cria o banco
        self.db_pacientes = DatabasePacientes()
        self.db_pacientes.criar_banco()

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
        opcoes = self.atualizar_opcoes() # atualiza a lista de pacientes do ComboBox
        self.nome_paciente.addItems(opcoes)
        self.layout_principal.addWidget(self.nome_paciente)

        self.adicionar_btn = QPushButton('Adicionar ➕')
        self.adicionar_btn.clicked.connect(self.adicionar)
        self.layout_frame_botoes.addWidget(self.adicionar_btn)
        
        self.remover_btn = QPushButton('Remover ❌')
        self.remover_btn.clicked.connect(self.remover)
        self.layout_frame_botoes.addWidget(self.remover_btn)

        self.cancelar_btn = QPushButton('Cancelar')
        self.cancelar_btn.clicked.connect(self.cancelar)
        self.layout_frame_botoes.addWidget(self.cancelar_btn)
        
        self.layout_principal.addWidget(self.frame_botoes)

        # Setando layouts na janela
        self.setLayout(self.layout_principal)

    # Inserir aqui funções de ação dos elementos
    def adicionar(self):
        bd = self.db_pacientes.bd
        conexao = sqlite3.connect(bd)
        cursor = conexao.cursor()

        nome = self.nome_paciente.currentText()
        if nome != "":
            try:
                cursor.execute(
                    "INSERT INTO pacientes (Nome) VALUES (?)",
                    (nome,)
                )
                conexao.commit()
                QMessageBox.information(self, "Sucesso", f'O nome "{nome}" foi adicionado!')

                self.update()

            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Nome existente", f'O nome "{nome}" já existe!')
        else:
            QMessageBox.warning(self, "Erro de digitação", 'O nome não pode ser vazio')

        conexao.close()

    def remover(self):
        bd = self.db_pacientes.bd
        conexao = sqlite3.connect(bd)
        cursor = conexao.cursor()

        nome = self.nome_paciente.currentText()

        if nome != "":
            try:
                print('Deletando...')
                cursor.execute(f'DELETE FROM pacientes WHERE Nome = "{nome}"')
                conexao.commit()
                QMessageBox.information(self, "Sucesso", f'O nome "{nome}" foi removido!')
                self.update()

            except sqlite3.IntegrityError:
                QMessageBox.warning(self, "Impossível remover", f'O nome "{nome}" não existe!')
        else:
            QMessageBox.warning(self, "Erro de digitação", 'O nome não pode ser vazio')

    def cancelar(self):
        self.close()

    def atualizar_opcoes(self):
        bd = self.db_pacientes.bd
        conexao = sqlite3.connect(bd)
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM pacientes')
        opcoes = cursor.fetchall()

        return [item[0] for item in opcoes]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = RegistrarPacientes()
    janela.show()
    sys.exit(app.exec_())