import sys

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView

from rules.connection import Data
from rules.rules_actions import AddRuleDialog
from ui_main import Ui_MainWindow
from utils.process_rules import check_rules
from utils.process_text import extract_data


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()

        # Connect buttons
        self.ui.add_rule_button.clicked.connect(self.open_rules_window)
        self.ui.edit_rule_button.clicked.connect(self.edit_current_rule)
        self.ui.delete_rule_button.clicked.connect(self.delete_current_rule)
        self.ui.process_text_button.clicked.connect(self.process_text)
        self.ui.start_button.clicked.connect(self.check_rules)

        # Drag and Drop
        self.ui.rules_list.setDragDropMode(QAbstractItemView.InternalMove)

        self.load_rules_list()

    def check_rules(self):
        rules_list = [self.ui.rules_list.item(i).text() for i in range(self.ui.rules_list.count())]
        output_parameters = self.load_parameters_list()

        passed_rule = check_rules(rules_list, output_parameters)

        if passed_rule:
            self.ui.passed_rule_text.setPlainText(f"Passed Rule: {passed_rule}")
        else:
            self.ui.passed_rule_text.setPlainText("Passed Rule: None")

    def process_text(self):
        text = self.ui.input_text.toPlainText()
        data = extract_data(text)
        self.populate_output_table(data)

    def populate_output_table(self, data):
        self.ui.output_table.setRowCount(len(data))
        for i, (key, value) in enumerate(data.items()):
            self.ui.output_table.setItem(i, 0, QtWidgets.QTableWidgetItem(key))
            self.ui.output_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(value)))

    def load_rules_list(self):
        self.ui.rules_list.clear()

        rules = self.conn.get_all_rules()

        for rule_id, rule in rules:
            list_item = QtWidgets.QListWidgetItem(rule)
            list_item.setData(Qt.UserRole, rule_id)
            self.ui.rules_list.addItem(list_item)

    def load_parameters_list(self):
        data_dict = {}

        for row in range(self.ui.output_table.rowCount()):
            param = self.ui.output_table.item(row, 0).text()
            value = self.ui.output_table.item(row, 1).text()
            data_dict[param] = value

        return data_dict

    def open_rules_window(self, r_id):
        output_parameters = self.load_parameters_list()
        self.ui_window = AddRuleDialog(parent=self, r_id=r_id, mode="add", parameters=output_parameters)
        self.ui_window.show()

    def edit_current_rule(self):
        selected_index = self.ui.rules_list.currentIndex()
        output_parameters = self.load_parameters_list()
        if selected_index.isValid():
            r_id = selected_index.data(Qt.UserRole)
            self.ui_window = AddRuleDialog(parent=self, mode="edit", r_id=r_id, parameters=output_parameters)
            self.ui_window.show()

    def delete_current_rule(self):
        selected_index = self.ui.rules_list.currentIndex()

        if selected_index.isValid():
            r_id = selected_index.data(Qt.UserRole)
            self.conn.delete_rule_query(r_id)
            self.load_rules_list()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
