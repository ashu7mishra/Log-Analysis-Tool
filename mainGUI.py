from PyQt5 import QtCore, QtGui, QtWidgets, uic


class Ui_MainWindow(object):
    def setupUi(self):
        super(Ui_MainWindow, self).__init__()
        uic.loadUi('LogFileAnalysis.ui', self)

