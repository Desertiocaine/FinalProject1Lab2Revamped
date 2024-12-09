import unittest
from grades import calculate_grades, calculate_final_grade

class TestGrades(unittest.TestCase):
    def test_calculate_grades(self):
        scores = [95, 85, 75, 65, 55]
        expected_grades = ['A', 'A', 'B', 'C', 'D']
        result = calculate_grades(scores)
        self.assertEqual(expected_grades, result)

    def test_empty_scores(self):
        scores = []
        expected_grades = []
        result = calculate_grades(scores)
        self.assertEqual(result, expected_grades)

    def test_edge_scores(self):
        scores = [100, 90, 80, 70, 60]
        expected_grades = ['A', 'A', 'B', 'C', 'D']
        result = calculate_grades(scores)
        self.assertEqual(result, expected_grades)

    def test_calculate_final_grade(self):
        self.assertEqual(calculate_final_grade([90, 80, 70]), (80.0, 'B'))
        self.assertEqual(calculate_final_grade([100]), (100.0, 'A'))
        with self.assertRaises(ValueError):
            calculate_final_grade([])

if __name__ == '__main__':
    unittest.main()