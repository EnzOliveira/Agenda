from PyQt5.QtWidgets import QStyledItemDelegate, QComboBox, QMessageBox
from PyQt5.QtCore import Qt

class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        self.model = model

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.setModel(self.model)
        combo.setModelColumn(0) 
        combo.setEditable(True)
        combo.setInsertPolicy(QComboBox.NoInsert)

        return combo

    def setEditorData(self, editor, index):
        valor = index.data()
        i = editor.findText(valor)
        if i >= 0:
            editor.setCurrentIndex(i)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText())
