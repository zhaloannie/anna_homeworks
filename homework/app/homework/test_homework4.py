import pytest
from homework4 import is_valid_email, avg, uah_to_usd

#For email
def test_is_valid_email():
    assert is_valid_email('test@example.com') == True

def test_is_more_at_in_email():
    assert is_valid_email("test@@example.com") == False

def test_is_there_extra_point_in_email():
    assert is_valid_email("test@examplecom") == False

def test_empty_email():
    assert is_valid_email("") == False

#For avg
def test_avg_normal():
    assert avg([1,2,3,4,5]) == 3

def test_list_with_one_element():
    assert avg([7]) == 7

def test_list_with_negative_numbers():
    assert avg([-1,-2]) == -1.5

def test_list_is_empty():
    with pytest.raises(ValueError):
        avg([])

#For uah to usd

def test_normal_case():
    assert uah_to_usd(1000, 40) == 25

def test_invalid_rate():
    with pytest.raises(ValueError):
        uah_to_usd(1000, 0)

def test_invalid_amount():
    with pytest.raises(ValueError):
        uah_to_usd(-1000, 42)

def test_large_values():
    assert uah_to_usd(1_000_000, 50) == 20_000

def test_float_precision():
    result = uah_to_usd(100, 33.3)
    assert result == pytest.approx(3.003, rel=1e-3)