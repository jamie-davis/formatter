from ObjectAnalysis.column_classifier import classify_columns
from ObjectAnalysis.field_extractor import FieldExtractor


def map_values(values, columns):
    col_index = 0
    num_columns = len(columns)
    value = iter(values)
    line = ''
    for col in columns:
        col_index += 1

        col_value = str(next(value))
        if not col.left_align:
            col_value = col_value.rjust(col.required_width)

        if (col_index < num_columns):
            col_value = col_value.ljust(col.required_width + 1)

        line += col_value

    return line + "\n"


class Output:
    """ Class for formatting text data. Call the methods of the class to fill the report buffer and then access the
    formatted data using the report property."""
    def __init__(self):
        self.report = ''

    def format_table(self, items):
        """Format a list of objects as a report"""
        fields = FieldExtractor.extract(items)
        columns = classify_columns(fields)

        if any([col.heading for col in columns if col.heading is not None]):
            self.report += map_values([col.heading if col.heading is not None else '' for col in columns], columns)
            self.report += map_values([('-' * col.required_width) for col in columns], columns)

        for item in fields.rows:
            values = [item[col.heading] if col.heading in item.keys() else '' for col in columns]
            self.report += map_values(values, columns)
