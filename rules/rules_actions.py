from PySide6.QtWidgets import QDialog, QTableWidgetItem, QPushButton

from rules.connection import Data
from ui_rules import Ui_Dialog


class AddRuleDialog(QDialog):
    def __init__(self, parent=None, r_id=None, mode=None, parameters=None):
        super(AddRuleDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.conn = Data()

        self.main_window = parent

        self.r_id = r_id
        self.mode = mode
        self.parameters = parameters

        self.rules_table = self.ui.rules_table

        if mode and r_id:
            self.get_current_rule(r_id)

        # Populate parameters selector
        self.populate_parameters_list(parameters)

        # Connect buttons
        self.ui.rule_add.clicked.connect(self.add_new_rule)
        self.ui.accept_rules_button.clicked.connect(self.accept_rules)
        self.ui.update_button.clicked.connect(self.update_rule_view_text)

    def populate_parameters_list(self, parameters):
        self.ui.parameter_selection.clear()
        for key, value in parameters.items():
            self.ui.parameter_selection.addItem(key)

    def get_current_rule(self, r_id):
        rule = self.conn.get_rule_by_id(r_id)
        parameters = self.conn.get_parameters_by_rule_id(r_id)

        self.ui.rule_view_text.setPlainText(rule)

        for item in parameters:
            row_position = self.rules_table.rowCount()
            self.rules_table.insertRow(row_position)

            # Insert data into table
            self.rules_table.setItem(row_position, 0, QTableWidgetItem(str(item["id"])))
            self.rules_table.setItem(row_position, 1, QTableWidgetItem(item["parameter"]))
            self.rules_table.setItem(row_position, 2, QTableWidgetItem(item["operator"]))
            self.rules_table.setItem(row_position, 3, QTableWidgetItem(str(item["value"])))

            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda: self.delete_row(row_position))
            self.rules_table.setCellWidget(row_position, 4, delete_button)

        self.update_rule_view_text()

    def add_new_rule(self):
        rule_parameter = self.ui.parameter_selection.currentText()
        rule_operator = self.ui.operator_selection.currentText()
        rule_value = self.ui.rule_value.toPlainText()

        row_position = self.rules_table.rowCount()
        self.rules_table.insertRow(row_position)

        # Insert data into table
        self.rules_table.setItem(row_position, 0, QTableWidgetItem("-"))
        self.rules_table.setItem(row_position, 1, QTableWidgetItem(rule_parameter))
        self.rules_table.setItem(row_position, 2, QTableWidgetItem(rule_operator))
        self.rules_table.setItem(row_position, 3, QTableWidgetItem(rule_value))

        # Add delete button
        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda: self.delete_row(row_position))
        self.rules_table.setCellWidget(row_position, 4, delete_button)

        self.update_rule_view_text()

    def delete_row(self, row):
        button_widget = self.rules_table.cellWidget(row, 4)
        if button_widget:
            button_widget.deleteLater()

        self.rules_table.removeRow(row)

        self.update_buttons()
        self.update_rule_view_text()

    def update_buttons(self):
        for row in range(self.rules_table.rowCount()):
            button_widget = self.rules_table.cellWidget(row, 3)
            if button_widget:
                button_widget.clicked.disconnect()
                button_widget.clicked.connect(lambda _, r=row: self.delete_row(r))

    def update_rule_view_text(self):
        rule_texts = []
        row_count = self.rules_table.rowCount()

        for row in range(row_count):
            parameter = self.rules_table.item(row, 1).text()
            operator = self.rules_table.item(row, 2).text()
            value = self.rules_table.item(row, 3).text()
            rule_texts.append(f"{parameter} {operator} {value}")

        combined_rules = " | ".join(rule_texts)
        self.ui.rule_view_text.setPlainText(combined_rules)

    def get_rules_table_data(self):
        data = []
        row_count = self.rules_table.rowCount()
        column_count = self.rules_table.columnCount()

        for row in range(row_count):
            row_data = []
            for col in range(column_count):
                item = self.rules_table.item(row, col)
                if item is not None:
                    row_data.append(item.text())
            data.append(row_data)
        return data

    def accept_rules(self):
        if self.mode == "add":
            data = self.ui.rule_view_text.toPlainText()

            if data == "":
                self.accept()
                return

            rule_id = self.conn.add_new_rule_query(data)
            for row_data in self.get_rules_table_data():
                parameter = row_data[1]
                operator = row_data[2]
                value = row_data[3]
                self.conn.add_new_parameter_query(rule_id, parameter, operator, value)
            self.main_window.load_rules_list()
            self.accept()

        elif self.mode == "edit":
            rule_id = self.r_id
            self.update_rule_view_text()
            data = self.ui.rule_view_text.toPlainText()

            if data == "":
                self.conn.delete_rule_query(rule_id)
                self.main_window.load_rules_list()
                self.accept()

            self.conn.edit_rule_query(rule_id, data)
            for row_data in self.get_rules_table_data():
                parameter_id = row_data[0]
                parameter = row_data[1]
                operator = row_data[2]
                value = row_data[3]
                self.conn.edit_parameter_query(parameter_id, parameter, operator, value)

            self.main_window.load_rules_list()
            self.accept()
