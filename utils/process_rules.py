import re


def compare_values(rule_value, table_value, operator):
    """Function to compare values based on the operator."""
    try:
        # Convert values to floats if possible
        rule_value_float = float(rule_value.replace(',', '').replace('$', ''))
        table_value_float = float(table_value.replace(',', '').replace('$', ''))

        if operator == "=":
            return rule_value_float == table_value_float
        elif operator == "<":
            return table_value_float < rule_value_float
        elif operator == ">":
            return table_value_float > rule_value_float
        elif operator == "<=":
            return table_value_float <= rule_value_float
        elif operator == ">=":
            return table_value_float >= rule_value_float
        else:
            return False  # Invalid operator
    except ValueError:
        # If conversion to float is not possible, compare as strings
        if operator == "=":
            return rule_value == table_value
        elif operator == "<":
            return table_value < rule_value
        elif operator == ">":
            return table_value > rule_value
        elif operator == "<=":
            return table_value <= rule_value
        elif operator == ">=":
            return table_value >= rule_value
        else:
            return False  # Invalid operator


def check_rules(rules_list, output_table):
    """Check a list of rules against data from the table."""
    passed_rule = None  # Initially assume no rule passes

    for rule_index, rule in enumerate(rules_list):
        # Split the rule into individual conditions separated by | (OR)
        conditions = rule.split(' | ')
        rule_passed = True  # Assume rule passes until all conditions are checked

        for condition in conditions:
            # Use regex to extract the parameter, operator, and value
            match = re.match(r"(\w+\s\w+|\w+)\s*(>=|<=|=|>|<)\s*(\S+)", condition.strip())
            if match:
                param = match.group(1).strip()
                operator = match.group(2).strip()
                value = match.group(3).strip()

                # Find the parameter in the table (e.g., in the output_table dictionary)
                if param in output_table:
                    table_value = output_table[param]

                    # Compare the value from the table and the rule, considering the operator
                    if not compare_values(value, table_value, operator):
                        rule_passed = False  # If any condition fails, the rule doesn't pass
                        break
                else:
                    rule_passed = False  # If parameter is not found in the table, the rule doesn't pass
                    break
            else:
                rule_passed = False  # If the condition format is invalid, the rule doesn't pass
                break

        # If the rule passes, record its number
        if rule_passed:
            passed_rule = rule_index + 1  # Rule number (1-based index)
            break  # Stop the loop as we've found the first matching rule

    return passed_rule
