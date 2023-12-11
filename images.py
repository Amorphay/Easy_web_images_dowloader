# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(720, 476)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 50, 301, 31))
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(370, 50, 321, 361))
        self.plainTextEdit.setReadOnly(True)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 420, 261, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 423, 151, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 54, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 30, 54, 16))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 90, 161, 20))
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 160, 301, 22))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 140, 54, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 30, 54, 16))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 110, 221, 16))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 220, 54, 16))
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(20, 330, 301, 22))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 370, 301, 21))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 250, 54, 16))
        self.comboBox_3 = QComboBox(Form)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(20, 270, 241, 22))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 310, 54, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Easy web images dowloader", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"https://www.keromakura.net", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"start", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Clear History", None))
        self.label.setText(QCoreApplication.translate("Form", u"Url:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Log", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u" parse url automatically", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"images", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"url", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"To get:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"(like this)", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"(forcibly change the format of the url)", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"To save:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"directory with the same name of the url", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"input yourself", None))

        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Directory name if you choose to input yourself", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Format:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Form", u"orginal format of the file(recommend)", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Form", u"jpg", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Form", u"png", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Form", u"jif", None))

        self.label_8.setText(QCoreApplication.translate("Form", u"Path:", None))
    # retranslateUi

