# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatientInfoWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDateTimeEdit, QFrame, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextBrowser, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_PatientInfoWIndow(object):
    def setupUi(self, PatientInfoWIndow):
        if not PatientInfoWIndow.objectName():
            PatientInfoWIndow.setObjectName(u"PatientInfoWIndow")
        PatientInfoWIndow.resize(967, 833)
        self.up_groupBox = QGroupBox(PatientInfoWIndow)
        self.up_groupBox.setObjectName(u"up_groupBox")
        self.up_groupBox.setGeometry(QRect(0, 0, 951, 111))
        self.name_label = QLabel(self.up_groupBox)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(10, 20, 66, 18))
        self.name_lineEdit = QLineEdit(self.up_groupBox)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setGeometry(QRect(60, 10, 113, 36))
        self.gender_label = QLabel(self.up_groupBox)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setGeometry(QRect(190, 20, 66, 18))
        self.tel_lineEdit = QLineEdit(self.up_groupBox)
        self.tel_lineEdit.setObjectName(u"tel_lineEdit")
        self.tel_lineEdit.setGeometry(QRect(420, 10, 151, 36))
        self.gender_comboBox = QComboBox(self.up_groupBox)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setGeometry(QRect(250, 10, 125, 36))
        self.tel_label = QLabel(self.up_groupBox)
        self.tel_label.setObjectName(u"tel_label")
        self.tel_label.setGeometry(QRect(380, 20, 66, 18))
        self.remark_lineEdit = QLineEdit(self.up_groupBox)
        self.remark_lineEdit.setObjectName(u"remark_lineEdit")
        self.remark_lineEdit.setGeometry(QRect(610, 60, 201, 36))
        self.remark_label = QLabel(self.up_groupBox)
        self.remark_label.setObjectName(u"remark_label")
        self.remark_label.setGeometry(QRect(550, 70, 66, 18))
        self.address_lineEdit = QLineEdit(self.up_groupBox)
        self.address_lineEdit.setObjectName(u"address_lineEdit")
        self.address_lineEdit.setGeometry(QRect(120, 60, 411, 36))
        self.address_label = QLabel(self.up_groupBox)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(10, 70, 111, 18))
        self.edit_mode_checkBox = QCheckBox(self.up_groupBox)
        self.edit_mode_checkBox.setObjectName(u"edit_mode_checkBox")
        self.edit_mode_checkBox.setGeometry(QRect(820, 70, 97, 24))
        self.birthdate_dateEdit = QDateEdit(self.up_groupBox)
        self.birthdate_dateEdit.setObjectName(u"birthdate_dateEdit")
        self.birthdate_dateEdit.setGeometry(QRect(650, 10, 201, 42))
        self.birthdate_label = QLabel(self.up_groupBox)
        self.birthdate_label.setObjectName(u"birthdate_label")
        self.birthdate_label.setGeometry(QRect(580, 20, 66, 18))
        self.down_groupBox = QGroupBox(PatientInfoWIndow)
        self.down_groupBox.setObjectName(u"down_groupBox")
        self.down_groupBox.setGeometry(QRect(0, 111, 961, 711))
        self.treeWidget = QTreeWidget(self.down_groupBox)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Visit Date Time");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(0, 10, 241, 671))
        self.allergic_history_label = QLabel(self.down_groupBox)
        self.allergic_history_label.setObjectName(u"allergic_history_label")
        self.allergic_history_label.setGeometry(QRect(240, 10, 111, 21))
        self.allergic_history_textEdit = QTextEdit(self.down_groupBox)
        self.allergic_history_textEdit.setObjectName(u"allergic_history_textEdit")
        self.allergic_history_textEdit.setGeometry(QRect(349, 10, 591, 61))
        self.past_medical_history_label = QLabel(self.down_groupBox)
        self.past_medical_history_label.setObjectName(u"past_medical_history_label")
        self.past_medical_history_label.setGeometry(QRect(240, 90, 111, 51))
        self.past_medical_history_textEdit = QTextEdit(self.down_groupBox)
        self.past_medical_history_textEdit.setObjectName(u"past_medical_history_textEdit")
        self.past_medical_history_textEdit.setGeometry(QRect(349, 90, 591, 61))
        self.new_pushButton = QPushButton(self.down_groupBox)
        self.new_pushButton.setObjectName(u"new_pushButton")
        self.new_pushButton.setGeometry(QRect(709, 650, 103, 36))
        self.delete_record_pushButton = QPushButton(self.down_groupBox)
        self.delete_record_pushButton.setObjectName(u"delete_record_pushButton")
        self.delete_record_pushButton.setGeometry(QRect(581, 650, 111, 36))
        self.add_record_pushButton = QPushButton(self.down_groupBox)
        self.add_record_pushButton.setObjectName(u"add_record_pushButton")
        self.add_record_pushButton.setGeometry(QRect(829, 650, 103, 36))
        self.chief_complaint_label = QLabel(self.down_groupBox)
        self.chief_complaint_label.setObjectName(u"chief_complaint_label")
        self.chief_complaint_label.setGeometry(QRect(239, 280, 111, 21))
        self.diagnosis_textEdit = QTextEdit(self.down_groupBox)
        self.diagnosis_textEdit.setObjectName(u"diagnosis_textEdit")
        self.diagnosis_textEdit.setGeometry(QRect(359, 500, 581, 41))
        self.diagnosis_textEdit.setStyleSheet(u"")
        self.history_of_the_present_illness_textEdit = QTextEdit(self.down_groupBox)
        self.history_of_the_present_illness_textEdit.setObjectName(u"history_of_the_present_illness_textEdit")
        self.history_of_the_present_illness_textEdit.setGeometry(QRect(359, 340, 581, 91))
        self.history_of_the_present_illness_textEdit.setStyleSheet(u"")
        self.diagnosis_label = QLabel(self.down_groupBox)
        self.diagnosis_label.setObjectName(u"diagnosis_label")
        self.diagnosis_label.setGeometry(QRect(239, 500, 111, 21))
        self.history_of_the_present_illness_label = QLabel(self.down_groupBox)
        self.history_of_the_present_illness_label.setObjectName(u"history_of_the_present_illness_label")
        self.history_of_the_present_illness_label.setGeometry(QRect(239, 340, 111, 81))
        self.examinination_textEdit = QTextEdit(self.down_groupBox)
        self.examinination_textEdit.setObjectName(u"examinination_textEdit")
        self.examinination_textEdit.setGeometry(QRect(359, 440, 581, 51))
        self.examinination_textEdit.setStyleSheet(u"")
        self.chief_complaint_textEdit = QTextEdit(self.down_groupBox)
        self.chief_complaint_textEdit.setObjectName(u"chief_complaint_textEdit")
        self.chief_complaint_textEdit.setGeometry(QRect(359, 280, 581, 51))
        self.chief_complaint_textEdit.setStyleSheet(u"")
        self.remedy_textEdit = QTextEdit(self.down_groupBox)
        self.remedy_textEdit.setObjectName(u"remedy_textEdit")
        self.remedy_textEdit.setGeometry(QRect(359, 550, 581, 81))
        self.remedy_textEdit.setStyleSheet(u"")
        self.examinination_label = QLabel(self.down_groupBox)
        self.examinination_label.setObjectName(u"examinination_label")
        self.examinination_label.setGeometry(QRect(239, 440, 111, 21))
        self.remedy_label = QLabel(self.down_groupBox)
        self.remedy_label.setObjectName(u"remedy_label")
        self.remedy_label.setGeometry(QRect(239, 550, 111, 21))
        self.textBrowser = QTextBrowser(self.down_groupBox)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(249, 200, 251, 61))
        self.textBrowser.setStyleSheet(u"font: 700 11pt \"Liberation Serif\";")
        self.line = QFrame(self.down_groupBox)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(239, 170, 711, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.realtime_dateTimeEdit = QDateTimeEdit(self.down_groupBox)
        self.realtime_dateTimeEdit.setObjectName(u"realtime_dateTimeEdit")
        self.realtime_dateTimeEdit.setGeometry(QRect(574, 230, 241, 42))
        self.realtime_dateTimeEdit.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.realtime_label = QLabel(self.down_groupBox)
        self.realtime_label.setObjectName(u"realtime_label")
        self.realtime_label.setGeometry(QRect(500, 240, 66, 18))
        self.edit_record_checkBox = QCheckBox(self.down_groupBox)
        self.edit_record_checkBox.setObjectName(u"edit_record_checkBox")
        self.edit_record_checkBox.setGeometry(QRect(820, 250, 111, 24))
        self.delete_all_records_pushButton = QPushButton(self.down_groupBox)
        self.delete_all_records_pushButton.setObjectName(u"delete_all_records_pushButton")
        self.delete_all_records_pushButton.setGeometry(QRect(360, 650, 151, 36))
        self.export_button = QPushButton(self.down_groupBox)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setGeometry(QRect(250, 650, 103, 36))

        self.retranslateUi(PatientInfoWIndow)

        QMetaObject.connectSlotsByName(PatientInfoWIndow)
    # setupUi

    def retranslateUi(self, PatientInfoWIndow):
        PatientInfoWIndow.setWindowTitle(QCoreApplication.translate("PatientInfoWIndow", u"PatientInfoWindow", None))
        self.up_groupBox.setTitle("")
        self.name_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Name:", None))
        self.gender_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Gender:", None))
        self.tel_lineEdit.setText("")
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("PatientInfoWIndow", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("PatientInfoWIndow", u"Female", None))

        self.tel_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"TEL:", None))
        self.remark_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Remark:", None))
        self.address_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Home Address:", None))
        self.edit_mode_checkBox.setText(QCoreApplication.translate("PatientInfoWIndow", u"Edit Info", None))
        self.birthdate_dateEdit.setDisplayFormat(QCoreApplication.translate("PatientInfoWIndow", u"yyyy/MM/dd", None))
        self.birthdate_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"<html><head/><body><p>Birthdate:</p></body></html>", None))
        self.down_groupBox.setTitle("")
        self.allergic_history_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Allergic History:", None))
        self.past_medical_history_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"<html><head/><body><p align=\"center\">Past Medical </p><p align=\"center\">History:</p></body></html>", None))
        self.new_pushButton.setText(QCoreApplication.translate("PatientInfoWIndow", u"Clear ", None))
        self.delete_record_pushButton.setText(QCoreApplication.translate("PatientInfoWIndow", u"Delete Record", None))
        self.add_record_pushButton.setText(QCoreApplication.translate("PatientInfoWIndow", u"Add Record", None))
        self.chief_complaint_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Chief Complaint:", None))
        self.diagnosis_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"<html><head/><body><p align=\"center\">Diagnosis:</p></body></html>", None))
        self.history_of_the_present_illness_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"<html><head/><body><p align=\"center\">History of the</p><p align=\"center\"> Present </p><p align=\"center\">Illness:</p></body></html>", None))
        self.examinination_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"<html><head/><body><p align=\"center\">Examination:</p></body></html>", None))
        self.remedy_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"<html><head/><body><p align=\"center\">Remedy:</p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("PatientInfoWIndow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Liberation Serif'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Cantarell'; font-size:22pt;\">Medical Records</span></p></body></html>", None))
        self.realtime_dateTimeEdit.setDisplayFormat(QCoreApplication.translate("PatientInfoWIndow", u"yyyy-MM-dd HH:mm:ss", None))
        self.realtime_label.setText(QCoreApplication.translate("PatientInfoWIndow", u"Realtime:", None))
        self.edit_record_checkBox.setText(QCoreApplication.translate("PatientInfoWIndow", u"Edit Record", None))
        self.delete_all_records_pushButton.setText(QCoreApplication.translate("PatientInfoWIndow", u"Delete All Records", None))
        self.export_button.setText(QCoreApplication.translate("PatientInfoWIndow", u"Export", None))
    # retranslateUi

