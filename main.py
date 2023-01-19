import sys
from PyQt5.QtWidgets import QApplication
from LogFileAnalysis import LogFileAnalysis

app = QApplication(sys.argv)

library = LogFileAnalysis()

sys.exit(app.exec_())