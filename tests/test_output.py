import pytest

from output import Output
from approvaltests import verify


def test_report():
    output = Output()
    assert output.report == ""


def test_format_table():
    """Test the simplest table of objects"""

    class TestItem:
        def __init__(self, name, age, num_pets):
            self.name = name
            self.age = age
            self.num_pets = num_pets

    # Arrange
    items = [TestItem("Ann", 21, 1), TestItem("Bob", 45, 2), TestItem("Cath", 52, 4)]
    output = Output()

    # Act
    output.format_table(items)

    # Assert
    verify(output.report)


def test_format_table_not_collection():
    # Arrange
    items = "not an array"
    output = Output()

    # Act
    output.format_table(items)

    # Assert
    verify(output.report)


def test_format_table_from_object():
    # Arrange
    class TestItem1:
        def __init__(self, name, age, num_pets):
            self.name = name
            self.age = age
            self.num_pets = num_pets

    items = TestItem1("Ann", 21, 1)
    output = Output()

    # Act
    output.format_table(items)

    # Assert
    verify(output.report)


def test_format_table_with_sparse_columns():
    """Test table where rows have different heading names"""

    class TestItem1:
        def __init__(self, name, age, num_pets):
            self.name = name
            self.age = age
            self.num_pets = num_pets

    class TestItem2:
        def __init__(self, name, age, num_computers):
            self.name = name
            self.age = age
            self.num_computers = num_computers

    # Arrange
    items = [TestItem1("Ann", 21, 1), TestItem2("Bob", 45, 2), TestItem1("Cath", 52, 4)]
    output = Output()

    # Act
    output.format_table(items)

    # Assert
    verify(output.report)


def test_format_table_with_list_of_primitives():
    # Arrange
    items = [1, 2000, 3, 4]
    output = Output()

    # Act
    output.format_table(items)

    # Assert
    verify(output.report)


def test_format_table_with_list_of_mixed_primitives():
    # Arrange
    items = [1, 2, 'banana', 300, 4]
    output = Output()

    # Act
    output.format_table(items)

    # Assert
    verify(output.report)


def test_format_table_with_list_of_primitives_and_objects():
    class TestItem:
        def __init__(self, name, age, num_pets):
            self.name = name
            self.age = age
            self.num_pets = num_pets

    # Arrange
    items = [TestItem("Ann", 21, 1), 4500, 'banana', TestItem("Cath", 52, 4)]
    output = Output()

    # Act
    output.format_table(items)

    # Assert
    verify(output.report)


def test_format_table_with_list_of_dict():
    # Arrange
    items = [{
        'one': 1,
        'two': 2,
    }]
    output = Output()

    # Act
    output.format_table(items)

    # Assert
    verify(output.report)
