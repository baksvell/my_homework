import pytest
from src.utils import data_convert, transaction_convert, operation_amount, presentation, operation_list


def test_data_convert():
    assert data_convert("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_data_convert_empty():
    assert data_convert("") == "Дата не указана"


def test_transaction_convert():
    assert transaction_convert("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert transaction_convert("Счет 35383033474447895560") == "Счет **5560"


def test_transaction_convert_empty():
    with pytest.raises(AttributeError):
        transaction_convert(None)


def test_operation_amount():
    assert operation_amount("123", "123") == "123 123"
    assert operation_amount("", "") == " "


def test_presentation_nodata():
    with pytest.raises(TypeError):
        presentation(None)


def test_operation_list():
    assert operation_list()