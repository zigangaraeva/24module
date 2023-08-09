import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator


    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 10


    def test_adding_unsuccess(self):
        assert self.calc.adding(self, 1, 1) == 10


    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 1, 0)