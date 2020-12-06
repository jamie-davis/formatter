import pytest
from approvaltests import verify

from ObjectAnalysis.field_extractor import FieldExtractor

def test_keys_are_extracted():
    class TestItem:
        def __init__(self, name, age, numPets):
            self.name = name
            self.age = age
            self.numPets = numPets

    # Arrange
    items = [TestItem("Ann", 21, 1), TestItem("Bob", 45, 2), TestItem("Cath", 52, 4)]

    # Act
    fx = FieldExtractor.extract(items)

    # Assert
    assert fx.keys == ["name", "age", "numPets"]


def test_row_values_are_extracted():
    class TestItem:
        def __init__(self, name, age, numPets):
            self.name = name
            self.age = age
            self.numPets = numPets

    # Arrange
    items = [TestItem("Ann", 21, 1), TestItem("Bob", 45, 2), TestItem("Cath", 52, 4)]

    # Act
    fx = FieldExtractor.extract(items)

    # Assert
    assert str(fx.rows) == str([vars(item) for item in items])


def test_row_values_are_extracted_from_a_tuple():
    class TestItem:
        def __init__(self, name, age, numPets):
            self.name = name
            self.age = age
            self.numPets = numPets

    # Arrange
    items = (TestItem("Ann", 21, 1), TestItem("Bob", 45, 2), TestItem("Cath", 52, 4))

    # Act
    fx = FieldExtractor.extract(items)

    # Assert
    assert str(fx.rows) == str([vars(item) for item in items])
