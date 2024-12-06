# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_rule.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHeaderView, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSplitter, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(560, 416)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 521, 51))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.parameter_selection = QComboBox(self.layoutWidget)
        self.parameter_selection.addItem("")
        self.parameter_selection.setObjectName(u"parameter_selection")

        self.gridLayout.addWidget(self.parameter_selection, 1, 0, 1, 1)

        self.value_lable = QLabel(self.layoutWidget)
        self.value_lable.setObjectName(u"value_lable")

        self.gridLayout.addWidget(self.value_lable, 0, 2, 1, 1)

        self.rule_add = QPushButton(self.layoutWidget)
        self.rule_add.setObjectName(u"rule_add")

        self.gridLayout.addWidget(self.rule_add, 1, 3, 1, 1)

        self.parameter_lable = QLabel(self.layoutWidget)
        self.parameter_lable.setObjectName(u"parameter_lable")

        self.gridLayout.addWidget(self.parameter_lable, 0, 0, 1, 1)

        self.operator_lable = QLabel(self.layoutWidget)
        self.operator_lable.setObjectName(u"operator_lable")

        self.gridLayout.addWidget(self.operator_lable, 0, 1, 1, 1)

        self.operator_selection = QComboBox(self.layoutWidget)
        self.operator_selection.addItem("")
        self.operator_selection.addItem("")
        self.operator_selection.addItem("")
        self.operator_selection.addItem("")
        self.operator_selection.addItem("")
        self.operator_selection.setObjectName(u"operator_selection")

        self.gridLayout.addWidget(self.operator_selection, 1, 1, 1, 1)

        self.rule_value = QPlainTextEdit(self.layoutWidget)
        self.rule_value.setObjectName(u"rule_value")

        self.gridLayout.addWidget(self.rule_value, 1, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 80, 52, 16))
        self.rules_table = QTableWidget(Dialog)
        if (self.rules_table.columnCount() < 5):
            self.rules_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.rules_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.rules_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.rules_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.rules_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.rules_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.rules_table.setObjectName(u"rules_table")
        self.rules_table.setGeometry(QRect(20, 140, 521, 221))
        self.accept_rules_button = QPushButton(Dialog)
        self.accept_rules_button.setObjectName(u"accept_rules_button")
        self.accept_rules_button.setGeometry(QRect(20, 370, 521, 24))
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 100, 521, 31))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.rule_view_text = QPlainTextEdit(self.splitter)
        self.rule_view_text.setObjectName(u"rule_view_text")
        self.splitter.addWidget(self.rule_view_text)
        self.update_button = QPushButton(self.splitter)
        self.update_button.setObjectName(u"update_button")
        self.splitter.addWidget(self.update_button)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.parameter_selection.setItemText(0, QCoreApplication.translate("Dialog", u"123", None))

        self.value_lable.setText(QCoreApplication.translate("Dialog", u"Value", None))
        self.rule_add.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.parameter_lable.setText(QCoreApplication.translate("Dialog", u"Parameter", None))
        self.operator_lable.setText(QCoreApplication.translate("Dialog", u"Operator", None))
        self.operator_selection.setItemText(0, QCoreApplication.translate("Dialog", u"=", None))
        self.operator_selection.setItemText(1, QCoreApplication.translate("Dialog", u"<", None))
        self.operator_selection.setItemText(2, QCoreApplication.translate("Dialog", u">", None))
        self.operator_selection.setItemText(3, QCoreApplication.translate("Dialog", u"<=", None))
        self.operator_selection.setItemText(4, QCoreApplication.translate("Dialog", u">=", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Rule View", None))
        ___qtablewidgetitem = self.rules_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.rules_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Parameter", None));
        ___qtablewidgetitem2 = self.rules_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Operator", None));
        ___qtablewidgetitem3 = self.rules_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Value", None));
        self.accept_rules_button.setText(QCoreApplication.translate("Dialog", u"Accept", None))
        self.update_button.setText(QCoreApplication.translate("Dialog", u"Update", None))
    # retranslateUi

