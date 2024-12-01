import unittest
from grades import calculate_grades


class TestGrades(unittest.TestCase):
    """
    Test case for the calculate_grades function.
    """

    def test_calculate_grades(self):
        """
        Test the grading system with a predefined set of scores.
        Ensure the calculated grades match the expected results.
        """
        scores = [95, 85, 75, 65, 55]
        expected_grades = ['A', 'B', 'C', 'D', 'F']
        result = calculate_grades(scores)

        # Output debug information for each comparison
        print(f"Calculated: {result}, Expected: {expected_grades}")

        self.assertEqual(result, expected_grades)

    def test_empty_scores(self):
        """
        Test with an empty list of scores.
        The expected result should be an empty list of grades.
        """
        scores = []
        expected_grades = []
        result = calculate_grades(scores)

        print(f"Calculated: {result}, Expected: {expected_grades}")

        self.assertEqual(result, expected_grades)

    def test_edge_scores(self):
        """
        Test with edge scores to verify correctness at grade boundaries.
        """
        scores = [100, 90, 80, 70, 60]
        expected_grades = ['A', 'A', 'B', 'C', 'D']
        result = calculate_grades(scores)
        print(f"Calculated: {result}, Expected: {expected_grades}")
        self.assertEqual(result, expected_grades)


if __name__ == "__main__":
    unittest.main()
