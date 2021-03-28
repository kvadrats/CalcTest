

class NumberHolder():
    def __init__(self, number_to_handle):
        self.number = number_to_handle

    def add(self, number_to_add):
        self. number = self.number + number_to_add

    def subtract(self):
        raise NotImplementedError()

    def divide(self):
        raise NotImplementedError()

    def multiply(self):
        raise NotImplementedError()

    def divide_with_remainder(self):
        raise NotImplementedError()
