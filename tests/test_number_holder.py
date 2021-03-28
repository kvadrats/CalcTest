from core.number_holder import NumberHolder
import pytest

from unittest.mock import MagicMock, patch
import datetime


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


def test_slow_adding():
    holder = NumberHolder(100)
    start_time = datetime.datetime.now()
    holder.slow_adding(5)
    end_time = datetime.datetime.now()
    time_diff = end_time - start_time

    assert time_diff.seconds == 5


def test_mocking_of_slow_adding():
    holder = NumberHolder(100)
    mock_obj = MagicMock()
    mock_obj.return_value = holder.add(3)

    start_time = datetime.datetime.now()
    with patch("core.number_holder.NumberHolder.slow_adding", mock_obj):
        holder.slow_adding(3)

        end_time = datetime.datetime.now()
        time_diff = end_time - start_time
        assert time_diff.seconds == 0

        assert holder.number == 103


