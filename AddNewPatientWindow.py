# This Python file uses the following encoding: utf-8
from PySide2.QtCore import QDateTime
from PySide2 import QtWidgets, QtCore
from PySide2.QtCore import Qt, QTimer, QCoreApplication
from PySide2.QtWidgets import  QLabel, QTextEdit, QMessageBox
from PySide2.QtGui import  QKeySequence, QShortcutEvent, QKeyEvent


from ui_addNewPatientWindow import Ui_AddNewPatientWindow

import re

from Database import Database
from Exportdata import Exportdata

class AddNewPatientWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, database : Database):
        super().__init__(parent)

        self.ui = Ui_AddNewPatientWindow()
        self.ui.setupUi(self)
        self.initStyle()
        
        #push button
        self.ui.cancel_pushButton.clicked.connect(self.closeWindow)
        self.ui.ok_pushButton.clicked.connect(self.saveInfo)
        
        self.database = database
        self.exportdata = Exportdata(database)
        
        #error label
        self.error_label = QLabel(self)
        self.error_label.setStyleSheet("color:red")
        
        #focus out event
        self.ui.name_textEdit.focusOutEvent = self.name_txtEdit_focus_out_event
        self.ui.tel_textEdit.focusOutEvent = self.tel_txtEdit_focus_out_event
        self.ui.gender_comboBox.focusOutEvent = self.gender_comboBox_focus_out_event
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000)
        
        # print to pdf
        self.ui.print_pushButton.clicked.connect(self.print_to_pdf)
        
    def initStyle(self):
        self.ui.remark_textEdit.setPlaceholderText("None")
        self.ui.allergic_history_textEdit.setPlaceholderText("None")
        self.ui.past_medical_history_textEdit.setPlaceholderText("None")
        self.ui.chief_complaint_textEdit.setPlaceholderText("None")
        self.ui.history_of_the_present_illness_textEdit.setPlaceholderText("None")
        self.ui.examinination_textEdit.setPlaceholderText("None")
        self.ui.diagnosis_textEdit.setPlaceholderText("None")
        self.ui.remedy_textEdit.setPlaceholderText("None")
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        if isinstance(event, QShortcutEvent) and event.key() == QKeySequence(Qt.CTRL | Qt.Key_W):
            self.close()
        super().keyPressEvent(event)



    def closeWindow(self):
        self.close()
        
    def name_txtEdit_focus_out_event(self, event):
        name = self.ui.name_textEdit.toPlainText()
        pattern = r'^[\u4e00-\u9fa5a-zA-Z]+$'
        coord = self.ui.name_textEdit.geometry().bottomLeft()
        if not re.match(pattern, name):
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText("Invalid Name")           
        else:
            self.error_label.setText("")
            QTextEdit.focusOutEvent(self.ui.tel_textEdit, event)
        
    def tel_txtEdit_focus_out_event(self, event):
        tel = self.ui.tel_textEdit.toPlainText()
        pattern = r'^\d{1,11}$'
        coord = self.ui.tel_textEdit.geometry().bottomLeft()
        if not re.match(pattern, tel):
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText("Invalid TEL number")
        else:
            self.error_label.setText("")
            QTextEdit.focusOutEvent(self.ui.name_textEdit, event)

    def gender_comboBox_focus_out_event(self, event):
        self.error_label.setText("")
        QTextEdit.focusOutEvent(self.ui.name_textEdit, event)
        
    def update_date_time(self):
        self.ui.add_dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        


    def show_confirmation_dialog(self) -> bool:
        formatted_date_time = self.ui.add_dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setIcon(QMessageBox.Warning)
        confirm_dialog.setWindowTitle('Confirmation')
        confirm_dialog.setText(f'Proceed with date and time: {formatted_date_time}?')
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        confirm_dialog.setDefaultButton(QMessageBox.Cancel)

        response = confirm_dialog.exec_()
        if response == QMessageBox.Yes:
            return True            
        else:
            return False


    def saveInfo(self):
        if not self.show_confirmation_dialog():
            return
        #patient table
        name = self.ui.name_textEdit.toPlainText()
        gender = self.ui.gender_comboBox.currentText()
        birthdate = self.ui.birth_dateEdit.date().toString('yyyy-MM-dd')
        tel = self.ui.tel_textEdit.toPlainText()
        address = self.ui.address_textEdit.toPlainText()
        remark = self.ui.remark_textEdit.toPlainText()
        allergic_history = self.ui.allergic_history_textEdit.toPlainText()
        past_medical_history = self.ui.past_medical_history_textEdit.toPlainText()

        if self.error_label.text() != "":
            pass
        elif self.ui.gender_comboBox.currentText() == "(Select)":
            coord = self.ui.gender_comboBox.geometry().bottomLeft()
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText("Please select gender")
        elif self.ui.name_textEdit.toPlainText() == "":
            coord = self.ui.name_textEdit.geometry().bottomLeft()
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText("Invalid Name")   
        elif self.ui.tel_textEdit.toPlainText() == "":
            coord = self.ui.tel_textEdit.geometry().bottomLeft()
            self.error_label.setGeometry(coord.x(), coord.y(), 300, 11)
            self.error_label.setText("Invalid TEL number")   
        else:
            patient_id = self.database.insert_patient(name, gender, birthdate, tel, address, remark, allergic_history, past_medical_history)
                    
        #visit table
        visit_date = self.ui.add_dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        cheif_complaint = self.ui.chief_complaint_textEdit.toPlainText()
        present_illness = self.ui.history_of_the_present_illness_textEdit.toPlainText()
        visit_id = self.database.insert_visit(patient_id, visit_date, cheif_complaint, present_illness)
        
        #logs table
        examination = self.ui.examinination_textEdit.toPlainText()
        diagnosis = self.ui.diagnosis_textEdit.toPlainText()
        remedy = self.ui.remedy_textEdit.toPlainText()
        self.database.insert_log(visit_id, examination, diagnosis, remedy)
        
        self.close()
        
    @QtCore.Slot()
    def reTranslate(self):
        self.ui.retranslateUi(self)
        self.initStyle()


        
    @QtCore.Slot()
    def print_to_pdf(self):
        name = self.ui.name_textEdit.toPlainText()
        gender = self.ui.gender_comboBox.currentText()
        birthdate = self.ui.birth_dateEdit.date().toString('yyyy-MM-dd')
        tel = self.ui.tel_textEdit.toPlainText()
        address = self.ui.address_textEdit.toPlainText()
        remark = self.ui.remark_textEdit.toPlainText()
        allergic_history = self.ui.allergic_history_textEdit.toPlainText()
        past_medical_history = self.ui.past_medical_history_textEdit.toPlainText()
        visit_date = self.ui.add_dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        chief_complaint = self.ui.chief_complaint_textEdit.toPlainText()
        present_illness = self.ui.history_of_the_present_illness_textEdit.toPlainText()
        examination = self.ui.examinination_textEdit.toPlainText()
        diagnosis = self.ui.diagnosis_textEdit.toPlainText()
        remedy = self.ui.remedy_textEdit.toPlainText()
        
        # Create a table with the data
        data = [[QCoreApplication.translate("AddNewPatientWindow", u"Name", None), name],
                [QCoreApplication.translate("AddNewPatientWindow", u"Gender", None), gender],
                [QCoreApplication.translate("AddNewPatientWindow", u"Birthdate", None), birthdate],
                [QCoreApplication.translate("AddNewPatientWindow", u"Telephone", None), tel],
                [QCoreApplication.translate("AddNewPatientWindow", u"Address", None), address],
                [QCoreApplication.translate("AddNewPatientWindow", u"Remark", None), remark],
                [QCoreApplication.translate("AddNewPatientWindow", u"Allergic History", None), allergic_history],
                [QCoreApplication.translate("AddNewPatientWindow", u"Past Medical History", None), past_medical_history],
                [QCoreApplication.translate("AddNewPatientWindow", u"Visit Date", None), visit_date],
                [QCoreApplication.translate("AddNewPatientWindow", u"Chief Complaint", None), chief_complaint],
                [QCoreApplication.translate("AddNewPatientWindow", u"Present Illness", None), present_illness],
                [QCoreApplication.translate("AddNewPatientWindow", u"Examination", None), examination],
                [QCoreApplication.translate("AddNewPatientWindow", u"Diagnosis", None), diagnosis],
                [QCoreApplication.translate("AddNewPatientWindow", u"Remedy", None), remedy]]

        self.exportdata.print_to_pdf(data, filename=name)
        QMessageBox.information(self, QCoreApplication.translate("AddNewPatientWindow", u"Success!", None), name + QCoreApplication.translate("AddNewPatientWindow", u" printed as PDF file", None))
        






