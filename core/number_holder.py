

class NumberHolder():
    def __init__(self, number):
        self.number = number

    def add(self, number_to_add):
        self.number += number_to_add
        return self.number

    def subtract(self, number_to_subtract):
        self.number -= number_to_subtract
        return self.number

    def multiply(self, number_to_multiply):
        self.number *= number_to_multiply
        return self.number

    def divide(self, number_to_divide):
        self.number /= number_to_divide
        return self.number

    def reminder(self, number_for_reminder):
        self.number %= number_for_reminder
        return self.number

