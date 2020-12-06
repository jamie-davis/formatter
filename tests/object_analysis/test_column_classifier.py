import datetime

from approvaltests import verify

from ObjectAnalysis.column_classifier import classify, calculate_width


def test_column_type_classifiers():
    values = [1, 1.1, 'string', [],
              complex(5, 3),
              datetime.date(2020, 11, 18),
              datetime.datetime(2020, 11, 18, 11, 35, 44, 500000),
              datetime.time(11, 36, 1, 998999)]
    result = ''
    for value in values:
        result += str(value) + ' ' + type(value).__name__ + ': ' + str(classify(value)) + "\n"
    verify(result)


def test_calculate_width():
    values = [1, 1.1, [],
              complex(5, 3),
              datetime.date(2020, 11, 18),
              datetime.datetime(2020, 11, 18, 11, 35, 44, 500000),
              datetime.time(11, 36, 1, 998999)]
    expected = max([len(str(value)) for value in values])
    assert calculate_width(values) == expected


def test_calculate_width_finds_longest_line():
    values = ["1234567890",
              """1234567890
12345678901234567890
123456789012345678901234567890
12345678901234567890
1234567890"""]
    assert calculate_width(values) == 30
