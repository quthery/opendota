# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'opendota.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(550, 250)
        Dialog.setStyleSheet(u"background-color:black;")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 20, 131, 31))
        self.pushButton.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"font-family:Arial;"
)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 381, 41))
        self.lineEdit.setStyleSheet(u"border-color:white;")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 70, 531, 221))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(370, 80, 150, 150))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

