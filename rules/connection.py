from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("database.db")

        if not db.open():
            QtWidgets.QMessageBox.critical(
                None,
                "Cannot open database",
                "Unable to establish a database connection.",
                QtWidgets.QMessageBox.Cancel,
                QtWidgets.QMessageBox.NoButton,
            )
            return False

        query = QtSql.QSqlQuery()
        query.exec_(
            "CREATE TABLE IF NOT EXISTS parameters (id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "rule_id INTEGER, parameter TEXT, operator TEXT, value INTEGER,"
            "FOREIGN KEY(rule_id) REFERENCES rules(id))")

        query.exec_(
            "CREATE TABLE IF NOT EXISTS rules (id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "rule TEXT)"
        )
        return True

    def execute_query_as_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec_()
        return query

    def add_new_rule_query(self, rule):
        sql_query = "INSERT INTO rules (rule) VALUES (?)"
        self.execute_query_as_params(sql_query, [rule])

        query = QtSql.QSqlQuery("SELECT last_insert_rowid()")
        query.next()
        rule_id = query.value(0)
        return rule_id

    def add_new_parameter_query(self, rule_id, parameter, operator, value):
        sql_query = "INSERT INTO parameters (rule_id, parameter, operator, value) VALUES (?, ?, ?, ?)"
        self.execute_query_as_params(sql_query, [rule_id, parameter, operator, value])

    def edit_rule_query(self, rule_id, rule):
        sql_query = "UPDATE rules SET rule = ? WHERE id = ?"
        self.execute_query_as_params(sql_query, [rule, rule_id])

    def edit_parameter_query(self, parameter_id, new_parameter, new_operator, new_value):
        sql_query = "UPDATE parameters SET parameter = ?, operator = ?, value = ? WHERE id = ?"
        self.execute_query_as_params(sql_query, [new_parameter, new_operator, new_value, parameter_id])

    def delete_rule_query(self, r_id):
        sql_query = "DELETE FROM parameters WHERE rule_id = ?"
        self.execute_query_as_params(sql_query, [r_id])

        sql_query = "DELETE FROM rules WHERE id = ?"
        self.execute_query_as_params(sql_query, [r_id])

    def get_all_rules(self):
        sql_query = "SELECT id, rule FROM rules"
        query = self.execute_query_as_params(sql_query)

        rules = []
        while query.next():
            rule_id = query.value(0)
            rule_name = query.value(1)
            rules.append((rule_id, rule_name))
        return rules

    def get_rule_by_id(self, r_id):
        sql_query = ("SELECT rule FROM rules WHERE id = ?")
        query = self.execute_query_as_params(sql_query, [r_id])

        if query.next():
            rule_name = query.value(0)
            return rule_name

    def get_parameters_by_rule_id(self, r_id):
        sql_query = ("SELECT id, parameter, operator, value FROM parameters WHERE rule_id = ?")
        query = self.execute_query_as_params(sql_query, [r_id])

        parameters = []
        while query.next():
            parameters_dict = {
                "id": query.value(0),
                "parameter": query.value(1),
                "operator": query.value(2),
                "value": query.value(3),
            }
            parameters.append(parameters_dict)
        return parameters
