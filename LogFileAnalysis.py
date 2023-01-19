from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from mainGUI import Ui_MainWindow


class LogFileAnalysis(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()