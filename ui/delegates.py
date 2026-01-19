from PyQt5.QtWidgets import QStyledItemDelegate, QComboBox

class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, opcoes, parent=None):
        super().__init__(parent)
        self.opcoes = opcoes

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.addItems(self.opcoes)
        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.NoInsert)

        return combo

    def setEditorData(self, editor, index):
        valor = index.data()
        if valor in self.opcoes:
            editor.setCurrentText(valor)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText())