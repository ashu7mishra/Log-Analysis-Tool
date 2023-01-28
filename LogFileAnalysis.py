from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from mainGUI import Ui_MainWindow
import os
import json
import pandas as pd


class LogFileAnalysis(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
        self.ResettoolButton.setIcon(QIcon('reset.PNG'))
        self.RightPayloadlabel.hide()
        self.RightPayloadpushButton.hide()
        self.RightPayloadtextEdit.hide()
        self.ParameterLeftPayloadlabel.setEnabled(False)
        self.ParameterLeftPayloadtableView.setEnabled(False)
        self.ParameterRightPayloadlabel.setEnabled(False)
        self.ParameterRightPayloadtableView.setEnabled(False)
        self.label.setEnabled(False)
        self.label_2.setEnabled(False)
        self.label_3.setEnabled(False)
        self.LeftPayloadParameterCountlabel.setEnabled(False)
        self.RightPayloadParameterCountlabel.setEnabled(False)
        self.label_8.setEnabled(False)
        self.LeftMisCountlabel.setEnabled(False)
        self.RightMisCountlabel.setEnabled(False)
        self.label_11.setEnabled(False)
        self.CommonCountlabel.setEnabled(False)
        self.CommonParameterpushButton.setEnabled(False)
        self.MisMatchedParameterpushButton.setEnabled(False)
        self.AllParameterpushButton.setEnabled(False)
        self.RequestParameterlabel.setEnabled(True)
        self.RequestParametertextEdit.setEnabled(True)
        self.ResponseAcknowledgementlabel.setEnabled(True)
        self.ResponseAcknowledgementtextEdit.setEnabled(True)
        self.ResponseCompletedlabel.setEnabled(True)
        self.ResponseCompletedtextEdit.setEnabled(True)
        self.AnonymousParameterlabel.setEnabled(True)
        self.AnonymousParametertextEdit.setEnabled(True)
        self.GetParameterListpushButton.show()
        self.ComparePayloadpushButton.hide()
        self.RightPayloadPath.hide()
        self.ResettoolButton.clicked.connect(self.reset)
        self.GetParameterradioButton.clicked.connect(self.get_parameter_list)
        self.CompareParameterradioButton.clicked.connect(self.compare_payload)
        self.LeftPayloadpushButton.clicked.connect(self.browse_left_payload_file)
        self.RightPayloadpushButton.clicked.connect(self.browse_right_payload_file)
        self.GetParameterListpushButton.clicked.connect(self.data_edit)

    def reset(self):
        self.LeftPayloadPath.setText('')
        self.LeftPayloadtextEdit.setPlainText('')
        self.RightPayloadPath.setText('')
        self.RightPayloadtextEdit.setPlainText('')
        self.RightPayloadlabel.hide()
        self.RightPayloadpushButton.hide()
        self.RightPayloadtextEdit.hide()
        self.ParameterLeftPayloadlabel.setEnabled(False)
        self.ParameterLeftPayloadtableView.setEnabled(False)
        self.ParameterRightPayloadlabel.setEnabled(False)
        self.ParameterRightPayloadtableView.setEnabled(False)
        self.label.setEnabled(False)
        self.label_2.setEnabled(False)
        self.label_3.setEnabled(False)
        self.LeftPayloadParameterCountlabel.setEnabled(False)
        self.RightPayloadParameterCountlabel.setEnabled(False)
        self.label_8.setEnabled(False)
        self.LeftMisCountlabel.setEnabled(False)
        self.RightMisCountlabel.setEnabled(False)
        self.label_11.setEnabled(False)
        self.CommonCountlabel.setEnabled(False)
        self.CommonParameterpushButton.setEnabled(False)
        self.MisMatchedParameterpushButton.setEnabled(False)
        self.AllParameterpushButton.setEnabled(False)
        self.RequestParameterlabel.setEnabled(True)
        self.RequestParametertextEdit.setEnabled(True)
        self.ResponseAcknowledgementlabel.setEnabled(True)
        self.ResponseAcknowledgementtextEdit.setEnabled(True)
        self.ResponseCompletedlabel.setEnabled(True)
        self.ResponseCompletedtextEdit.setEnabled(True)
        self.AnonymousParameterlabel.setEnabled(True)
        self.AnonymousParametertextEdit.setEnabled(True)
        self.GetParameterListpushButton.show()
        self.ComparePayloadpushButton.hide()
        self.RightPayloadPath.hide()

    def get_parameter_list(self):
        self.RightPayloadlabel.hide()
        self.RightPayloadpushButton.hide()
        self.RightPayloadtextEdit.hide()
        self.ParameterLeftPayloadlabel.setEnabled(False)
        self.ParameterLeftPayloadtableView.setEnabled(False)
        self.ParameterRightPayloadlabel.setEnabled(False)
        self.ParameterRightPayloadtableView.setEnabled(False)
        self.label.setEnabled(False)
        self.label_2.setEnabled(False)
        self.label_3.setEnabled(False)
        self.LeftPayloadParameterCountlabel.setEnabled(False)
        self.RightPayloadParameterCountlabel.setEnabled(False)
        self.label_8.setEnabled(False)
        self.LeftMisCountlabel.setEnabled(False)
        self.RightMisCountlabel.setEnabled(False)
        self.label_11.setEnabled(False)
        self.CommonCountlabel.setEnabled(False)
        self.CommonParameterpushButton.setEnabled(False)
        self.MisMatchedParameterpushButton.setEnabled(False)
        self.AllParameterpushButton.setEnabled(False)
        self.GetParameterListpushButton.show()
        self.ComparePayloadpushButton.hide()
        self.RightPayloadPath.hide()
        self.RequestParameterlabel.setEnabled(True)
        self.RequestParametertextEdit.setEnabled(True)
        self.ResponseAcknowledgementlabel.setEnabled(True)
        self.ResponseAcknowledgementtextEdit.setEnabled(True)
        self.ResponseCompletedlabel.setEnabled(True)
        self.ResponseCompletedtextEdit.setEnabled(True)
        self.AnonymousParameterlabel.setEnabled(True)
        self.AnonymousParametertextEdit.setEnabled(True)

    def compare_payload(self):
        self.RightPayloadlabel.show()
        self.RightPayloadpushButton.show()
        self.RightPayloadtextEdit.show()
        self.ParameterLeftPayloadlabel.setEnabled(True)
        self.ParameterLeftPayloadtableView.setEnabled(True)
        self.ParameterRightPayloadlabel.setEnabled(True)
        self.ParameterRightPayloadtableView.setEnabled(True)
        self.label.setEnabled(True)
        self.label_2.setEnabled(True)
        self.label_3.setEnabled(True)
        self.LeftPayloadParameterCountlabel.setEnabled(True)
        self.RightPayloadParameterCountlabel.setEnabled(True)
        self.label_8.setEnabled(True)
        self.LeftMisCountlabel.setEnabled(True)
        self.RightMisCountlabel.setEnabled(True)
        self.label_11.setEnabled(True)
        self.CommonCountlabel.setEnabled(True)
        self.CommonParameterpushButton.setEnabled(True)
        self.MisMatchedParameterpushButton.setEnabled(True)
        self.AllParameterpushButton.setEnabled(True)
        self.GetParameterListpushButton.hide()
        self.ComparePayloadpushButton.show()
        self.RightPayloadPath.show()
        self.RequestParameterlabel.setEnabled(False)
        self.RequestParametertextEdit.setEnabled(False)
        self.ResponseAcknowledgementlabel.setEnabled(False)
        self.ResponseAcknowledgementtextEdit.setEnabled(False)
        self.ResponseCompletedlabel.setEnabled(False)
        self.ResponseCompletedtextEdit.setEnabled(False)
        self.AnonymousParameterlabel.setEnabled(False)
        self.AnonymousParametertextEdit.setEnabled(False)

    def browse_left_payload_file(self):
        file_name = QFileDialog.getOpenFileName(directory="..\Log File Analysis") #filter="*.txt"
        try:
            file_data = open(file_name[0], "r+")
            path = str(file_name)
            path = path.split(',')
            file_path = path[0][1:]
            self.LeftPayloadPath.setText(file_path)
            try:
                self.LeftPayloadtextEdit.setPlainText(file_data.read())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Information")
                msg.setText("Unable to read file")
                msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Information")
            msg.setText("Please select a file")
            msg.exec_()

    def browse_right_payload_file(self):
        file_name = QFileDialog.getOpenFileName(directory="..\Log File Analysis") #filter="*.txt"
        try:
            file_data = open(file_name[0], "r+")
            path = str(file_name)
            path = path.split(',')
            file_path = path[0][1:]
            self.RightPayloadPath.setText(file_path)
            try:
                self.RightPayloadtextEdit.setPlainText(file_data.read())
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Information")
                msg.setText("Unable to read file")
                msg.exec_()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Information")
            msg.setText("Please select a file")
            msg.exec_()

    def parse_json_data(self, data, dictionary, keys):
        if type(data) is dict and data:
            for key in data:
                if key not in keys:
                    keys.append(key)
                    dictionary[key] = [data[key]]
                else:
                    dictionary[key].append(data[key])
                self.parse_json_data(data[key], dictionary, keys)
        elif type(data) is list and data:
            for item in data:
                self.parse_json_data(item, dictionary, keys)

    def data_edit(self):
        data = self.LeftPayloadtextEdit.toPlainText()
        data = json.loads(data)
        dictionary = {}
        keys = []
        self.parse_json_data(data, dictionary, keys)
        df = pd.DataFrame(dictionary)
        print(keys)
        print(dictionary)
        print(df)








