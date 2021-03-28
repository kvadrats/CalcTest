from core.number_holder import NumberHolder


def test_adding_of_number():
    holder = NumberHolder(100)
    holder.add(5)
    assert holder == 100+5


def test_subtracting_of_number():
    holder = NumberHolder(100)
    holder.subtract(5)
    assert holder == 100-5


def test_division():
    raise NotImplementedError()


def test_multiplication():
    raise NotImplementedError()


def test_get_division_remainder():
    raise NotImplementedError()


def test_all_actions_in_row():
    raise NotImplementedError()


def test_division_by_zero():
    raise NotImplementedError()