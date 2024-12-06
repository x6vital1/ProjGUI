# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSplitter, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(615, 547)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.output_table = QTableWidget(self.centralwidget)
        if (self.output_table.columnCount() < 2):
            self.output_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.output_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.output_table.setObjectName(u"output_table")
        self.output_table.setGeometry(QRect(280, 30, 311, 411))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(8, 8, 258, 246))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.input_text_label = QLabel(self.layoutWidget)
        self.input_text_label.setObjectName(u"input_text_label")

        self.verticalLayout.addWidget(self.input_text_label)

        self.input_text = QPlainTextEdit(self.layoutWidget)
        self.input_text.setObjectName(u"input_text")

        self.verticalLayout.addWidget(self.input_text)

        self.process_text_button = QPushButton(self.layoutWidget)
        self.process_text_button.setObjectName(u"process_text_button")

        self.verticalLayout.addWidget(self.process_text_button)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 270, 260, 272))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.rules_label = QLabel(self.widget)
        self.rules_label.setObjectName(u"rules_label")

        self.verticalLayout_3.addWidget(self.rules_label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter_2 = QSplitter(self.widget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Orientation.Vertical)
        self.rules_list = QListWidget(self.splitter_2)
        self.rules_list.setObjectName(u"rules_list")
        self.splitter_2.addWidget(self.rules_list)
        self.splitter = QSplitter(self.splitter_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.edit_rule_button = QPushButton(self.splitter)
        self.edit_rule_button.setObjectName(u"edit_rule_button")
        self.splitter.addWidget(self.edit_rule_button)
        self.delete_rule_button = QPushButton(self.splitter)
        self.delete_rule_button.setObjectName(u"delete_rule_button")
        self.splitter.addWidget(self.delete_rule_button)
        self.splitter_2.addWidget(self.splitter)

        self.verticalLayout_2.addWidget(self.splitter_2)

        self.add_rule_button = QPushButton(self.widget)
        self.add_rule_button.setObjectName(u"add_rule_button")

        self.verticalLayout_2.addWidget(self.add_rule_button)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(290, 450, 291, 31))
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.passed_rule_text = QPlainTextEdit(self.splitter_3)
        self.passed_rule_text.setObjectName(u"passed_rule_text")
        self.splitter_3.addWidget(self.passed_rule_text)
        self.start_button = QPushButton(self.splitter_3)
        self.start_button.setObjectName(u"start_button")
        self.splitter_3.addWidget(self.start_button)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CryptoGUI", None))
        ___qtablewidgetitem = self.output_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"parameter", None));
        ___qtablewidgetitem1 = self.output_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"value", None));
        self.input_text_label.setText(QCoreApplication.translate("MainWindow", u"Input Text", None))
        self.process_text_button.setText(QCoreApplication.translate("MainWindow", u"Process Text", None))
        self.rules_label.setText(QCoreApplication.translate("MainWindow", u"Rules", None))
        self.edit_rule_button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_rule_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.add_rule_button.setText(QCoreApplication.translate("MainWindow", u"Add Rule", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

