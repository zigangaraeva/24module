from app.calc import Calculator

class TestPositive:
    def setup(self):
        self.calc = Calculator

    def test_multiply (self):
        assert self.calc.multiply(self, 2, 3) == 6


    def test_division (self):
        assert self.calc.division(self, 15, 3) == 5


    def test_subtraction(self):
        assert self.calc.subtraction(self, 10, 3) == 7

    def test_adding(self):
        assert self.calc.adding(self, 10, 3) == 13

