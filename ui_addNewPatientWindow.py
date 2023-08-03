# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addNewPatientWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGroupBox, QLabel, QPushButton,
    QScrollArea, QScrollBar, QSizePolicy, QTextEdit,
    QWidget)

class Ui_AddNewPatientWindow(object):
    def setupUi(self, AddNewPatientWindow):
        if not AddNewPatientWindow.objectName():
            AddNewPatientWindow.setObjectName(u"AddNewPatientWindow")
        AddNewPatientWindow.resize(891, 947)
        icon = QIcon()
        iconThemeName = u"camera-web"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        AddNewPatientWindow.setWindowIcon(icon)
        self.scrollArea = QScrollArea(AddNewPatientWindow)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-10, 0, 901, 861))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 897, 857))
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 880, 200))
        self.name_textEdit = QTextEdit(self.groupBox)
        self.name_textEdit.setObjectName(u"name_textEdit")
        self.name_textEdit.setGeometry(QRect(60, 60, 131, 31))
        self.name_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.tel_label = QLabel(self.groupBox)
        self.tel_label.setObjectName(u"tel_label")
        self.tel_label.setGeometry(QRect(10, 110, 51, 21))
        self.birthdata_label = QLabel(self.groupBox)
        self.birthdata_label.setObjectName(u"birthdata_label")
        self.birthdata_label.setGeometry(QRect(410, 60, 71, 21))
        self.remark_textEdit = QTextEdit(self.groupBox)
        self.remark_textEdit.setObjectName(u"remark_textEdit")
        self.remark_textEdit.setGeometry(QRect(80, 150, 251, 31))
        self.remark_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.address_label = QLabel(self.groupBox)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(310, 110, 111, 31))
        self.birth_dateEdit = QDateEdit(self.groupBox)
        self.birth_dateEdit.setObjectName(u"birth_dateEdit")
        self.birth_dateEdit.setGeometry(QRect(490, 60, 165, 42))
        self.birth_dateEdit.setStyleSheet(u"")
        self.birth_dateEdit.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.birth_dateEdit.setCalendarPopup(True)
        self.birth_dateEdit.setCurrentSectionIndex(0)
        self.birth_dateEdit.setTimeSpec(Qt.LocalTime)
        self.birth_dateEdit.setDate(QDate(1999, 1, 1))
        self.remark_label = QLabel(self.groupBox)
        self.remark_label.setObjectName(u"remark_label")
        self.remark_label.setGeometry(QRect(10, 150, 61, 21))
        self.tel_textEdit = QTextEdit(self.groupBox)
        self.tel_textEdit.setObjectName(u"tel_textEdit")
        self.tel_textEdit.setGeometry(QRect(50, 110, 241, 31))
        self.tel_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
"")
        self.gender_label = QLabel(self.groupBox)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setGeometry(QRect(210, 60, 71, 21))
        self.name_label = QLabel(self.groupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(10, 60, 51, 21))
        self.address_textEdit = QTextEdit(self.groupBox)
        self.address_textEdit.setObjectName(u"address_textEdit")
        self.address_textEdit.setGeometry(QRect(420, 110, 331, 71))
        self.address_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.gender_comboBox = QComboBox(self.groupBox)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setGeometry(QRect(270, 60, 125, 36))
        self.gender_comboBox.setStyleSheet(u"")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 141, 31))
        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 200, 880, 240))
        self.medical_history_label = QLabel(self.groupBox_2)
        self.medical_history_label.setObjectName(u"medical_history_label")
        self.medical_history_label.setGeometry(QRect(10, 20, 181, 41))
        self.allergic_history_label = QLabel(self.groupBox_2)
        self.allergic_history_label.setObjectName(u"allergic_history_label")
        self.allergic_history_label.setGeometry(QRect(10, 60, 111, 21))
        self.allergic_history_textEdit = QTextEdit(self.groupBox_2)
        self.allergic_history_textEdit.setObjectName(u"allergic_history_textEdit")
        self.allergic_history_textEdit.setGeometry(QRect(120, 60, 651, 61))
        self.allergic_history_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.past_medical_history_label = QLabel(self.groupBox_2)
        self.past_medical_history_label.setObjectName(u"past_medical_history_label")
        self.past_medical_history_label.setGeometry(QRect(0, 140, 121, 51))
        self.past_medical_history_textEdit = QTextEdit(self.groupBox_2)
        self.past_medical_history_textEdit.setObjectName(u"past_medical_history_textEdit")
        self.past_medical_history_textEdit.setGeometry(QRect(120, 140, 651, 91))
        self.past_medical_history_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(880, 10, 16, 931))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(-60, 440, 1026, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 440, 880, 391))
        self.outpatient_records_label = QLabel(self.groupBox_3)
        self.outpatient_records_label.setObjectName(u"outpatient_records_label")
        self.outpatient_records_label.setGeometry(QRect(10, 0, 221, 41))
        self.chief_complaint_label = QLabel(self.groupBox_3)
        self.chief_complaint_label.setObjectName(u"chief_complaint_label")
        self.chief_complaint_label.setGeometry(QRect(10, 50, 111, 21))
        self.chief_complaint_textEdit = QTextEdit(self.groupBox_3)
        self.chief_complaint_textEdit.setObjectName(u"chief_complaint_textEdit")
        self.chief_complaint_textEdit.setGeometry(QRect(130, 50, 651, 51))
        self.chief_complaint_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.history_of_the_present_illness_label = QLabel(self.groupBox_3)
        self.history_of_the_present_illness_label.setObjectName(u"history_of_the_present_illness_label")
        self.history_of_the_present_illness_label.setGeometry(QRect(10, 110, 111, 81))
        self.history_of_the_present_illness_textEdit = QTextEdit(self.groupBox_3)
        self.history_of_the_present_illness_textEdit.setObjectName(u"history_of_the_present_illness_textEdit")
        self.history_of_the_present_illness_textEdit.setGeometry(QRect(130, 110, 651, 91))
        self.history_of_the_present_illness_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
