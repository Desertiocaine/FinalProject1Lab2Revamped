import unittest
from grades import calculate_grades, calculate_final_grade

class TestGrades(unittest.TestCase):
    """Test case for the calculate_grades function."""

    def test_calculate_grades(self):
        """Test the grading system with a predefined set of scores."""
        scores = [95, 85, 75, 65, 55]
        expected_grades = ['A', 'B', 'C', 'D', 'F']
        result = calculate_grades(scores)
        self.assertEqual(result, expected_grades)

    def test_empty_scores(self):
        """Test with an empty list of scores."""
        scores = []
        expected_grades = []
        result = calculate_grades(scores)
        self.assertEqual(result, expected_grades)

    def test_edge_scores(self):
        """Test with edge scores to verify correctness at grade boundaries."""
        scores = [100, 90, 80, 70, 60]
        expected_grades = ['A', 'A', 'B', 'C', 'D']
        result = calculate_grades(scores)
        self.assertEqual(result, expected_grades)

    def test_calculate_final_grade(self):
        """Test for calculate_final_grade with various score lists."""
        self.assertEqual(calculate_final_grade([90, 80, 70]), 80.0)
        self.assertEqual(calculate_final_grade([100]), 100.0)
        with self.assertRaises(ValueError):
            calculate_final_grade([])

if __name__ == '__main__':
    unittest.main()