from core.number_holder import NumberHolder
import pytest

def test_adding_of_number():
    holder = NumberHolder(100)
    holder.add(5)
    assert holder.number == 100+5


def test_subtracting_of_number():
    holder = NumberHolder(100)
    holder.subtract(5)
    assert holder.number == 100-5


def test_multiplying_of_number():
    holder = NumberHolder(100)
    holder.multiply(5)
    assert holder.number == 100*5


def test_dividing_of_number():
    holder = NumberHolder(100)
    holder.divide(5)
    assert holder.number == 100/5


def test_get_division_remainder():
    holder = NumberHolder(100)
    holder.reminder(6)
    assert holder.number == 100%6


def test_all_actions_in_row():
    holder = NumberHolder(100)
    holder.add(5)
    holder.subtract(6)
    holder.multiply(2)
    holder.add(2)
    holder.divide(100)

    assert holder.number == 2


def test_division_by_zero():
    holder = NumberHolder(1)
    with pytest.raises(ZeroDivisionError):
        holder.divide(0)
