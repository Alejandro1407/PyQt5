from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QObject, pyqtSlot, pyqtSignal

class widgetSignals(QObject):

    sucess = pyqtSignal(object)

class widget(QWidget):

    def __init__(self):
        self.signals = widgetSignals()
        QWidget.__init__(self)

    def sucess(self, result:object):
        reply = QMessageBox.question(
            self, "Confirmacion",
            "¿Abrir este proyecto?",
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.signals.sucess.emit(result)
        else:
            pass


