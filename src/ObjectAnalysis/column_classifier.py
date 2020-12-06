from collections import defaultdict
from enum import IntEnum, auto


class ColumnType(IntEnum):
    MIXED = auto()
    STRING = auto()
    NUMBER = auto()
    DATE = auto()
    UNKNOWN = auto()


def classify_columns(field_extract):
    return [ClassifiedColumn.classify(key, field_extract) for key in field_extract.keys]


def classify(value):
    types = {
        'int': ColumnType.NUMBER,
        'float': ColumnType.NUMBER,
        'str': ColumnType.STRING,
        'date': ColumnType.DATE,
        'datetime': ColumnType.DATE,
        'time': ColumnType.DATE,
        'complex': ColumnType.NUMBER
    }
    return types.get(type(value).__name__, ColumnType.UNKNOWN)


def get_types(values):
    column_types = defaultdict(int)
    for value in values:
        column_types[classify(value)] += 1
    return column_types


def calculate_width(values):
    return max([max([len(line) for line in str(value).splitlines()]) for value in values])


class ClassifiedColumn:
    def __init__(self, heading, left_align, required_width, column_type):
        self.heading = heading
        self.left_align = left_align
        self.required_width = required_width
        self.column_type = column_type

    @staticmethod
    def classify(key, field_extract):
        values = [row[key] for row in field_extract.rows if key in row.keys()]
        value_types = get_types(values)
        if len(value_types) > 1:
            column_type = ColumnType.MIXED
        else:
            column_type = next(iter(value_types))

        return ClassifiedColumn(key, column_type != ColumnType.NUMBER, max(len(key) if key is not None else 0, calculate_width(values)), column_type)
