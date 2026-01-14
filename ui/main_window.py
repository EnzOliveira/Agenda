from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QCalendarWidget, QTableView,
    QHeaderView, QMessageBox, QMenu, QPushButton, QApplication
)
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import QDate
from PyQt5.QtCore import Qt

import sqlite3

from datetime import date, timedelta
import sys

from database.db_manager import DatabaseManager
from models.horarios_model import HorariosModel
from ui.calendar_styles import CalendarStyles
from ui.register_pacients_window import RegistrarPacientes

# Gerar janela
class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        # ✅ cria o gerenciador de banco
        self.db_manager = DatabaseManager()

        # ✅ cria o banco
        self.db_manager.criar_banco()

        self.bd = self.db_manager.bd
        self.data_min = self.db_manager.data_min
        self.data_max = self.db_manager.data_max
        self.datas = [
            self.data_min + timedelta(days=i)
            for i in range((self.data_max - self.data_min).days + 1)
        ]

        # Definindo o título e tamanho da janela
        self.setWindowTitle('Agenda')
        self.setGeometry(300, 250, 1300, 540)

        # Definindo layouts da janela
        self.layout_principal = QVBoxLayout()
        self.layout_conteudo = QHBoxLayout()

        # ---------- calendario ------------
        self.calendario = QCalendarWidget()
        self.calendario.setMinimumDate(self.data_min)
        self.calendario.setMaximumDate(self.data_max)
        self.calendario.selectionChanged.connect(self.filtrar_tebela)
        self.layout_conteudo.addWidget(self.calendario)

        # ---------- personalização calendario ------------
        self.personalizar_calendario()

        # Ativa o menu de contexto
        self.calendario.setContextMenuPolicy(Qt.CustomContextMenu)

        # Conecta o sinal do botão direito
        self.calendario.customContextMenuRequested.connect(
            self.abrir_menu
        )

        # --------- tabela das consultas ---------
        
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(self.bd)

        if not db.open():
            QMessageBox.critical(None, "Erro", "Não foi possível conectar ao banco de dados.")
            sys.exit(1)

        # criando o modelo de dados
        self.modelo = QSqlTableModel(self, db)
        self.modelo.setTable("horarios")  # nome da tabela no SQLite
        self.modelo.setFilter(f"Data = '{date.today().strftime('%d-%m-%Y')}'")
        self.modelo.select()  # executa o SELECT automaticamente

        # cria uma tabela visual
        self.tabela_horarios = QTableView()
        self.tabela_horarios.setModel(self.modelo)
        self.tabela_horarios.resizeColumnsToContents()
        self.tabela_horarios.setAlternatingRowColors(True)
        self.tabela_horarios.setMinimumSize(400, 238)
        self.tabela_horarios.hideColumn(0)
        self.tabela_horarios.setSelectionBehavior(QTableView.SelectRows)  # selecionar uma célula seleciona a linha toda
        
        # interceptar alterações
        self.tabela_horarios.model().dataChanged.connect(self.confirmar_alteracao)

        header = self.tabela_horarios.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)  # segunda coluna se ajusta
        header.setSectionResizeMode(2, QHeaderView.Stretch)           # primeria coluna se expande
        self.layout_conteudo.addWidget(self.tabela_horarios)

        self.agendar_paciente_btn = QPushButton('Adicionar Paciente')
        self.agendar_paciente_btn.clicked.connect(self.abri_janela_registrar_pacientes)
        self.layout_principal.addWidget(self.agendar_paciente_btn)

        self.layout_principal.addLayout(self.layout_conteudo)

        # Setando layouts na janela
        self.setLayout(self.layout_principal)

    # Inserir aqui funções de ação dos elementos
    def filtrar_tebela(self):
        data_selecionada = self.calendario.selectedDate().toString("dd-MM-yyyy")
        
        self.modelo.setFilter(f"Data = '{data_selecionada}'")
        self.modelo.select()

    def confirmar_alteracao(self):
        resposta = QMessageBox.question(
            self,
            "Confirmar alteração",
            "Tem certeza que deseja salvar essa modificação?",
            QMessageBox.Yes | QMessageBox.No
        )
        if resposta == QMessageBox.No:
            self.modelo.revertAll()  # desfaz as alterações
        else:
            self.modelo.submitAll()  # confirma e grava no banco
            self.personalizar_calendario()
            self.calendario.update()

    def personalizar_calendario(self):
         # Dia atual
        hoje = QDate.currentDate()
        self.calendario.setDateTextFormat(hoje, CalendarStyles.dia_atual())

        conexao = sqlite3.connect(self.bd)
        cursor = conexao.cursor()

        lista_dias_cheios = []
        lista_dias_parcialmente_cheios = []
        lista_dias_livres = []
        self.lista_folgas = []

        for data in self.datas:
            cursor.execute(
                "SELECT * FROM horarios WHERE Data = ?",
                (data.strftime("%d-%m-%Y"),)
            )
            consulta = cursor.fetchall()

            total = len(consulta)
            ocupados = sum(1 for c in consulta if c[2])

            if ocupados == total:
                lista_dias_cheios.append(data)
            elif ocupados > 0:
                lista_dias_parcialmente_cheios.append(data)
            else:
                lista_dias_livres.append(data)

        for data in lista_dias_cheios:
            qdate = QDate(data.year, data.month, data.day)
            self.calendario.setDateTextFormat(qdate, CalendarStyles.dia_cheio())

        for data in lista_dias_parcialmente_cheios:
            qdate = QDate(data.year, data.month, data.day)
            self.calendario.setDateTextFormat(qdate, CalendarStyles.dia_parcial())

        for data in lista_dias_livres:
            qdate = QDate(data.year, data.month, data.day)
            self.calendario.setDateTextFormat(qdate, CalendarStyles.dia_livre())

        for data in self.lista_folgas:
            qdate = QDate(date.year, date.month, date.day)
            self.calendario.setDateTextFormat(qdate, CalendarStyles.folgas())

        # Reaplica estilo especial se HOJE estiver em alguma lista
        if hoje.toPyDate() in lista_dias_cheios:
            self.calendario.setDateTextFormat(hoje, CalendarStyles.dia_atual_cheio())
        elif hoje.toPyDate() in lista_dias_parcialmente_cheios:
            self.calendario.setDateTextFormat(hoje, CalendarStyles.dia_atual_parcial())
        else:
            self.calendario.setDateTextFormat(hoje, CalendarStyles.dia_atual())

        conexao.close()

    def abrir_menu(self, pos):
        # Data selecionada no calendário
        data = self.calendario.selectedDate()

        menu = QMenu(self)

        acao_marcar_folga = menu.addAction("Marcar como folga")
        acao_remover_folga = menu.addAction("Remover evento")
        acao_marcar_dias_semana = menu.addAction("Agendar paciente para cada 7 dias")

        # Mostra o menu na posição do mouse
        acao = menu.exec_(self.calendario.mapToGlobal(pos))

        if acao == acao_marcar_folga:
            self.lista_folgas.append(data.toString("dd/MM/yyyy"))
            print(self.lista_folgas)
        elif acao == acao_remover_folga:
            print("Remover evento em:", data.toString("dd/MM/yyyy"))
        elif acao == acao_marcar_dias_semana:
            print("Marcado:", data.toString("dd/MM/yyyy"))

    def abri_janela_registrar_pacientes(self):
        dialog = RegistrarPacientes()
        dialog.exec_()  # 🔒 trava a janela anterior
