import unittest
from math_quiz import integer_range, arithmetic_operator, numbers


class TestMathGame(unittest.TestCase):

    def test_integer_range_randomness(self):

        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = integer_range(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_arithmetic_operator_selection(self):

        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of selections
            operator = arithmetic_operator()
            self.assertIn(operator, valid_operators)


    def test_generate_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 3, '-', '10 - 3', 7),
                (4, 6, '*', '4 * 6', 24),
                (9, 3, '+', '9 + 3', 12),
                (7, 5, '-', '7 - 5', 2)

            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:

                problem, answer = numbers(num1, num2, operator)

                self.assertEqual(problem, expected_problem)

                self.assertEqual(answer, expected_answer)



if __name__ == "__main__":
    unittest.main()
