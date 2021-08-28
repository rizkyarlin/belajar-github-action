import unittest
import calculator


class CalculatorTestCase(unittest.TestCase):
    def test_addition_can_provide_correct_answer(self):
        x = 3
        y = 4
        result = calculator.addition(x, y)
        correct_result = x + y
        self.assertEqual(result, correct_result)

    def test_divide_can_provide_correct_answer(self):
        x = 8
        y = 4
        correct_result = x / y
        result = calculator.divide(x, y)
        self.assertEqual(result, correct_result)

    def test_sum_three_numbers_correct(self):
        x = 1
        y = 2
        z = 3
        correct_result = x + y + z
        result = calculator.sum_three_numbers(x, y, z)
        self.assertEqual(result, correct_result)


if __name__ == '__main__':
    unittest.main()
