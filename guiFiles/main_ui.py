# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

from qfluentwidgets import (CaptionLabel, LineEdit, PushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(809, 585)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = CaptionLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.urlEdit = LineEdit(Form)
        self.urlEdit.setObjectName(u"urlEdit")

        self.horizontalLayout.addWidget(self.urlEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = CaptionLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.cookieEdit = LineEdit(Form)
        self.cookieEdit.setObjectName(u"cookieEdit")

        self.horizontalLayout_2.addWidget(self.cookieEdit)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.label_4 = CaptionLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 6))
        self.label_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.outPath = LineEdit(Form)
        self.outPath.setObjectName(u"outPath")

        self.horizontalLayout_3.addWidget(self.outPath)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(0, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.label_5 = CaptionLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(219, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.comboBox)

        self.pushButton = PushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(4, 11))

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.label = CaptionLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setTextInteractionFlags(Qt.TextInteractionFlag.LinksAccessibleByKeyboard|Qt.TextInteractionFlag.LinksAccessibleByMouse)

        self.verticalLayout.addWidget(self.label)

        self.outBrowser = QTextBrowser(Form)
        self.outBrowser.setObjectName(u"outBrowser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.outBrowser.sizePolicy().hasHeightForWidth())
        self.outBrowser.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.outBrowser)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.clearButton = PushButton(Form)
        self.clearButton.setObjectName(u"clearButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.clearButton)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Bilibili Downloader", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u89c6\u9891\u94fe\u63a5\uff1a", None))
        self.urlEdit.setText("")
        self.urlEdit.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"cookie\uff1a", None))
        self.cookieEdit.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u8def\u5f84\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u89e3\u7801\u5668\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"ffmpeg", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"moviepy", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"ffmpeg", None))
        self.comboBox.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa\u7ed3\u679c\uff1a", None))
        self.clearButton.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
    # retranslateUi