"")
        self.examinination_label = QLabel(self.groupBox_3)
        self.examinination_label.setObjectName(u"examinination_label")
        self.examinination_label.setGeometry(QRect(10, 210, 111, 21))
        self.diagnosis_label = QLabel(self.groupBox_3)
        self.diagnosis_label.setObjectName(u"diagnosis_label")
        self.diagnosis_label.setGeometry(QRect(10, 270, 111, 21))
        self.examinination_textEdit = QTextEdit(self.groupBox_3)
        self.examinination_textEdit.setObjectName(u"examinination_textEdit")
        self.examinination_textEdit.setGeometry(QRect(130, 210, 651, 51))
        self.examinination_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.diagnosis_textEdit = QTextEdit(self.groupBox_3)
        self.diagnosis_textEdit.setObjectName(u"diagnosis_textEdit")
        self.diagnosis_textEdit.setGeometry(QRect(130, 270, 651, 41))
        self.diagnosis_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.remedy_label = QLabel(self.groupBox_3)
        self.remedy_label.setObjectName(u"remedy_label")
        self.remedy_label.setGeometry(QRect(10, 320, 111, 21))
        self.remedy_textEdit = QTextEdit(self.groupBox_3)
        self.remedy_textEdit.setObjectName(u"remedy_textEdit")
        self.remedy_textEdit.setGeometry(QRect(130, 320, 651, 81))
        self.remedy_textEdit.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2.raise_()
        self.verticalScrollBar.raise_()
        self.line_2.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.ok_pushButton = QPushButton(AddNewPatientWindow)
        self.ok_pushButton.setObjectName(u"ok_pushButton")
        self.ok_pushButton.setGeometry(QRect(680, 890, 103, 36))
        self.print_pushButton = QPushButton(AddNewPatientWindow)
        self.print_pushButton.setObjectName(u"print_pushButton")
        self.print_pushButton.setGeometry(QRect(20, 880, 111, 41))
        self.cancel_pushButton = QPushButton(AddNewPatientWindow)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setGeometry(QRect(570, 890, 103, 36))

        self.retranslateUi(AddNewPatientWindow)

        QMetaObject.connectSlotsByName(AddNewPatientWindow)
    # setupUi

    def retranslateUi(self, AddNewPatientWindow):
        AddNewPatientWindow.setWindowTitle(QCoreApplication.translate("AddNewPatientWindow", u"AddNewPatientWindow", None))
        self.groupBox.setTitle("")
        self.tel_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"TEL:", None))
        self.birthdata_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Birth Date:", None))
        self.address_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Home Address:", None))
        self.birth_dateEdit.setDisplayFormat(QCoreApplication.translate("AddNewPatientWindow", u"yyyy/MM/dd", None))
        self.remark_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Remark:", None))
        self.gender_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Gender:", None))
        self.name_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Name:", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("AddNewPatientWindow", u"(Select)", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("AddNewPatientWindow", u"Male", None))
        self.gender_comboBox.setItemText(2, QCoreApplication.translate("AddNewPatientWindow", u"Female", None))

        self.label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Patient Info</span></p></body></html>", None))
        self.groupBox_2.setTitle("")
        self.medical_history_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Medical History</span></p></body></html>", None))
        self.allergic_history_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Allergic History: ", None))
        self.past_medical_history_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">Past Medical </p><p align=\"center\">History:</p></body></html>", None))
        self.groupBox_3.setTitle("")
        self.outpatient_records_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Outpatient Records</span></p></body></html>", None))
        self.chief_complaint_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"Chief Complaint:", None))
        self.history_of_the_present_illness_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">History of the</p><p align=\"center\"> Present </p><p align=\"center\">Illness:</p></body></html>", None))
        self.examinination_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">Examination:</p></body></html>", None))
        self.diagnosis_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">Diagnosis:</p></body></html>", None))
        self.remedy_label.setText(QCoreApplication.translate("AddNewPatientWindow", u"<html><head/><body><p align=\"center\">Remedy:</p></body></html>", None))
        self.ok_pushButton.setText(QCoreApplication.translate("AddNewPatientWindow", u"OK", None))
        self.print_pushButton.setText(QCoreApplication.translate("AddNewPatientWindow", u"Print", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("AddNewPatientWindow", u"Cancel", None))
    # retranslateUi

