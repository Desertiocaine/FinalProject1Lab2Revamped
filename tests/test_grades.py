import unittest
from grades import calculate_grades

class TestGrades(unittest.TestCase):

    def test_calculate_grades(self):
        scores = [95, 85, 75, 65, 55]
        expected_grades = ['A', 'B', 'C', 'D', 'F']
        result = calculate_grades(scores)
        print(f"Calculated: {result}, Expected: {expected_grades}")
        self.assertEqual(result, expected_grades)

if __name__ == '__main__':
    unittest.main()