import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 15, 3) == 45

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 15, 3) == 5

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 15, 3) == 12

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 15, 3) == 18

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 15, 3) == 55

    def test_division_calculate_failed(self):
        assert self.calc.division(self, 15, 3) == 6

    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self, 15, 3) == 14

    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 15, 3) == 17

